import os, sys, time
from colorama import Fore
from art import *


from tools.list_tools import list_items, list_commands, list_tools
from tools.printer import print_msg, get_input, clear_console, print_tool_name
from tools.loader import Loader
from tools.run_tool import run_tool
from tools.confirm import confirm_exit
from tools.fancy import fancy_typo, fancy_text

commands = ["List Tools", "Exit"]
tools = ["Hack Spider •     [ Web Crawler, gets the sitemap ]", 
         "Lazy Auth •       [ Password list Generator ]", 
         "One Auth •        [ Unique Password Generator ]", 
         "ATM Machine •     [ ATM Machine simulator ]",
         "iGuess Num •      [ A number guessinggame with incremental stages and stores players data in a database ]",
         "Aboki $FX •       [ A currency converter ]",
         "Dictionary •      [ A simple offline dictionary ]",
         "Brute Auth •      [ Coming soon ]", 
         "Anon Chat •       [ Coming soon ]", 
         "WiF-i •           [ Coming soon ]", 
         "Cam Hijack •      [ Coming soon ]", 
         "Hoarder •         [ Coming soon ]"]


clear_console()
is_active = True


toolname = fancy_typo("HACKSTER", "fancy12")
loader = Loader(load_text="Loading {}".format(toolname), load_type="success", feedback="{} Successfully Loaded".format(toolname))
loader.load()
loader.terminate(timeout=1.5)

print_tool_name("HACKSTER", "Devvyhac", "Team Trace Techie", "github.com/devvyhac")


def get_command():
  list_commands(commands) 
  option = get_input("\nEnter option")
    
  return option

def hackster():
  global is_active  
  while is_active:
    if not is_active:
      break
      
    try:
      option = int(get_command())
      
      if option == 91:
        confirm = confirm_exit("Do you really want to quit? Y/n: ")
        if confirm == True:
          sys.exit()
          
        pass
    
      elif option == 90:
        clear_console()
        reload = Loader(load_text="Fetching Tools", load_type="success")
        reload.load()
        reload.terminate(timeout=1.2)
        list_tools(tools)
    
      else:
        option = int(option)
        running = run_tool(option, tools, commands)
        continue

    
    except KeyboardInterrupt:
      if confirm_exit("Do you really want to quit? Y/n: "):
        break
        
      continue
    
    except ValueError:
      clear_console()
      loader = Loader(load_type="info", load_text="Wrong Entry! • Fetching Tools", feedback = "Invalid Entry, Use digits!")
      loader.load()
      loader.terminate(timeout=2)
      print_msg("error", "Only Digits are allowed!", clear=True)
      
      continue
      
      
    #except:
      #print("another new error")

hackster()