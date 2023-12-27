from portScanner import PortScanner

class Interface:
    def __init__(self):
        self.target = None
        self.start_range = None
        self.end_range = None
        self.nr_threads = None
        self.portScanner = None

         #self.portScanner = PortScanner()


    def options(self):
        option_selected = input("Enter option")
        if option_selected == '1':
            self.first_option()

    def first_option(self):
        print("-----------Let's scan-----------")

        self.target = input("What is going to be the target(IP): ")
        self.start_range = int(input("What is going to be the start range(Port-range): "))
        self.end_range = int(input("What is going to be the end range(Port-range): "))
        self.nr_threads = int(input("Number of threads: "))
        self.portScanner = PortScanner(target=self.target, range_scan_start=self.start_range, range_scan_end=self.end_range, nr_of_threads=self.nr_threads)
        self.portScanner.fill_queue()
        self.portScanner.run_on_threads()
        self.portScanner.check_port()
        print("-----------------------------------------------")
        print("The scan results ")
        self.portScanner.print_opened_ports()




if __name__ == "__main__":
    interface = Interface()
    interface.options()


