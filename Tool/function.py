from colorama import init , Fore


init() # Call Colors
GREEN = Fore.GREEN
RED = Fore.RED
BLUE = Fore.BLUE
RESET = Fore.RESET
WHITE = Fore.WHITE

class Tools:
    
    def banner(self=None):
        
        print(f"""{BLUE}              
   ▄████████      ▄█           ███    █▄      ███▄▄▄▄          ▄█   ▄█▄      ▄██████▄        ▄▄▄▄███▄▄▄▄       
  ███    ███     ███           ███    ███     ███▀▀▀██▄       ███ ▄███▀     ███    ███     ▄██▀▀▀███▀▀▀██▄     
  ███    ███     ███           ███    ███     ███   ███       ███▐██▀       ███    ███     ███   ███   ███     
  ███    ███     ███           ███    ███     ███   ███      ▄█████▀        ███    ███     ███   ███   ███     
▀███████████     ███           ███    ███     ███   ███     ▀▀█████▄        ███    ███     ███   ███   ███     
  ███    ███     ███           ███    ███     ███   ███       ███▐██▄       ███    ███     ███   ███   ███     
  ███    ███     ███▌    ▄     ███    ███     ███   ███       ███ ▀███▄     ███    ███     ███   ███   ███     
  ███    █▀      █████▄▄██     ████████▀       ▀█   █▀        ███   ▀█▀      ▀██████▀       ▀█   ███   █▀      
                 ▀                                            ▀                                          
                 {Fore.CYAN}   
             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                                                            
            |  Coded By  : Mehdi Ojaghloo           |
            |  Email     : alunmom.mahdi@gmail.com  |
            |  Telegram  : @alunkomm                |
            |  Instagram : @mr_metim                |
             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
            {RESET}  """)

    def options(self=None):
            print(f"""  
        OPTIONS :
        {RED}
        [ 1 ]  -  Whois
        [ 2 ]  -  Dns Checker
        [ 3 ]  -  Ip Location
        [ 4 ]  -  Sub Domains
        [ 5 ]  -  WordPress Plugins
        [ 6 ]  -  Admin Page Finder
        [ 7 ]  -  WebSite Information
        [ 8 ]  -  Port Scanner
        [ 9 ]  -  Show HTTP Header  
          00   -  Return To Main Menu        
           0   -  Exit
         {RESET} """)
        

        