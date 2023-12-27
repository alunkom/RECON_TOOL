import requests
from requests.exceptions import MissingSchema, InvalidSchema
import time

class Sub_Domain:
    
    def __init__(self, domain_name):
        self.domain_name = domain_name

    def check_domain(self):
        req = requests.head(f'http://{self.domain_name}')
        if req.status_code == 200 or req.status_code == 403:
            print(f'Domain {self.domain_name} exists')
            return True
    
    def check_subdomains(self, BLUE, RESET, RED, GREEN):
        
        discoverd_subdomain = []
        sub_list = []
        
        with open("modules/Subdomain.txt", 'r')as file:
            subdomains = file.readlines()
            for i in subdomains:
                sub = i.strip("\n")
                sub_list += [sub] 
                
        for sub in sub_list:
            time.sleep(1)
            url = f'https://{sub}.{self.domain_name}'
            try:                
                req = requests.head(url)
                if req.status_code == 200 or req.status_code == 403:
                    print(f" {GREEN} [+]  Discovered Subdomain : {BLUE} {sub} {RESET}")
                    discoverd_subdomain += [url]
                else:
                    print(f" {RED} [-]  Not Found Plugin : {sub} {RESET}")
            except:
                print(f" {RED} [-]  Not Found Plugin : {sub} {RESET}")
                
        with open(f"results/plugins/{self.domain_name}.txt", "w") as f:
            for subdomian in discoverd_subdomain:
                f.write(subdomian) 
