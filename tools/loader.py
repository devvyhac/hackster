import itertools
import threading
import time
import sys, os
from colorama import init, Fore

init(autoreset=True)

#here is the animation
class Loader():
  def __init__(self, load_type = "success", load_text = "Loading", feedback=None, progress=None):
    self.load_type = load_type
    self.load_text = load_text
    self.feedback = feedback
    self.progress = progress
    self.done = False
    self.is_loading = True
    self.event = threading.Event()
    
  def set_opt(self, load_type = "success", load_text = "Loading", feedback=None):
    self.load_type = load_type
    self.load_text = load_text
    self.feedback = feedback
    self.load()
    
  def terminate(self, timeout=0, seize=1):
    time.sleep(timeout)
    self.is_loading = False
    self.display_feedback(seize)
    
  
  def display_feedback(self, seize):
    if self.load_type == "success":
      feedback = self.feedback if self.feedback else "Success"
      sys.stdout.write('\r\n{}{} ✔️    \n'.format(Fore.LIGHTGREEN_EX, feedback))
    
    elif self.load_type == "error":
      feedback = self.feedback if self.feedback else "Error"
      sys.stdout.write('\r\n{}{} ❌    \n'.format(Fore.LIGHTRED_EX, feedback))
   
    elif self.load_type == "info":
      feedback = self.feedback if self.feedback else "Info"
      sys.stdout.write('\r\n{}{} ℹ️  \n'.format(Fore.LIGHTBLUE_EX, feedback))
      
    elif self.load_type == "warning":
      feedback = self.feedback if self.feedback else "Warning"
      sys.stdout.write('\r\n{}{} ⚠️  \n'.format(Fore.LIGHTYELLOW_EX, feedback))
      
    time.sleep(seize)
  
    
  def close_event(self, seize = .5):
    self.event.set()
    while self.is_loading:
      continue
      
    self.event.clear()
      
  def load(self, delay=1.5, seize = .5):
 
    t = threading.Thread(target=self.handle_load, args = (), daemon = True)
    t.start() 
    
    t2 = threading.Thread(target=self.close_event, args = (), daemon = True)
    t2.start() 
  
  def set_progress(self, text):
    self.progress = text
    
  def handle_load(self):
    self.event.wait()
    print("")
    for c in itertools.cycle(['°', '•', '.', '.', '•', '°']):
      if not self.event.is_set():
        break
        
      sys.stdout.write(('\r{}{} {}' + c+c+c).format(Fore.LIGHTYELLOW_EX, self.load_text, Fore.LIGHTGREEN_EX))
      
      if self.progress:
        sys.stdout.write("     {}".format(str(self.progress)))
      
      sys.stdout.flush()
      time.sleep(0.1)
 

