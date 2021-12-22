import socket
import select
import mysql.connector
import sys

HEADER_LENGTH = 100

IP = "127.0.0.1"
PORT = 5000

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.settimeout(500)
# SO_ - socket option ... Sets REUSEADDR (as a socket option) to 1 on socket
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind, so server informs operating system that it's going to use given IP and port
# For a server using 0.0.0.0 means to listen on all available interfaces, useful to connect locally to 127.0.0.1 and remotely to LAN interface IP
server_socket.bind((IP, PORT))

# This makes server listen to new connections
server_socket.listen()
# List of sockets for select.select()
sockets_list = [server_socket]
# List of connected clients - socket as a key, user header and name as data
clients = {}

print(f'Listening for connections on {IP}:{PORT}...')

# CONNECTING TO DB AND CREATING TABLE IF NOT EXIST
def DBConnection():
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="mysql",
                database="Socket")
            print("DB CONNECTED SUCCESSFULLY")    
            mycursor = db.cursor(buffered=True)  
            mycursor.execute("CREATE TABLE IF NOT EXISTS CLIENTS(IP VARCHAR (255)  NOT NULL PRIMARY KEY,PORT VARCHAR(255) NOT NULL , Dname VARCHAR(255),Mname VARCHAR(255),Lname VARCHAR(255),phone INT(50),mail VARCHAR(255) UNIQUE,Birth_date Date,Doctor_ID INT(150) UNIQUE,syndicate_number INT (100) UNIQUE,salary INT(50),gender VARCHAR(255),address text,job_rank VARCHAR(255),access_level int DEFAULT 2,image LONGBLOB,calendarid VARCHAR (600) UNIQUE )")
            db.commit()
            print("TABLE CREATED SUCCESSFULLY")    
            #QMessageBox.about(self, 'Connection', 'Database Connected Successfully')
        except mysql.connector.Error as e:
            #QMessageBox.about(self, 'Connection', 'Failed To Connect Database')
            print("Failed To Connect Database")    
            #sys.exit(1)

def insert_data(ADDRESS,NAME):
    try:
        # CONNECTING TO DB AND CREATING TABLE IF NOT EXIST
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="mysql",
            database="Socket")
        print("DB CONNECTED SUCCESSFULLY")
        mycursor = db.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS CLIENTS(IPPORT VARCHAR (255)  NOT NULL , NAME VARCHAR(255), MSG VARCHAR(255))")
        #db.commit()
        print("TABLE CREATED SUCCESSFULLY")
        # INSERTING DATA IN THE TABLE
        sql = "INSERT INTO CLIENTS (IPPORT,NAME) VALUES (%s,%s)"
        val = (ADDRESS,NAME)
        mycursor.execute(sql, val)
        # COMMITING CHANGES TO THE DB
        db.commit()
        print("DATA INSERTED SUCCESSFULLY")

    except mysql.connector.Error as e:
        #self.labelResult.setText("Error Inserting Data")
        print(e.errno)

def update_data(ADDRESS,MSG):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="mysql",
            database="Socket")
        mycursor = db.cursor()
        sql = "UPDATE CLIENTS SET MSG = %s WHERE IPPORT = %s"
        val = (MSG,ADDRESS)
        mycursor.execute(sql, val)
        db.commit()
        print(MSG)
        print("MESSAGE UPDATED SUCCESSFULLY")
    except mysql.connector.Error as e:
      print('An exception occurred... ',e)

# Handles message receiving
def receive_message(client_socket):
    try:
        # Receive our "header" containing message length, it's size is defined and constant
        message_header = client_socket.recv(HEADER_LENGTH)
        # If we received no data, client gracefully closed a connection, for example using socket.close() or socket.shutdown(socket.SHUT_RDWR)
        if not len(message_header):
            return False
        # Convert header to int value
        message_length = int(message_header.decode('utf-8').strip())
        # Return an object of message header and message data
        return {'header': message_header, 'data': client_socket.recv(message_length)}
    except:
        # If we are here, client closed connection violently, for example by pressing ctrl+c on his script or just lost his connection
        # socket.close() also invokes socket.shutdown(socket.SHUT_RDWR) what sends information about closing the socket (shutdown read/write) and that's also a cause when we receive an empty message
        return False

while True:
    # Calls Unix select() system call or Windows select() WinSock call with three parameters:
    #   - rlist - sockets to be monitored for incoming data
    #   - wlist - sockets for data to be send to (checks if for example buffers are not full and socket is ready to send some data)
    #   - xlist - sockets to be monitored for exceptions (we want to monitor all sockets for errors, so we can use rlist)
    # Returns lists:
    #   - reading - sockets we received some data on (that way we don't have to check sockets manually)
    #   - writing - sockets ready for data to be send thru them
    #   - errors  - sockets with some exceptions
    # This is a blocking call, code execution will "wait" here and "get" notified in case any action should be taken
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
    # Iterate over notified sockets
    for notified_socket in read_sockets:
        # If notified socket is a server socket - new connection, accept it
        if notified_socket == server_socket:
            # Accept new connection That gives us new socket - client socket, connected to this given client only, it's unique for that client
            # The other returned object is ip/port set
            client_socket, client_address = server_socket.accept()
            # Client should send his name right away, receive it
            user = receive_message(client_socket)
            # If False - client disconnected before he sent his name
            if user is False:
                continue
            # Add accepted socket to select.select() list
            sockets_list.append(client_socket)
            # Also save username and username header
            clients[client_socket] = user
            print('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))
            # print(client_socket)
            print("client_address: {}:{}".format(*client_address))
            print("username: {}".format(user['data'].decode('utf-8')))
            insert_data("{}:{}".format(*client_address),user['data'].decode('utf-8'))

        # Else existing socket is sending a message
        else:
            # Receive message
            message = receive_message(notified_socket)
            # If False, client disconnected, cleanup
            if message is False:
                print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))
                # Remove from list for socket.socket()
                sockets_list.remove(notified_socket)
                # Remove from our list of users
                del clients[notified_socket]
                continue
            # Get user by notified socket, so we will know who sent the message
            user = clients[notified_socket]
            print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')
            print("client_address: {}:{}".format(*client_address))
            print("username: {}".format(user['data'].decode('utf-8')))
            update_data("{}:{}".format(*client_address),message['data'].decode('utf-8'))
            
            # Iterate over connected clients and broadcast message
            for client_socket in clients:
                # But don't sent it to sender
                if client_socket != notified_socket:
                    # Send user and message (both with their headers)
                    # We are reusing here message header sent by sender, and saved username header send by user when he connected
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
        # mes = input('server: ')
        # for client_socket in clients:
        #         # But don't sent it to sender
        #         if client_socket != notified_socket:
        #             # Send user and message (both with their headers)
        #             # We are reusing here message header sent by sender, and saved username header send by user when he connected
        #             client_socket.send(bytes(mes,'utf-8'))
    # It's not really necessary to have this, but will handle some socket exceptions just in case
    for notified_socket in exception_sockets:
        # Remove from list for socket.socket()
        sockets_list.remove(notified_socket)
        # Remove from our list of users
        del clients[notified_socket]
