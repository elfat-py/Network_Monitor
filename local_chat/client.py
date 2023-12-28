import socket
import threading


class Client:
    def __init__(self, nickname):
        self.local_host = self.get_loopback_address()
        self.client = self.request_connection()
        self.nickname = nickname

        self.port = 66666

    def get_loopback_address(self):
        return socket.gethostbyname("localhost")
    def request_connection(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.local_host, 33333))
        return client

    def listen_message(self):
        while True:
            try:
                message = self.client.recv(1024).decode('ascii')
                if message == 'NICK':
                    self.client.send(self.nickname.encode('ascii'))
                else:
                    print(message)
            except:
                # Close Connection When Error
                print("An error occurred!")
                self.client.close()
                break

    def write(self):
        while True:
            message = '{}: {}'.format(self.nickname, input(''))
            self.client.send(message.encode('ascii'))

    def start_live_connection(self):
        write_thread = threading.Thread(target=self.write)
        write_thread.start()

        receive_thread = threading.Thread(target=self.listen_message)
        receive_thread.start()
client_name = input("Name: ")
client = Client(client_name)
client.start_live_connection()