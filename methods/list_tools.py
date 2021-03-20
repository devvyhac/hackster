import os
from colorama import Fore, init



console_width = os.get_terminal_size().columns
init(autoreset=True)

def list_commands(commands):
  print("""{1}{0}
{2}SN          COMMAND NAME{1}
{0}
  """.format(console_width*"•", Fore.CYAN, Fore.LIGHTGREEN_EX))

  for index, command in enumerate(commands, 90):
    print("{2}[•{5}{0}{2}•]:     {3}{1}{4}"\
      .format(index, command, 
        Fore.GREEN, 
        Fore.YELLOW , 
        Fore.RESET, 
        Fore.LIGHTRED_EX
      ))
    

def list_tools(tools):
  print("\n{0}[✓]{1} Available tools {0}[✓]{2}\n"\
    .format(Fore.GREEN, Fore.LIGHTYELLOW_EX, Fore.RESET))
  

  print("""{1}{0}
{2}SN          TOOL NAME{1}
{0}
  """.format(console_width*"•", Fore.CYAN, Fore.LIGHTGREEN_EX))
  
  for index, tool in enumerate(tools, 1):
    print("{2}[•{5}{0}{2}•]:      {3}{1}{4}"\
      .format(index, tool, 
        Fore.GREEN, 
        Fore.YELLOW , 
        Fore.RESET, 
        Fore.LIGHTYELLOW_EX
      ))
   
  print("")
  print("\nℹ️   {1}INFO: {0} Select Items Using the Assigned Number  ℹ️    "\
  .format(Fore.LIGHTMAGENTA_EX, Fore.LIGHTYELLOW_EX))
 
  
      

def list_items(tools, cmd):
  list_tools(tools)
  list_commands(cmd)  
  print("\nℹ️   {1}INFO: {0} Select Items Using the Assigned Number  ℹ️    "\
  .format(Fore.LIGHTMAGENTA_EX, Fore.LIGHTYELLOW_EX))
  