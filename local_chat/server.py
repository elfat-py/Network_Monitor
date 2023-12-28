import threading
import socket


class Server:
    def __init__(self):
        self.local_host = self.get_loopback_address()
        self.server_socket = self.server_listen()
        self.port = 66666
        self.clients = []
        self.nicknames = []
        self.message = None
        self.client = None
        #self.server_start = self.receive()
        #self.receive()


    def get_loopback_address(self):
     return socket.gethostbyname("localhost")

    def server_listen(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.local_host, 33333))
        server.listen()
        return server


    def client_identification(self):
        self.clients = []
        self.nicknames = []

    def message_broadcast(self, message):
        for client in self.clients:
            try:
                client.send(message)
            except socket.error as e:
                print(f"There is some error trying to broadcast the message to {client}, problem: {e}")


    def handle(self):
        while True:
            try:
                # Broadcasting Messages
                self.message = self.client.recv(1024)
                self.message_broadcast(self.message)
            except Exception as e:
                # Removing And Closing Clients
                index = self.clients.index(self.client)
                self.clients.remove(self.client)
                self.client.close()
                nickname = self.nicknames[index]
                self.message_broadcast(f'{nickname} left!'.encode('ascii'))
                self.nicknames.remove(nickname)
                print(f"There was an error: {e}")
                break

    def receive(self):
        while True:
            # Accept Connection
            self.client, address = self.server_socket.accept()
            print("Connected with {}".format(str(address)))

            # Request And Store Nickname
            self.client.send('NICK'.encode('ascii'))
            nickname = self.client.recv(1024).decode('ascii')
            self.nicknames.append(nickname)
            self.clients.append(self.client)

            # Print And Broadcast Nickname
            print("Nickname is {}".format(nickname))
            self.message_broadcast("{} joined!".format(nickname).encode('ascii'))
            self.client.send('Connected to server!'.encode('ascii'))

            # Start Handling Thread For Client
            print("The connection has started! ")
            thread = threading.Thread(target=self.handle, args=(self.client,))
            thread.start()
    def run_server(self):
        while True:
            self.receive()

    def start_server(self):
        thread = threading.Thread(target=self.run_server)
        thread.start()

if __name__ == "__main__":
    server = Server()
    server.start_server()



# server_start = Server()
# server_start.start()

