import requests
import time as t


class Wordpress_Plugins:
    
    def __init__(self, domain):
        self.domain = domain
        
    def Discover_Plugins(self, BLUE, RESET, RED, GREEN):
        plugin_list = []
        discoverd_plugins_list = []
        file = open("modules/plugins.txt")
        content = file.readlines()
        for i in content:
            plugin_with_n = i.strip("\n")
            plugin_list += [plugin_with_n]
            
           
        for plug in plugin_list: 
            url = f"http://{self.domain}{plug}"
            response1 = requests.head(url)
            if response1.status_code == 200 or response1.status_code == 403:
                t.sleep(1)
                print(f" {GREEN} [+] Discovered Plugin : {BLUE} {plug} {RESET}")
                discoverd_plugins_list.append(url)
            else:
                print(f" {RED} [-]  Not Found Plugin : {plug} {RESET}")
                
            with open(f"results/plugins/{self.domain}.txt", "w") as f:
                for plug in discoverd_plugins_list:
                    f.write(plug)           

