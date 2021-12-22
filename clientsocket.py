import socket
import sys
import errno

class Client():
    # def __init__(self,msg:str):
    #     self.message = msg
    #     print(self.message)
    def __init__(self,user:str,msg:str):
        HEADER_LENGTH = 100
        IP = "127.0.0.1"
        PORT = 5000
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((IP, PORT))
        self.client_socket.setblocking(False)
        self.username = user.encode('utf-8')
        self.username_header = f"{len(self.username):<{HEADER_LENGTH}}".encode('utf-8')
        self.client_socket.send(self.username_header + self.username)
        while True:
            # message = input(f'{my_username} > ')
            self.message = msg
            if self.message:
                self.message = self.message.encode('utf-8')
                self.message_header = f"{len(self.message):<{HEADER_LENGTH}}".encode('utf-8')
                self.client_socket.send(self.message_header + self.message)

            try:
                while True:
                    self.username_header = self.client_socket.recv(HEADER_LENGTH)
                    if not len(self.username_header):
                        print('Connection closed by the server')
                        sys.exit()
                    self.username_length = int(self.username_header.decode('utf-8').strip())
                    self.username = self.client_socket.recv(self.username_length).decode('utf-8')
                    self.message_header = self.client_socket.recv(HEADER_LENGTH)
                    self.message_length = int(self.message_header.decode('utf-8').strip())
                    self.message = self.client_socket.recv(self.message_length).decode('utf-8')
                    print(f'{self.username} > {self.message}')
            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print('Reading error: {}'.format(str(e)))
                    sys.exit()
                continue

            except Exception as e:
                # Any other exception - something happened, exit
                print('Reading error: '.format(str(e)))
                sys.exit()
        
    

