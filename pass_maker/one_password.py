import random, string
from colorama import Fore

from tools.printer import print_msg, print_tool_name
from tools.confirm import confirm_exit

from .generator import get_pass_length

pass_chars = string.ascii_letters + string.digits + string.punctuation

def yield_one_password():
  print_tool_name("One Auth", "Devvyhac", "Team Trace Techie", "github.com/devvyhac")
  while True:
    try:
      password = (random.choice(pass_chars) for p in range(get_pass_length()))
      password = "".join(password)
      print_msg("success", "\nYour Password °•.> {} {} {} ".format(Fore.LIGHTYELLOW_EX, password, Fore.RESET))
      print("")
    
      restart = confirm_exit("{}Do you want to generate another Password? Y/n: ".format(Fore.CYAN), no_reload = True)
      if restart:
        continue
      
      else:
        break
        
    except KeyboardInterrupt:
      break
