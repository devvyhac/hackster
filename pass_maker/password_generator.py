import os, sys, time, random

from tools.printer import get_input, print_msg, file_handle_success, print_tool_name, clear_console

from tools.confirm import confirm_exit
from .generator import yield_password, get_pass_length

from tools.loader import Loader
from tools.timer import Timer
from tools.progress import Progress


pass_list = []
timer = Timer()

class PassGenerator:
  def __init__(self):
    pass
    
  def initialize_props(self):       
    while True:
      try:
        values = self.get_values()
        self.amount = values['amount']
        self.set_filename(values['filename'])
        
        break
        
      except KeyboardInterrupt:
        break
        
      except:
        print_msg("error", "Please enter correct values")
        #print("")
        continue
        
    self.length = get_pass_length()
  
  def get_values(self):
    amount = int(get_input("Amount of passwords, default <100>: "))
    filename = get_input("Filename, with or without (.txt): ").split(".")[0] + ".txt"
    filename = "password_lists/{}".format(filename)
    return {
      'amount': amount,
      'filename': filename
    }
  
  def set_filename(self, filename):
    if os.path.exists(filename):
      os.remove(filename)
      
    self.filename = filename #"{}.txt".format(url)


  def save_to_file(self, password):
    with open(self.filename, "a+") as passfile:
      passfile.write(password + "\n")


  def run_tasks(self):
    global pass_list
    
    loader = Loader(
      load_text="Generating Passwords.", 
      load_type="success", 
      feedback="Passwords Generation Successful!")
    
    try:
      p = Progress()
      timer.start_timer()
      loader.load()
      
      for i in range(self.amount):
        
        #time.sleep(.01)
        pass_key = yield_password(self.length)
        loader.set_progress(pass_key)
        
        pass_list.append(pass_key)
        
    except KeyboardInterrupt:
      sys.exit()
      
    finally:
      loader.terminate(timeout=1)
      # timer.get_timestamp()
      
      print_msg("success", "Please wait! Saving words to file...")
      
      for index, key in enumerate(pass_list, 1):
        self.save_to_file(key)
        p.bar.update(index)
      
      p.bar.finish()
      print_msg("success", "\n{} Passwords Generated.".format(len(pass_list)))
      del pass_list
      file_handle_success(self.filename)
      timer.get_timestamp()


def generate_password():
  pass_generator = PassGenerator()

  while True:
    try:
      print_tool_name("Lazy Auth", "Devvyhac", "Team Trace Techie", "github.com/devvyhac")

      pass_generator.initialize_props()
      pass_generator.run_tasks()

    except KeyboardInterrupt:
      break
      
    finally:
      
      if not confirm_exit("Do you want to continue? [Y/n]: "):
        break
        
      continue
      # print_msg("info", "Restarting program in 5 seconds.")
      # print_msg("info", "Press Ctrl + c to quit")

      # time.sleep(5)
      clear_console()







