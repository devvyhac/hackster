import progressbar
import time

class Progress:
  def __init__(self):
    self.bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)

#bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)

#bar.start()
#for i in range(100):
#    bar.update(i+1)
#    sleep(0.1)
#bar.finish()

