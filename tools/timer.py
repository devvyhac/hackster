from time import time, sleep
from .printer import print_msg

class Timer:
  def __init__(self):
    self.saved_time = []
    
  def start_timer(self, start=False):
    timestamp = time()
    self.saved_time.append(timestamp)
    
    if start:
      print_msg("success", "Timer Started. ")
      
  def check(self, timestamp, index, text = "Time Taken"):    
    if int(timestamp) >= 60:
      print_msg("success", "{}: •[ {:.2f} ]• minutes".format(text, (time() - self.saved_time[index])/60))
    
    elif int(timestamp) >= 1 and int(timestamp) < 60:
      print_msg("success", "{}: •[ {:.2f} ]• seconds".format(text, time() - self.saved_time[index]))
    
    else:
      print_msg("success", "{}: •[ {:.4f} ]• milliseconds".format(text, time() - self.saved_time[index]))

  def get_timestamp(self, total=False):
    now = time()
    timestamp = now - self.saved_time[-1]
    
    self.check(timestamp, -1)
    self.saved_time.append(time())
    
    if total:
      timestamp = now - self.saved_time[0]
      self.check(timestamp, 0, text="Total Time Taken")



