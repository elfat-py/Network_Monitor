import socket
import threading

class Client:
    def __init__(self, nickname):
        self.local_host = self.get_loopback_address()
        self.client = self.request_connection()
        self.nickname = nickname
        self.port = 33333

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
                print(message)
            except:
                print("An error occurred!")
                self.client.close()
                break

    def write(self):
        while True:
            message = f"{self.nickname}: {input('')}"
            self.client.send(message.encode('ascii'))

    def start_live_connection(self):
        thread_write = threading.Thread(target=self.write)
        thread_listen = threading.Thread(target=self.listen_message)

        thread_write.start()
        thread_listen.start()

# Example usage
if __name__ == "__main__":
    client_nickname = input("Provide a nickname in order to join the room chat: ")
    chat_room_client = Client(client_nickname)
    chat_room_client.start_live_connection()
