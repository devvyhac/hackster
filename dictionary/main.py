import difflib, json, time, os
from tools.printer import print_msg, clear_console, get_input, print_tool_name

class Dictionary:
    def __init__(self, file = None):
        self.active = True
        self.base_folder = "./dictionary"
        self.filename = file if file is not None else f"{self.base_folder}/dictionary.json"
        self.wordlist = self.read_file()
    
    def read_file(self):       
        with open(self.filename, "r") as file:
            return json.loads(file.read())
        
    def save_search(self, word):
        search_file_path = f"{self.base_folder}/previous_searches.txt"
        # if not os.path.exists(search_file_path):

        with open(search_file_path, "a+") as searches:
            searches.seek(0)
            previous = searches.read()
            if word not in previous:
                searches.write(word + "\n")
        
    def get_word(self):
        word = get_input("\nEnter word(s) separated by ',': ")
        print("")
        assert len(word) >= 2, "Kindly enter a valid English word"
        return word
            
    def translate(self):
        print_tool_name("Dictionary", "Devvyhac", "Team Trace Techie", "https://github.com/devvyhac/hackster/dictionary")
        print_msg("info", """  
                   This is a simple dictionary app.
                   Here, you can enter the word and hit 'Enter' to display the meaning.
                
                   TIP: Just enter the word you would like to know the meaning of.
                
                   ENJOY 😊. \n""", art=False)
        while True:
            try:
                # clear_console()
                words = self.get_word().replace(" ", "").split(",")

                for word in words:
                    if word in self.wordlist.keys():
                        self.save_search(word)
                        meaning = self.wordlist[word]
                        print_msg("info", word.upper())
                        print_msg("success", meaning)

                    else: 
                        match = difflib.get_close_matches(word, self.wordlist.keys())

                        for item in match:
                            y_or_no = get_input(f'Do you mean "{item}"? Enter Y(yes) or n(no) to continue: ').lower()

                            if y_or_no == "yes" or y_or_no == "y" or y_or_no == "":
                                self.save_search(item)
                                meaning = self.wordlist[item]
                                if meaning:
                                    print_msg("info", item.upper())
                                    print_msg("success", meaning)
                                    
                                    break


                            elif y_or_no == "no" or y_or_no == "n":
                                print_msg("info", "Word doesn't exist.")
                                continue

                            else: 
                                print_msg("error", "Wrong command! proceeding anyways. ")
                                break


            except KeyboardInterrupt:
                break

            except Exception as e:
                print("error", e)
        
if __name__ == "__main__":
    dic = Dictionary()
    dic.translate()
