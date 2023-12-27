import dns.resolver 


class Dns:
    
    def __init__(self,Domain):
        self.Domain = Domain
        
    def check_a_record(self,type="A"):
        try:
            result = dns.resolver.resolve(self.Domain,type)
            for ip in result:
                print("     IP:",ip)
        except Exception as e:
            print(str(e))                
                
    def check_mx_record(self):
        try:
            mx_records = dns.resolver.resolve(self.Domain,'MX')
            print("     MX_Resault:")
            for mx_result in mx_records:
                print("     ",mx_result)
        except Exception as e:
            print(str(e))
            
    def check_ns_record(self):
        try:
            ns_records = dns.resolver.resolve(self.Domain, 'NS')
            print("     NS_Resault:")
            for ns_result in ns_records:
                print("     ",ns_result)
        except Exception as e:
            print(str(e))            
        
    def check_soa_record(self):
        try:
            soa_record = dns.resolver.resolve(self.Domain, 'SOA')
            print("     SOA_Resault:")
            for SOA_result in soa_record :
                print("     ",SOA_result)
        except Exception as e:
            print(str(e))
