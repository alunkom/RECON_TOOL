import socket
import requests
import json
import socket
import requests
# from ip2geotools.databases.noncommercial import DbIpCity
# from ip2
# from geopy.distance import distance

class Ip_Location:
    
    def __init__(self, domain):
        self.domain = domain

    def get_location(self):
        
        try:
            ip = str(socket.gethostbyname(self.domain))
            response = requests.post(f"http://ip-api.com/json/{ip}")
            data = response.json()
            print("\n")
            for key,value in data.items() :
                print(f'       {key}:{value}')
            # print(f"      IP: {data['ip']}")
            # print(f"      Network: {data['network']}")
            # print(f"      Version: {data['version']}")
            # print(f"      ")
            # print(f"      Country: {data['country']}")
            # print(f"      Region: {data['region']}")
            # print(f"      City: {data['city']}")
            # print(f"      Org: {data['org']}")
                
        except socket.gaierror:
            print("       Invalid domain name.")
            return None

