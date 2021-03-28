import time
from methods.printer import clear_console, print_tool_name, get_input
from methods.list_tools import list_commands
from methods.loader import Loader
from colorama import Fore

commands = ["Exit Current Program"]
  
def get_entry():
  entry = get_input("Target url")
  print("")
  
  return entry
  

def web_crawler(spider):
  
  print_tool_name("Hack Spider 🕷️", "Devvyhac", "Team Trace Techie", "github.com/devvyhac")

  list_commands(commands)
  print("")
  target_url = get_entry()
  
  while True: 
    try:
      
      if target_url == "90":
        clear_console()
        quiting = Loader(load_text="Terminating HACK SPIDER", load_type="info", feedback="HACK SPIDER Terminated")
        quiting.load()
        quiting.terminate(timeout=1.2, seize=0)
        break
      
      print("{}[+] {}Crawling...{}"\
      .format(
      Fore.LIGHTGREEN_EX, 
      Fore.LIGHTYELLOW_EX, 
      Fore.RESET
    ))
  
      spider.crawl(target_url)
      
      time.sleep(2)
      clear_console()    
      loader = Loader(load_text="Resetting variables", load_type="success", feedback="Variables reset, successfully")
      loader.load()
      loader.terminate(timeout=1.2,seize=0)
      
      print_tool_name("Hack Spider 🕷️", "Devvyhac", "Team Trace Techie", "github.com/devvyhac")

      list_commands(commands)
      target_url = get_entry()
       
    except KeyboardInterrupt:
      break
      
   