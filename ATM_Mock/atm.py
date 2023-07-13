import os, time, sqlite3
from datetime import datetime
from tools.list_tools import list_tools
from tools.printer import print_tool_name, print_msg, get_input

# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:m:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# THIS IS THE LIST/REGISTER/FORM THAT HAS 3 ITEMS IN IT
bank_accounts = [
    {   # LIST ITEM 1
        "id": 1,
        "name": "toonie",
        "passkey": 3453,
        "balance": 0
    },
    {   # LIST ITEM 2
        "id": 2,
        "name": "xyluz",
        "passkey": 8375,
        "balance": 0
    },
    {   # LIST ITEM 3
        "id": 3,
        "name": "parrot",
        "passkey": 9085,
        "balance": 0
    }
] # THE LIST ENDS HERE


# THIS CODE BELOW WILL CLEAR THE SCREEN/TERMINAL/CONSOLE
def clear_console():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system("clear")
    
    time.sleep(.5)

current_account = []




# THIS IS THE MECHANISM THAT ENSURES A SUCCESSFUL DEPOSITING
def deposit(customer_name, amount):
    for account in bank_accounts:
        if customer_name == account['name']:
            account['balance'] += amount
            clear_console()
            print_msg("success", "\nN-{} has been succesfully deposited to your account".format(amount))
            print_msg("info", "Your new Account balance is (N-{})".format(account['balance']), art=False)


# THIS IS THE MECHANISM THAT ALLOWS A SECURE WITHDRAWAL
def withdraw(customer_name, amount):
    for account in bank_accounts:
        if customer_name in account['name']:
            if account['balance'] >= amount:
                account['balance'] -= amount
                clear_console()
                print_msg("success", "Please take your cash")
                print_msg("info", "your new balance is: (N-{})".format(str(account['balance'])), art=False)
            else:
                clear_console()
                print_msg("error", "Insufficient Balance in your Account!")
                ask_to_proceed()


# THIS IS WHERE THE PROGRAM VERIFIES IF A USER IS REGISTERED OR NOT
name = ""
def check_name():
    global name
    try:
        name = get_input("Enter Your Account Name: \n")
    except KeyboardInterrupt:
        print_msg("warning", "\nQuiting!")
        exit()

    for account in bank_accounts:
        if name == account['name']:
            return True
        else:
            pass
    else:
        clear_console()
        print_msg("error", "\nNo Account with the name ({})".format(name))
        print_msg("info", "Please, open an account with us to continue!", art=False)

        # THIS IS WHERE A NEW CUSTOMER IS REGISTERED TO OUR BANKING SYSTEM, 
        # note: THIS WILL ADD THE NEW USER TO THE LIST OF USERS
        register = get_input("\nDo you want to proceed with opening an account with us? N/y: ")
        if register == "y" or register == "1" or register == "Y":
            try:
                # name = get_input("\nEnter Account Name: ")
                # name = name
                passkey = get_input("Enter a New Pin: ")
            except KeyboardInterrupt:
                print_msg("warning", "\nQuiting!")
                exit()

            print("")

            # CREATING A NEW USER DICTIONARY TO BE ADDED TO THE CUSTOMERS LIST
            new_user = {
                "id": len(bank_accounts) + 1,
                "name": name,
                "passkey": passkey,
                "balance": 0
            }

            # ADDING THE CUSTOMER TO THE LIST HERE
            bank_accounts.append(new_user)

        else:
            print_msg("warning", "\nQuiting program!")
            exit()

# VERIFYING THE PASSWORD IF IT IS CORRECT FOR THE ACCOUNT NAME OR NOT
passkey = 0
def check_passkey(name):
    global passkey, current_account
    while True:
        try:
            passkey = int(get_input("Enter your Pin ({}): \n".format(name)))
            for account in bank_accounts:
                if name == account['name'] and passkey == int(account['passkey']):
                    current_account = account
                    return True

            else:
                raise Exception("Wrong Pin for the Account Name ({})".format(name))

        except KeyboardInterrupt:
            print_msg("warning", "\nQuiting!")
            exit()

        except Exception as e:
            clear_console()
            print_msg("error", e)
            continue


