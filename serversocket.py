import socket
import select
import mysql.connector
import sys

HEADER_LENGTH = 100
IP = "127.0.0.1"
PORT = 5000


class Server():
    def __init__(self):
        super(Server,self).__init__()
        # Create a socket TCP/IP Connection
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.settimeout(5000)
        # SO_ - socket option ... Sets REUSEADDR (as a socket option) to 1 on socket
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind, so server informs operating system that it's going to use given IP and port
        # For a server using 0.0.0.0 means to listen on all available interfaces, useful to connect locally to 127.0.0.1 and remotely to LAN interface IP
        self.server_socket.bind((IP, PORT))
        # This makes server listen to new connections
        self.server_socket.listen()
        # List of sockets for select.select()
        self.sockets_list = [self.server_socket]
        # List of connected clients - socket as a key, user header and name as data
        self.clients = {}
        print(f'Listening for connections on {IP}:{PORT}...')
        # CONNECTING TO DB AND CREATING TABLE IF NOT EXIST

    
    def insert_data(self,ADDRESS, NAME):
        try:
            # CONNECTING TO DB AND CREATING TABLE IF NOT EXIST
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="mysql",
                database="Socket")
            print("DB CONNECTED SUCCESSFULLY")
            self.mycursor = self.db.cursor()
            self.mycursor.execute("CREATE TABLE IF NOT EXISTS CLIENTS(IPPORT VARCHAR (255)  NOT NULL , NAME VARCHAR(255), MSG VARCHAR(255))")
            print("TABLE CREATED SUCCESSFULLY")
            # INSERTING DATA IN THE TABLE
            self.sql = "INSERT INTO CLIENTS (IPPORT,NAME) VALUES (%s,%s)"
            self.val = (ADDRESS, NAME)
            self.mycursor.execute(self.sql, self.val)
            # COMMITING CHANGES TO THE DB
            self.db.commit()
            print("DATA INSERTED SUCCESSFULLY") 
        except mysql.connector.Error as e:
            #self.labelResult.setText("Error Inserting Data")
            print(e.errno)
    
    def update_data(self,ADDRESS, MSG):
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="mysql",
                database="Socket")
            self.mycursor = self.db.cursor()
            self.sql = "UPDATE CLIENTS SET MSG = %s WHERE IPPORT = %s"
            self.val = (MSG, ADDRESS)
            self.mycursor.execute(self.sql, self.val)
            self.db.commit()
            print(MSG)
            print("MESSAGE UPDATED SUCCESSFULLY")
        except mysql.connector.Error as e:
            print('An exception occurred... ', e)
        
        # Handles message receiving
    def receive_message(self,client_socket):
        try:
            # Receive our "header" containing message length, it's size is defined and constant
            self.message_header = client_socket.recv(HEADER_LENGTH)
            # If we received no data, client gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
            if not len(self.message_header):
                return False
            # Convert header to int value
            message_length = int(self.message_header.decode('utf-8').strip())
            # Return an object of message header and message data
            return {'header': self.message_header, 'data': client_socket.recv(message_length)}
        except:
            # If we are here, client closed connection violently, for example by pressing ctrl+c on his script or just lost his connection
            # socket.close() also invokes socket.shutdown(socket.SHUT_RDWR) what sends information about closing the socket (shutdown read/write) and that's also a cause when we receive an empty message
            return False
    
    def server_Run(self):
        self.read_sockets, _, self.exception_sockets = select.select(self.sockets_list, [], self.sockets_list)
        # Iterate over notified sockets
        for self.notified_socket in self.read_sockets:
            # If notified socket is a server socket - new connection, accept it
            if self.notified_socket == self.server_socket:
                # Accept new connection That gives us new socket - client socket, connected to this given client only, it's unique for that client
                # The other returned object is ip/port set
                self.client_socket, self.client_address = self.server_socket.accept()
                # Client should send his name right away, receive it
                self.user = self.receive_message(self.client_socket)
                # If False - client disconnected before he sent his name
                if self.user is False:
                    continue
                # Add accepted socket to select.select() list
                self.sockets_list.append(self.client_socket)
                # Also save username and username header
                self.clients[self.client_socket] = self.user
                print('Accepted new connection from {}:{}, username: {}'.format(*self.client_address, self.user['data'].decode('utf-8')))
                # print(client_socket)
                print("client_address: {}:{}".format(*self.client_address))
                print("username: {}".format(self.user['data'].decode('utf-8')))
                self.insert_data("{}:{}".format(*self.client_address), self.user['data'].decode('utf-8'))
            # Else existing socket is sending a message
            else:
            # Receive message
                self.message = self.receive_message(self.notified_socket)
                # If False, client disconnected, cleanup
                if self.message is False:
                    print('Closed connection from: {}'.format(self.clients[self.notified_socket]['data'].decode('utf-8')))
                    # Remove from list for socket.socket()
                    self.sockets_list.remove(self.notified_socket)
                    # Remove from our list of users
                    del self.clients[self.notified_socket]
                    continue
                # Get user by notified socket, so we will know who sent the message
                self.user = self.clients[self.notified_socket]
                print(f'Received message from {self.user["data"].decode("utf-8")}: {self.message["data"].decode("utf-8")}')
                print("client_address: {}:{}".format(*self.client_address))
                print("username: {}".format(self.user['data'].decode('utf-8')))
                self.update_data("{}:{}".format(*self.client_address), self.message['data'].decode('utf-8'))
                # Iterate over connected clients and broadcast message
                for self.client_socket in self.clients:
                    # But don't sent it to sender
                    if self.client_socket != self.notified_socket:
                        # Send user and message (both with their headers)
                        # We are reusing here message header sent by sender, and saved username header send by user when he connected
                        self.client_socket.send(self.user['header'] + self.user['data'] + self.message['header'] + self.message['data'])
        # It's not really necessary to have this, but will handle some socket exceptions just in case
        for self.notified_socket in self.exception_sockets:
            # Remove from list for socket.socket()
            self.sockets_list.remove(self.notified_socket)
            # Remove from our list of users
            del self.clients[self.notified_socket]
            
if __name__ == "__main__":
    import sys
    server=Server()
    server.server_Run()
