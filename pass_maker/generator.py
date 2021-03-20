import random, string
from colorama import Fore

from methods.printer import get_input, print_msg

pass_chars = string.ascii_letters + string.digits + string.punctuation

def get_pass_length():
  pass_len = 0
  while True:
    try:
      pass_len = get_input("Enter number of characters, default[8]: ")
      
      if pass_len == "":
        pass_len = 8
        print_msg("info", "Using Default Value {}".format(pass_len))
        break
      
      pass_len = int(pass_len)
      if pass_len < 8:
        print_msg("error", "Error! Value must be greater than [7]")
        continue
        
      break
      
    except KeyboardInterrupt:
      break
      
    except (TypeError, ValueError):
      
      print_msg("error", "Please enter value in digits!")
      continue
      
  return pass_len


def yield_password(pass_length):
  password = (random.choice(pass_chars) for p in range(pass_length))
  password = "".join(password)    
  return password


# print(yield_password())