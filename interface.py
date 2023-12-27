from portScanner import PortScanner
from ddosAttack import DDOsAttack
class Interface:
    def __init__(self):
        self.port_scanner = None
        self.ddos_attack = None
        self.target = None
        self.start_range = None
        self.end_range = None
        self.nr_threads = None
        self.port_to_attack = None
        self.fake_ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

         #self.portScanner = PortScanner()


    def options(self):
        print("")
        option_selected = input("Enter option")
        if option_selected == '1':
            self.first_option()
        elif option_selected == '2':
            self.second_option()


    def first_option(self):
        print("-----------Let's scan-----------")

        self.target = input("What is going to be the target(IP): ")
        self.start_range = int(input("What is going to be the start range(Port-range): "))
        self.end_range = int(input("What is going to be the end range(Port-range): "))
        self.nr_threads = int(input("Number of threads: "))
        self.port_scanner = PortScanner(target=self.target, range_scan_start=self.start_range, range_scan_end=self.end_range, nr_of_threads=self.nr_threads)
        self.port_scanner.fill_queue()
        self.port_scanner.run_on_threads()
        self.port_scanner.check_port()
        print("-----------------------------------------------")
        print("The scan results ")
        self.port_scanner.print_opened_ports()

    def second_option(self):
        print("-----------Let's scan-----------")
        self.target = input("What is going to be the target(IP): ")
        self.nr_threads = int(input("Number of threads: "))
        self.port_to_attack = int(input("What port the attack will be performed: "))
        self.ddos_attack = DDOsAttack(target=self.target, fake_ips=self.fake_ips, port=self.port_to_attack, nr_of_threads=self.nr_threads)
        self.ddos_attack.attach_with_threads()
        self.ddos_attack.total_nr_attacks()





if __name__ == "__main__":
    interface = Interface()
    interface.options()


