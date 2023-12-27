import function
import os
from pprint import pprint
from modules import whoii
from modules import HTTP_header
from modules import dnss
from modules import ip_location
from modules import sub_domains
from modules import Wordpress_Plugin
from modules import admin_page_finder
from modules import site_info
from modules import port_scanner

#----------------------------------------------------------------------------------------------------------------------------------------------

GREEN = function.GREEN
RED = function.RED
BLUE = function.BLUE
RESET = function.RESET
WHITE = function.WHITE

#----------------------------------------------------------------------------------------------------------------------------------------------

os.system('cls' or 'clear')
function.Tools.banner(None)

#----------------------------------------------------------------------------------------------------------------------------------------------

while True:
    
    function.Tools.options(None)

    try:
        
        num = input(f" {RED} [+] {WHITE} Enter a number from the list : {RESET}")
        
    #----------------------------------------------------------------------------------------------------------------------------------------------
    # WHOIS (1)
            
        if num == "1":
        
            domain = input(f" {RED} [+] {WHITE} Enter a Domain : {RESET}")
            informaition = whoii.Information(domain)
            ip = informaition.Get_ip(domain)
            print(f"\n {GREEN} [-] {WHITE} IP = {ip}")
            # domain_info = informaition.Domain_information(domain)
            print(f" {GREEN} [-] {WHITE} domain_info = \n ")
            server_info = informaition.Server_info(ip)
            # pprint(domain_info)
            print(f"{RESET}")
            pprint(server_info)
            
    #----------------------------------------------------------------------------------------------------------------------------------------------
    # DNS_Check (2)
    
        elif num == '2' :
            domain = input(f" {RED} [+] {WHITE} Enter a Domain : {RESET}")
            informaition_DNS = dnss.Dns(domain)
            a_record = informaition_DNS.check_a_record()
            mx_record = informaition_DNS.check_mx_record()
            ns_record = informaition_DNS.check_ns_record()
            soa_record = informaition_DNS.check_soa_record()
    
    #----------------------------------------------------------------------------------------------------------------------------------------------        
    # IP Location (3)
    
        elif num == '3':
            domain = input(f" {RED} [+] {WHITE} Enter a Domain : {RESET}")
            informaition_ip_location = ip_location.Ip_Location(domain)
            Ip_locaiton = informaition_ip_location.get_location()
    
    #----------------------------------------------------------------------------------------------------------------------------------------------
    # Sub Domains (4)

        elif num == "4":
            domain = input(f" {RED} [+] {WHITE} Enter a Domain : {RESET}")
            informaition_sub = sub_domains.Sub_Domain(domain)
            # informaition_check_domain = informaition_sub.check_domain()
            informaition_subdomain = informaition_sub.check_subdomains(BLUE,RESET,RED,GREEN)

    #----------------------------------------------------------------------------------------------------------------------------------------------
    # Wordpress Plugins (5)
    
        elif num == '5':
            domain = input(f" {RED} [+] {WHITE} Enter a Domain : {RESET}")
            informaition_wordpress = Wordpress_Plugin.Wordpress_Plugins(domain)
            wordpress_plugin = informaition_wordpress.Discover_Plugins(BLUE,RESET,RED,GREEN) 
    
    #----------------------------------------------------------------------------------------------------------------------------------------------
    # Admin page Finder (6)
    
        elif num == '6':
            domain = input(f" {RED} [+] {WHITE} Enter a Domain : {RESET}")
            informaition_admin = admin_page_finder.WebScraper(domain)
            informaition_admin_page = informaition_admin.admin_finder(GREEN,RED,RESET)
    
    #----------------------------------------------------------------------------------------------------------------------------------------------
    # WebSite Information
    
        elif num == '7' :
            domain = input(f" {RED} [+] {WHITE} Enter a Domain : {RESET}")
            info_site = site_info.Site_info(domain)
            info_site_out = info_site.Fetch_info(GREEN)
    
    #----------------------------------------------------------------------------------------------------------------------------------------------
    # Port Scanner 
    
        elif num == '8' :
            domain = input(f" {RED} [+] {WHITE} Enter a Domain : {RESET}")
            rrange = input(f" {RED} [**] {WHITE} Enter a Range of port( Ex: 20-25 ) :  {RESET}")
            port_scanner = port_scanner.Portscanner(domain,rrange,GREEN,RED,RESET)
            print("")
            port_scanner.Scan()
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #----------------------------------------------------------------------------------------------------------------------------------------------
       
        elif num == "9":
            try:
                domain = input(f" {RED} [+] {WHITE} Enter a Domain : {RESET}")
                domain = "http://"+domain
                http_header = HTTP_header.HTTP_Headers(domain)
                # http_header.fetch_headers()
                pprint(http_header.print_http_headers(domain))
            except:
                domain = "https://"+domain
                http_header = HTTP_header.HTTP_Headers(domain)
                pprint(http_header.print_http_headers(domain))
    
    #----------------------------------------------------------------------------------------------------------------------------------------------
            
        elif num == "0" :
            break
        
    #----------------------------------------------------------------------------------------------------------------------------------------------
            
    except Exception as e :
        print(f"{RED} Error : {e}")