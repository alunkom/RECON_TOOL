import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, URLopener, HTTPError


class WebScraper:
    def __init__(self, url):
        self.url = url


    def admin_finder(self,GREEN,RED,RESET):

        url = "http://"+self.url
        pages = open('modules/link.txt','r').read().splitlines()

        for page in pages:
            full_address = url+"/"+page
            req = requests.head(full_address)
            if req.status_code == 200 or req.status_code == 403:
                print(f" {GREEN} {full_address} is Exsists ====> 200 {RESET}")
            else :
                print(f" {RED} {full_address} is Not Exsists ====> 404 {RESET} ")    

