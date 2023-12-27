import requests
from urllib.parse import urlparse

class HTTP_Headers:
    
    def __init__(self,domain):
        self.domain = domain
        # self.headers = None
        # self.parse_url()
        
    def parse_url(self):
        parsed_url = urlparse(self.domain)
        self.domain = parsed_url.netloc
    
    # def fetch_headers(self):
        
        
    #     #     self.headers = response.headers
    #     #     return True
    #     # else:
    #     #     print("Error: Unable to fetch headers")
    #     #     return False           
             
    def print_http_headers(self,domain):
        # parsed_url = urlparse(self.domain)
        # self.domain = parsed_url.netloc
        response = requests.get(self.domain)
        # if self.headers is not None:
        if response.status_code == 200:
            print("     HTTP_Headers:")
            for key, value in response.headers.items():
                print(f"  {key} : {value}")
        # else:
            # print("     Error: Headers not fetched yet")
                    
                
        
            