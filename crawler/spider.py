import requests as r
import os, sys, time
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs
from colorama import Fore, init
import threading

from tools.printer import file_handle_success, print_msg
from tools.progress import Progress
from tools.timer import Timer


lock = threading.Lock()

init()
links_array = []
progress = Progress()
timer = Timer()

class Spider:
  filename = "spider"
  def __init__(self):
    self.links_array = []
    self.err = None
    self.r = r.Session()
    self.i = 0
    
  def get_name(self):
    return self.filename
    
  def save_links(self, link):
    with open(self.filename, "a+") as link_file:
      link_file.write(link)
      
  def set_filename(self, url):
    url = url.replace("https://", "")\
    .replace("http://", "").split(".")[0]
    
    self.filename = "crawled_sites/{}.txt".format(url)
    
    if os.path.exists(self.filename):
      os.remove(self.filename)
    
    
  def request(self, url):
      response = self.r.get(url)
      if response:
        return response
        
  def soup(self, content):
    soup = bs(content, "html.parser")
    a_tags = soup.findAll("a")
    #forms = soup.findAll("form")
    
    return a_tags
    
  def surf_url(self, url):
    global links_array
    try:
      url = "https://{}".format(str(url)) if "https://" not in url else url
      response = self.request(url)
      a_tags = self.soup( response.content)
      
      for a in a_tags:
        href = a.get("href")
        link = urljoin(url, href).split("?")[0].split("#")[0]
        
        if link not in links_array and url in link and link != url and link != url+"/":
          
          #lock.acquire()
            
          links_array.append(link)
          print("[+] {}".format(link))
          
          #time.sleep(.1)
          #lock.release()
          
          self.surf_url(link)
      
      #self.i += 1
      #progress.bar.update(self.i)
    
    except KeyboardInterrupt:
      print("\n{}[¶]{} Detected <CTRL+C>, Quitting Crawler...".format(Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.RESET))
      print("{}[✓]{} {}Check {} for sitemap result list{}\n"\
      .format(Fore.LIGHTGREEN_EX, Fore.RESET, Fore.LIGHTYELLOW_EX, web_spider.filename, Fore.RESET))
      
    except r.exceptions.MissingSchema:
      print("{0}[∆] Missing Schema for {3}<Host> --> {1}{2}{3}\n"\
      .format(Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, url, Fore.RESET))
      return False
      
      
    except r.exceptions.ConnectionError:
      print("{0}[∆] Error while connecting to {3}<Host> --> {1}{2}{3}\n"\
      .format(Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, url, Fore.RESET))
      return False

    #except:
      #print("{0}[∆] Unable to connect to {3}<Host> --> {1}{2}{3}\n"\
        #.format(Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, url, Fore.RESET))
      #sys.exit()


def crawl(target_url, threads = 4):
  global links_array
  
  try:
    thread_list = []
    spider = Spider()
    spider.set_filename(target_url)
    
    timer.start_timer()
    spider.surf_url(target_url)
    
    #for i in range(threads):  
#      thread = threading.Thread(
#        target = spider.surf_url, 
#        args = (target_url, lock, ))
#        
#      thread_list.append(thread)
#      thread.start()
#        
#    for t in thread_list:
#      t.join()
    
    timer.get_timestamp()
    
  except KeyboardInterrupt:
    cmd = str(input("Do you really want to quit? y/n: "))
    if cmd == "y" or cmd == "Y" or cmd == "":
      sys.exit()
    elif cmd == "n" or cmd == "N":
      pass
   
  finally:
    timer.get_timestamp()
    
    for link in links_array:
      spider.save_links(link + "\n")
    
    file_handle_success("./" + spider.filename)
    timer.get_timestamp()

    print(" ")
    exit()
    
    # print_msg("info", "Restarting program in 10 seconds")
    # time.sleep(10)
      
    
    # except:
      # print("{0}[∆] Error while connecting to {3}<Host> --> {1}{2}{3}\n"\
        # .format(Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, url, Fore.RESET))

      # break




