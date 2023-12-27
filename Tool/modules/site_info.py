import builtwith
class Site_info:
    def __init__(self, domain):
        self.domain = domain

    def Fetch_info(self, GREEN):
        response = builtwith.builtwith("http://"+self.domain)
        for i in response:
            print(f"      {GREEN} {i}", response[i])