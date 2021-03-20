import sys, os, time, threading
from colorama import Fore 

from .printer import print_msg, clear_console
from .loader import Loader
from .list_tools import list_items

from crawler import spider
from crawler.web_crawler import web_crawler

from pass_maker.password_generator import generate_password
from pass_maker.one_password import yield_one_password

def run_tool(index, tools, commands, delay=1.2):
  try:
    switcher = {
      1: {
           "func": lambda: web_crawler(spider),
           "name": "Hack Spider"
         },
      2: {
           "func": lambda: generate_password(),
           "name": "Lazy Auth"
         },
      3: {
           "func": lambda: yield_one_password(), 
           "name": "One Auth"
         }
    }
    
    if switcher[index]:
      
      clear_console()
      loader = Loader(load_text="Starting {}".format(switcher[index]['name'].upper()), load_type="success", feedback="Program loads Successfully!")
      loader.load()
      loader.terminate(timeout=2)
      
      return switcher[index]['func']()
    
  except KeyError:
    clear_console()
    loader = Loader(load_type="info", load_text="Selected Tools, Not Available! • Fetching Tools", feedback = "Invalid Entry, Use digits!")
    loader.load()
    loader.terminate(timeout=2, seize= 2)
    
    print_msg("error", "Option {}•[{}]•{} not Valid!".format(Fore.CYAN, index, Fore.RED), clear=True)
    
    #list_items(tools, commands)
    
  #except:
    # print_msg("err", "Option {0}•[{1}]•{2} not Valid!"\
      #.format(color.LIGHTYELLOW_EX, index, color.RED), color=color)
    