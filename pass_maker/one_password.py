import random, string
from colorama import Fore

from methods.printer import print_msg, print_tool_name
from methods.confirm import confirm_exit

from .generator import get_pass_length

pass_chars = string.ascii_letters + string.digits + string.punctuation

def yield_one_password():
  print_tool_name("One Auth", "Devvyhac", "Trace Techie", "github.com/tracetechie")
  while True:
    try:
      password = (random.choice(pass_chars) for p in range(get_pass_length()))
      password = "".join(password)
      print_msg("success", "Your Password °•.> {}{}{} ".format(Fore.LIGHTYELLOW_EX, password, Fore.RESET))
    
      restart = confirm_exit("{}Do you want to generate another Password? Y/n: ".format(Fore.CYAN), no_reload = True)
      if restart:
        continue
      
      else:
        break
        
    except KeyboardInterrupt:
      break
