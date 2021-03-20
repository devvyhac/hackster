from .loader import Loader
from .printer import clear_console

def confirm_exit(question, no_reload = False):
  confirm = str(input(question))
  if confirm == "y" or confirm == "Y" or confirm == "":
    if no_reload:
      pass
      
    else:
      quiting = Loader(load_type="info", load_text="Quiting Program", feedback="Program Terminated")
      quiting.load()
      quiting.terminate(timeout=1.2)
      print("")
        
    return True
      
  elif confirm == "n" or confirm == "N":
    if no_reload:
      pass
    
    else:
      restart = Loader(load_type="success", load_text="Restarting Program", feedback="Program Restarted")
      restart.load()
      restart.terminate(timeout=1.2)
      print("")
      clear_console()
        
    return False