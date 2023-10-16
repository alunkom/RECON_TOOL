from ipwhois import IPWhois
import whois,socket
from whois import WhoisPrivateRegistry


class Information:
        
    def __init__ (self , domain):
        self.domain = domain
    
    def Get_ip (self,domain):
        ip = socket.gethostbyname(domain)
        return ip
    
    def Domain_information(self,ip):
        obj = IPWhois(ip)
        return obj.lookup_whois()
    
    def Server_info(self,domain):
        ip = Information.Get_ip(domain)
        info = IPWhois(ip)
        info = info.lookup_whois()
        return info     

