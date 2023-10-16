import function
import os
from modules import whoii
from pprint import pprint

GREEN = function.GREEN
RED = function.RED
BLUE = function.BLUE
RESET = function.RESET
WHITE = function.WHITE

os.system('cls' or 'clear')
function.Tools.banner(None)

while True:
    
    function.Tools.options(None)

    try:
        
        num= input(f" {RED} [+] {WHITE} Enter a number from the list : {RESET}")
        
        if num == "1":
        
            domain = input(f" {RED} [+] {WHITE} Enter a Domain : {RESET}")
            informaition = whoii.Information(domain)
            ip = informaition.Get_ip(domain)
            print(f"\n {GREEN} [-] {WHITE} IP = {ip}")
            domain_info = informaition.Domain_information(ip)
            # server_info = informaition.Server_info(domain)
            print(f" {GREEN} [-] {WHITE} domain_info = \n")
            pprint(domain_info)
            # print(server_info)
    
        elif num == "0" :
            break
    except Exception as e :
        print(f"{RED} Error : {e}")