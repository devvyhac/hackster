import json, time, sqlite3, string, random
from random import randint
from tools.printer import get_input, print_tool_name, print_msg, clear_console
from tools.loader import Loader
from tools.confirm import confirm_exit as confirm

class Guess:
    def __init__(self):
        self.active = True
        self.min = 0
        self.max = 10
        self.set_correct(self.min, self.max)
        self.chances = 5
        self.attempts = self.chances
        self.attempts_list = []
        self.level = 1
        self.score = 0
        self.highscorer = []
        self.set_highscorer()

        self.current_player = None
        self.chance_regulator = 4

    # creating the number that the user must guess to proceed to the next level.
    def set_correct(self, min, max):
        self.correct = randint(min, max)

    def db(self):
        conn = sqlite3.connect("C:\\Users\\Devvyhac\\Documents\\python\\hackster\\number_guessing_game\\players.db")
        cursor = conn.cursor()

        # conn.execute('''CREATE TABLE Highscore
        #      (ID INTEGER PRIMARY KEY AUTOINCREMENT   NOT NULL,
        #      pid            TEXT    NOT NULL,
        #      name           TEXT    NOT NULL,
        #      level          INT     NOT NULL,
        #      score          INT     NOT NULL);''')

        return {
            "conn": conn,
            "cursor": cursor
        }
    

    def set_player_name(self):

    # creating a loop that runs regardless of the error from user input with a warning message each time.
        while True:

      # Exception handling below here.
            try:
                self.player_name = get_input("Enter Username")
                if len(self.player_name) < 3:
                    raise Exception("Please make your Username at least 3 characters")
                break

            except Exception as e:
                print_msg("error", e)
                continue

    # retrieving the highscore of the player with the highest score to be displayed
    def set_highscorer(self, **kwargs):

        # Exception handling block where database query is being made to read or write data from the database
        try:
            db = self.db()
            
            # querying the database to get the highest score
            query = "SELECT * FROM Players WHERE (score = ( SELECT MAX(score) AS 'Highscore' FROM Players as highscore ))"
            db["cursor"].execute(query)
            self.highscorer = list(db["cursor"].fetchone())


            # db["cursor"].execute("SELECT * FROM Players where id=1")
            # self.highscorer = list(db["cursor"].fetchone())
      
            # comparing the score of the current player to the highest score in the database to update the highest score if necessary
            if self.score >= self.highscorer[-1]:
                self.highscorer[-1] = self.score
                self.highscorer[1] = self.current_player["pid"]
                self.highscorer[2] = self.current_player["name"]
                self.highscorer[3] = self.current_player["level"]
      
        except sqlite3.Error as e:
            print_msg("error", f"SQLite Error: {e}")

        except Exception as e:
            print_msg("error", f"Core Error: {e}")

        finally: db["conn"].close()

    def set_play_data(self):
        try:
            db = self.db()

            if self.score > self.current_player["score"]:
                db["cursor"].execute("UPDATE Players SET level={}, score={} where pid='{}' and name='{}'"\
                .format(self.level, self.score, self.current_player["pid"], self.current_player["name"]))
        
                db["conn"].commit()
      
        except sqlite3.Error as e:
            print_msg("error", f"SQLite Error: {e}")

        finally: db["conn"].close()

    def set_player_data(self):
        try:
            db = self.db()

            # generating a unique id for each player
            characters = string.ascii_letters + string.digits
            new_player_id = ""
            for i in range(10):
                new_player_id += random.choice(characters)
      
            db["cursor"].execute("SELECT * FROM Players where name='{}'".format(self.player_name))
            player = db["cursor"].fetchone()

            # checking if a player is a returning player or a new player
            # if the player already exists, append "old" to the player's data
            if player:
                self.current_player = {
                    "pid": player[1],
                    "name": player[2],
                    "level": player[3],
                    "score": player[4],
                    "exists": True
                }
      
            # else if the player is new, create a new entry for him/her in the data base
            else:
                sql = "INSERT INTO Players(pid, name, level, score) VALUES('{0}', '{1}', {2}, {3})"\
                .format(str(new_player_id), 
                self.player_name,
                self.level, self.score)
        
                # execute the command to create new entry in the database for the new user.
                db["cursor"].execute(sql)
                
                db["cursor"].execute("SELECT * FROM Players where pid='{}' and name='{}'"\
                .format(str(new_player_id), self.player_name))
                
                player = list(db["cursor"].fetchone())

                self.current_player = {
                    "pid": player[1],
                    "name": player[2],
                    "level": player[3],
                    "score": player[4],
                    "exists": False
                }
                
                db["conn"].commit()
        
        
        except sqlite3.Error as e:
            print_msg("error", f"SQLite Error: {e}")

        finally: db["conn"].close()

    # this method gets the user input for the total number of chances they have before its game over.
    def get_guess(self):
        while True:
            try:
                # getting each trial from the player
                print_msg("info", "Guess the Number between [ {} ] and [ {} ] || Chances left: [• {} •] || Previous Attempts: [• {} •]"\
                .format(self.min, self.max, self.attempts, self.attempts_list), art=True)
                
                self.trial = int(get_input("Enter your Guess"))
                self.attempts_list.append(self.trial)
                break
            except ValueError:
                print_msg("error", "Only Numbers are allowed, try again")
                continue

    # increasing the number of chances for a player if they successfully guessed the number.
    def increase_chances(self, addition):
        self.chances += addition
        self.attempts = self.chances

    # take the player to the next stage and increase of the number of guess range to improve difficulty.
    def proceed(self):
        self.level += 1
        self.max += 5

    # ensuring that number of chances can only be increased after certain amount of stages.
        if self.level % 10 == 0:
            self.chance_regulator += 1

        if self.level % self.chance_regulator == 0:
            self.increase_chances(2)

        else:
            self.attempts = self.chances

        self.set_correct(self.min, self.max)
        self.score += 10

        self.set_play_data()
        self.set_highscorer()
        self.attempts_list = []

        # clears the console and display a beautiful message on the console
        loader = Loader(load_text="Loading Stage •[{}]•".format(self.level), load_type="success")
        loader.load()
        loader.terminate(timeout=.4, seize=1.1)

        clear_console()

        # print the current info for page, player and score.
        print_msg("info", "Highscore •[{}]• By •[{}]•"\
        .format(self.highscorer[-1], self.highscorer[2], art=True))

        print_msg("info", f"Player: •[{self.current_player['name']}]• <•> Stage: [• {self.level} •], Score: [• {self.score} •]", art=False)


    def compare_guess(self):
        # checks if the guess is correct and proceed to the next level
        if self.trial == self.correct:
            print_msg("success", "You guessed right! going to next level")
            time.sleep(1)
            self.proceed()

        # checks if the guessed number is greater that the correct number and hint the player, then reduce attempts   
        elif self.trial > self.correct:
            self.attempts -= 1
            print_msg("info", "Your guess is greater than the correct number")
            # print_msg("warning", f"You have •[{self.attempts}]• Attempts left, try again")
          
        # checks if the lesser number is greater that the correct number and hint the player, then reduce attempts
        elif self.trial < self.correct:
            self.attempts -= 1
            print_msg("info", "Your guess is less than the correct number")
            # print_msg("warning", f"You have •[{self.attempts}]• Attempts left, try again")

    # the method that serves as the entry point to the whole game.
    def guess_it(self, show_tips=True, restart = False):
        if show_tips:
            print_tool_name("Guess Py", "Devvyhac", "Team Trace Techie", "github.com/devvyhac")
            print_msg("info", """  This is a number guessing game, 
                where you need to guess the correct number 
                to proceed to the next level.
                
                TIP: There will be an hint 
                that tells you whether your guess is 
                greater than or less than the correct number.
                
                ENJOY 😊. \n""", art=False)

        if not restart:
            self.set_player_name()

        self.set_player_data()


        # checks whether the player is a new player or an old player and display the appropriate info.
        if self.current_player["exists"]:
            print_msg("success", "Welcome back, {}".format(self.current_player["name"]))
        else:
            print_msg("success", "New Player! {}".format(self.current_player["name"]))
        
        print_msg("info", "Highscore •[{}]• By {}"\
        .format(self.highscorer[-1], self.highscorer[2], art=True))
        
        print_msg("info", f"Your previous Score: [• {self.current_player['score']} •] in Level: [• {self.current_player['level']} •]", art=False)

        print_msg("info", f"Current Player: {self.player_name} <•> Stage: [• {self.level} •], Score: [• {self.score} •]", art=False)
        
        # print_msg("info", "Guess the Number between {} and {} // Chances left: [• {} •] // Previous Attempts: [• {} •]"\
        # .format(self.min, self.max, self.chances, self.attempts_list), art=True)

        self.get_guess()
    
        # the main game loop
        while self.active != False:
            try:
                self.compare_guess()
                self.get_guess()
            
                if self.attempts <= 1:
                    clear_console()
                    print_msg("error", "GAME OVER!!!")
                    time.sleep(3)

                    if confirm("Do you wish to restart? (Y/n): ", no_reload = True):
                        
                        loader = Loader(load_text="Restarting game...", load_type="success")
                        loader.load()
                        loader.terminate(timeout=.4, seize=1.1)

                        clear_console()

                        self.__init__()
                        self.guess_it(restart = True)
                    

                    self.active = False
                    exit()
                    break
            
            except KeyboardInterrupt:
                print("Quiting game")
                time.sleep(1)
                self.active = False
                exit()
                break



if __name__ == "__main__":
    player = Guess()
    player.guess_it()
    # cursor.execute("DROP TABLE Players")
    


    