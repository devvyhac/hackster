import requests, json, sys
from tools.printer import print_msg, print_tool_name, get_input, clear_console

# api_key=31120a6edf-52f0320c4e-qqu4cg


all_codes = dict()

def get_amount():
    while True:
        try:
            return float(get_input("Enter Amount: "))
            
        except KeyboardInterrupt:
            print_msg("warning", "\nProgram Terminated!\n")
            exit()

        except Exception as e:
            print_msg("error", e)
            continue

def get_all_codes(display=False):
    try:
        r_data = requests\
            .get("https://api.fastforex.io/currencies?api_key=31120a6edf-52f0320c4e-qqu4cg")

        return json.loads(r_data.content)['currencies']

    except requests.exceptions.ConnectionError:
        print_msg("error", "\nUnable to Connect to Host! Please check your internet connection\n")
        exit()

def get_curr(payloads):
    try:
        response = requests\
            .get("https://api.fastforex.io/fetch-one", params=payloads)

        r_data = json.loads(response.content)

        if "error" in r_data:
            raise Exception(r_data['error'])

        return r_data

    except requests.exceptions.ConnectionError as e:
        print_msg("error", e)
        return False

    except Exception as e:
        print_msg("error", e)

def get_code(text):
    all_codes = get_all_codes()
    while True:
        try:
            code = get_input(text).upper()
            if code in all_codes:
                return code
            else:
                raise Exception("The Currency code --> {} does not exist"\
                    .format(code))

        except KeyboardInterrupt:
            print_msg("warning", "\nProgram Terminated!\n")
            exit()

        except Exception as e:
            print_msg("error", e)
            continue


def convert():
    curr_from = get_code("Convert From: ")
    curr_to = get_code("Convert To: ")
    amount = get_amount()

    payloads = {
        "from":curr_from, 
        "to": curr_to, 
        "api_key":"31120a6edf-52f0320c4e-qqu4cg"
    }

    data = get_curr(payloads)
    if data != None:
        total = data['result'][curr_to] * amount
        print_msg("success", "\n{}-{} ==> {}-{:.2f} ".format(
            curr_from, amount, curr_to, total
        ))

def converter():
    print_tool_name("Aboki $$", "Devvyhac", "Team Trace Techie", "github.com/devvyhac")
    convert()