# THIS IS THE SECTION THAT ASKS IF THE CUSTOMER WILL LIKE TO CONTINUE OR NOT
def ask_to_proceed(text=None):
    try:
        if text != None:
          retry = get_input(text + "? y/N: ")
          
        else:
          retry = get_input("\nDo You want to do something else? y/N:  ")
          

    except KeyboardInterrupt:
        print_msg("warning", "\nQuiting!")
        exit()

    if retry == "y" or retry == "1" or retry == "Y":
        check_passkey(name)
        print_options()
        ATM()

    else:
        print_msg("warning", "\nQuiting program!")
        exit()
        
def ask_to_continue(text=None, purpose="", amount=0):
    try:
        if text != None:
            get_input("\n{}? y/N: ".format(text))
        else:
            retry = get_input("\nDo You really Want to proceed to {} (N-{})? y/N:  ".format(purpose, amount))

    except KeyboardInterrupt:
        print_msg("warning", "\nQuiting!")
        exit()
        
    if retry == "y" or retry == "1" or retry == "Y":
        pass

    else:
        print_msg("warning", "Transaction has been cancelled!")
        time.sleep(2)
        print_options()
        ATM()

        
     

# THIS IS THE CODE THAT PRINTS THE AVAILABLE OPTIONS AS WELL AS WELCOMING THE USER
def print_options():
    print_msg("success", "\tWelcome, {}. Balance => ( N-{}.00 )"\
      .format(name.upper(), current_account['balance']), art=False)
    
    options = [
      "Withdrawal",
      "Cash Deposit",
      "Complaints",
      "Exit"
    ]
    
    list_tools(options, heading=False)


# THIS IS THE MAIN ATM MACHINE, IT IS THE MAIN APPLICATION
def ATM():
    clear_console()
    
    print_msg("info", "\tZuri Bank ATM", art=False)
    print_msg("info", "\tDate/Time: "+dt_string, art=True)
    print_options()

    while True:
        try:
            option = int(get_input("\nPlease Select an option: "))
            print("")
            break
        except KeyboardInterrupt:
            print_msg("warning", "\nQuiting program!")
            break
        except Exception:
            print_msg("error", "Please Enter a Valid Option!")
            continue
    
    try:
        print_msg("info", "You Selected Option {}".format(option), art=False)


        if option == 1:
            amount = int(get_input("How much do you want to withdraw? "))
            ask_to_continue(purpose="Withdraw", amount=amount)
            withdraw(name, amount)

        elif option == 2:
            amount = int(get_input("How much do you want to deposit? "))
            ask_to_continue(purpose="Deposit", amount=amount)
            deposit(name, amount)

        elif option == 3:
            complaints = get_input("What are your complaints: \n-> ")
            ask_to_continue(text="Do you want to proceed with the complaint")
            print_msg("info", "\nYour complaints have been recieved, we will get \nback to you within 10 working days", art=False)
            
        elif option == 4:
            print_msg("warning", "Quiting Program!")
            ask_to_continue()
            exit()

        else:
            print_msg("error", "Please Select a valid option!")
            

        ask_to_proceed()

    except KeyboardInterrupt:
        print_msg("warning", "\nQuiting!")
        exit()

    except UnboundLocalError:
        pass
        

def ATM_Mock():
    print_tool_name("ATM Mock", "Devvyhac", "Team Trace Techie", "github.com/devvyhac")
    
    print_msg("info", """Welcome to Zuri Bank PLC.
    
We offer the best Bank banking service 
around as we serve our customers 24/7.

We offer Online, Offline, Mobile, USSD
as well as crypto currency banking services.
""", art=False)

    check_name()
    check_passkey(name)
    ATM()


# THIS IF STATEMENT BELOW IS JUST USED TO CHECK IF THE PROGRAM IS THE MAIN THREAD, 
# DON'T WORRY ABOUT THIS IS YOU DON'T GET IT YET.
# MAKE SURE YOU READ THE PROGRAM AND UNDERSTAND IT, OKAY?


#if __name__ == "__main__":
#    ATM()
