import sys, os
from colorama import Fore as c, init
from .fancy import fancy_text, fancy_typo

console_width = os.get_terminal_size().columns

init(autoreset=True)

def clear_console():
  if os.name == "nt":
      os.system("cls")
  else:
    os.system("clear")


def print_tool_name(text, creator, teamname, github):
  print("""{0}{3}
{1}  v1.3
{4}{2}{0}
[{6}°•.{1}✓{0}] {7}Created by {5}{0} [{6}.•°{1}>_{0}]
[{6}°•.{1}✓{0}] {7}{8}{0} [{6}.•°{1}>_{0}]
[{6}°•.{1}✓{0}] {7}GitHub >_ •[ {9} ]• {0} [{6}.•°{1}>_{0}]
{3}
{2}
""".format(
    c.CYAN, 
    c.GREEN, 
    c.RESET, 
    int(console_width) * "=",
    format(fancy_text(text).center(console_width)),
    format(fancy_typo(creator, font="love2")),
    c.LIGHTMAGENTA_EX,
    c.LIGHTCYAN_EX,
    format(fancy_typo(teamname, font="fancy21")),
    format(fancy_typo(github, font="fancy12")),
  ))
  

def file_handle_success(file, msg=""):
  print("\n{5}{1}{3}Result has been saved to {4}<• {2} •> {0}[°•.✓]{5}"\
    .format(
      c.LIGHTGREEN_EX, 
      c.LIGHTYELLOW_EX, 
      str(file), str(msg), 
      c.LIGHTCYAN_EX, c.RESET
    ), end="\n")
  

def get_input(msg):
  return input("{4}{0}{1}{2}[{3}.•°{2}]{4}>_ "\
    .format(
      c.LIGHTYELLOW_EX, 
      str(msg).title(), c.LIGHTMAGENTA_EX, 
      c.LIGHTGREEN_EX, c.LIGHTCYAN_EX, 
      c.RESET
    )) 

def print_msg(msg_type, msg, clear=False, art=True):
  if clear:
    clear_console()
  
  if msg_type == "warning":
    if art:
      print("\n{4}{0}{1} {2}.•° {3}[{0} ! ️{3}]{4}\n"\
      .format(
        c.LIGHTYELLOW_EX, 
        str(msg), c.LIGHTCYAN_EX,
        c.LIGHTMAGENTA_EX, 
        c.RESET, art))
    
    else:
      print("{2}{0}{1} \n"\
      .format(
        c.LIGHTYELLOW_EX, 
        str(msg),
        c.RESET))
  
  elif msg_type == "success":
    if art: 
      print("\n{4}{0}{1} {2}.•° {3}[{0} ✓ ️{3}]{4}"\
      .format(
        c.LIGHTGREEN_EX, 
        str(msg), c.LIGHTYELLOW_EX,
        c.LIGHTBLUE_EX,
        c.RESET, art))
    else:
      print("\n{2}{0}{1} \n"\
      .format(
        c.LIGHTGREEN_EX, 
        str(msg),
        c.RESET))
  
  elif msg_type == "info":
    if art:
      print("\n{4}{0}{1} {2}.•° {3}[{0} ∆ ️{3}]{4}"\
      .format(
        c.LIGHTCYAN_EX,
        str(msg), c.LIGHTGREEN_EX,
        c.LIGHTBLACK_EX,
        c.RESET, art))
    else:
      print("\n{2}{0}{1} "\
      .format(
        c.LIGHTCYAN_EX,
        str(msg),
        c.RESET))
    
  elif msg_type == "error":
    if art:
      print("\n{4}{0}{1} {2}.•° {3}[{0} ! ️{3}]{4}\n"\
      .format(
        c.LIGHTRED_EX,
        str(msg), c.LIGHTCYAN_EX,
        c.LIGHTMAGENTA_EX,
        c.RESET, art))
    else:
      print("\n{2}{0}{1} \n"\
      .format(
        c.LIGHTRED_EX,
        str(msg),
        c.RESET))
      
  else:
    print(str(msg))





