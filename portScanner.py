import socket
import threading
from queue import Queue


class PortScanner:

    def __init__(self, target, range_scan_start, range_scan_end,
                 nr_of_threads):  # The target is going to be any IP address (in our case we are going to scan the router)
        self.queue = Queue()
        self.opened_ports = []
        self.target = target
        self.range_scan_start = range_scan_start
        self.range_scan_end = range_scan_end
        self.nr_of_threads = nr_of_threads

    def port_scan(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.target, port))
            return True
        except:
            return False

    # < WE CAN ALSO USE THIS METHOD BUT IS GOING TO BE WAY SLOWER BECAUSE OF THE IF COND. AND WE ARE NOT USING THREADS  >
    # def nr_of_ports_scanned(self):
    #     for port in range(self.range_scan_start,self.range_scan_end):
    #         result = self.port_scan(port)
    #         if result:
    #             print(f"The port: {port} is opened: {result}")
    #         else:
    #             print(f"The port: {port} is closed: {result}")

    def fill_queue(self):
        for port in range(self.range_scan_start, self.range_scan_end):
            self.queue.put(port)

    def check_port(self):
        while not self.queue.empty():
            port = self.queue.get()
            if self.port_scan(port):
                print(f"The port {port} is opened!!")
                self.opened_ports.append(port)

    def run_on_threads(self):
        thread_list = []
        for _ in range(self.nr_of_threads):
            thread = threading.Thread(target=self.check_port)
            thread_list.append(thread)

        for thread in thread_list:
            thread.start()

        for thread in thread_list:
            thread.join()

    def print_opened_ports(self):
        if len(self.opened_ports) == 0:
            print(f"There are no opened ports on IP address: {self.target}")
        else:
            for port in self.opened_ports:
                print(f"The port {port}, is OPENED check it out!")
