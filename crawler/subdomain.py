import requests as r
from bs4 import BeautifulSoup as bs

def request(url):
  try:
    response = r.get(url)
    return response
  except r.exceptions.MissingSchema:
    pass
  except r.exceptions.ConnectionError:
    pass

protocol = "http://"
domain = "hackthebox.eu" 
with open("subdomain.txt", "r") as subdomain:
  for line in subdomain:
    word = line.strip()
    test_url = "{}{}.{}".format(protocol, word, domain)

    response = request(test_url)
    if response:
      print("[+] Subdomain Discovered <==> {}".format(test_url))
    else:
      print("[!] Subdomain not Found <==> {}".format(test_url))
# soup = request("https://farmapropos.com")
# print(soup)