from ipwhois import IPWhois
import whois,socket
from whois import WhoisPrivateRegistry
# import regex as rg
  
class Information:
        
    def __init__ (self , domain):
        self.domain = domain
    
    def Get_ip (self,domain):
        global ip
        ip = socket.gethostbyname(domain)
        return ip
    
    def Domain_information(self):
        domain_info = whois.query(self.domain)
        return domain_info
    
    def Server_info(self,domain):
        info = IPWhois(ip)
        server_info = info.lookup_whois()
        print("  ASN:",server_info['asn'])
        print("  ASN_CIDR:",server_info['asn_cidr'])
        print("  ASN_Country_Code:",server_info['asn_country_code'])
        print("  ASN_Date:",server_info['asn_date'])
        print("  ASN_Description:",server_info['asn_description'])
        print("  ASN_Registry:",server_info['asn_registry'])
        print("  Address:",server_info['nets']['address'])
        print("  Cidr:",server_info['nets']['cidr'])
        print("  City:",server_info['nets']['city'])
        print("   ")
        return info     

