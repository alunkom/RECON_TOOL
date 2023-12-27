import socket


class Portscanner :
    def __init__(self,domain,rrange,GREEN,RED,RESET) :
        self.domain = domain
        self.range = rrange
        self.green = GREEN
        self.red = RED
        self.reset = RESET


    def Scan(self):
        ip = str(socket.gethostbyname(self.domain))
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        rrange = self.range.split('-')  # 20-30 

        try:
            for port in range(int(rrange[0]),int(rrange[1])) :

                result = scanner.connect_ex((ip, port))

                if result == 0:
                    print(f" {self.green} [+] Port {port} is Open {self.reset}")

                else:  
                    print(f" {self.red} [-] Port {port} is Close {self.reset}") 

        except socket.gaierror:
            print(f" {self.red} Server Not responding {self.reset}")