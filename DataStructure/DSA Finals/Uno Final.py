import random
import os
import time

class Player:
    def __init__ (self, name):
        self.name = name
        self.next = None
        self.prev = None
        self.num_players = len(name) 
        self.hand =[]

class Cards:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        colors = ['Red', 'Green', 'Blue', 'Yellow']
        for color in colors:
            for number in range(10):
                self.cards.append(f"{color} {number}")
            self.cards.append(f"{color} Skip")
            self.cards.append(f"{color} Reverse")

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            return None
        
    def __str__(self):
        return ', '.join(self.cards)
#------------------------------------------------------------------------
class UNOGame:
    def __init__ (self):
        self.head = None
        self.current_player = None
        self.direction = 1 
        self.bad_word_count = 0  
        self.skip_next = False
        time.sleep (5)
        self.playing = False
        self.cards = Cards()
        self.cards.shuffle()
        self.deck = {
            "Red":    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            "Yellow": [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            "Blue":   [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            "Green":  [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
            "Wildcards": [1, 2]
        }
#--------------------------------------------------------------------------------------------------------
    #Profanity Filter
    def add_player (self, name): 
        bad_words = {
            "fuck", "shit", "bitch", "bastard", "dick", "pussy", "crap", "slut",
            "whore", "cock", "damn", "hell", "tits", "cum", "bollocks", "wanker",
            "prick", "bugger", "arse", "twat", "asshole", "dingus", "douchebag",
            "idiot", "moron", "loser", "jerk", "knobhead", "tosser", "pillock", "wops", "greasers"
        }

        banned_words = {"nigger", "nigga", "fag", "faggot", "cunt", "nazi", "kike", "cumlord"} 
        #banned words, it will end the program if used.
        
        lowered = name.lower ()
        for word in banned_words:
            if word in lowered:
                print ("This program does not tolerate Racism.")
                time.sleep (1)
                print (" ")
                print ("Exiting the Game...")
                time.sleep (1)
                exit ()

        for word in bad_words:
            if word in lowered:
                print ("Please type an appropriate name, Try again.")
                self.bad_word_count += 1
                if self.bad_word_count >= 3:
                    print ("Too many Bad Words entered, Please Try Again.")
                    time.sleep (0.5)
                    exit ()
                return False
        
        new_player = Player (name)
        if self.head is None:
            self.head = new_player
            new_player.next = new_player
            new_player.prev = new_player
            self.current_player = new_player
        else:
            tail = self.head
            while tail.next != self.head:
                tail = tail.next
            tail.next = new_player
            new_player.prev = tail
            self.head.prev = new_player
            new_player.next = self.head
        print (f"'{name}' has been added!")
        return True

    def start_game(self):
        if not self.head or self.head.next == self.head:
            print("Need at least 2 players to start.")
            return

        self.playing = True
        self.top_card = self.cards.draw_card()
        input("Press Enter to start the game...")
        print(f"Starting the game!")
        time.sleep(1)

        temp = self.head
        while True:
            temp.hand = [self.cards.draw_card() for _ in range(7)]  # the number here is how many cards the players will get.
            temp = temp.next
            if temp == self.head:
                break

        while self.playing:
            os.system('cls')
            print(f"\nIt's {self.current_player.name}'s turn.")
            print(f"Your Hand: {self.current_player.hand}")
            print(f"Current Card: {self.top_card}")

            choice = input("Pick a card or draw a card from the pile? (P/D): ").strip().upper()
            if choice == 'D':
                new_card = self.cards.draw_card()
                if new_card:
                    self.current_player.hand.append(new_card)
                    print(f"You drew: {new_card}")
                    print(" ")
                    time.sleep(1)
                else:
                    print("Deck is empty.")
                self.rotate_turn()
            elif choice == 'P':
                try:
                    index = int(input("Enter the card number to play: "))
                    if 0 <= index < len(self.current_player.hand):
                        chosen_card = self.current_player.hand[index]
                        if self.can_play_card(chosen_card):
                            self.top_card = chosen_card
                            self.current_player.hand.pop(index)
                            print(f"\n{self.current_player.name} played {chosen_card}!")
                            time.sleep(1.5)
                            if len(self.current_player.hand) == 0:
                                print(f"{self.current_player.name} wins! 🎉")
                                time.sleep(2)
                                print()
                                print("\nGame Over!")
                                input("Press Enter to exit.")
                                self.playing = False
                                return
                            if "Skip" in chosen_card:  
                                self.skip()
                                self.rotate_turn()
                            elif "Reverse" in chosen_card:
                                self.reverse()
                            else:
                                self.rotate_turn() 
                        else:
                            print("You can't play that card. Must match color or number.")
                        time.sleep(2)
                    else:
                        print("Invalid card number, try again.")
                        time.sleep(2)
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    time.sleep(2)

    def display_players (self): #display logic
        if self.head is None:
            print ("There are no players in the game right now.")
            return
        temp = self.head
        while True:
            print(f"[{temp.name}]", end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print ("[end of list.]")
        time.sleep (2.5)

    def remove_player (self, name): #remove player logic
        if not self.head:
            print ("No players to remove.")
            return
        temp = self.head
        while True:
            if temp.name == name:
                if temp.next == temp:
                    self.head = None
                    self.current_player = None
                else:
                    temp.prev.next = temp.next
                    if temp == self.head:
                        self.head = temp.next
                    if temp == self.current_player:
                        self.current_player = temp.next
                print (f"Player '{name}' was removed.")
                return
            temp = temp.next
            if temp == self.head:
                break
        print (f"I don't see a player named '{name}' in my system.")
        time.sleep(2)

    def rotate_turn(self):
        if not hasattr(self, 'skip_next'):
            self.skip_next = False
            
        if getattr(self, 'skip_next', False):
            if self.direction == 1:
                print(f"{self.current_player.next.name} has been skipped!")
                self.current_player = self.current_player.next.next
            else:
                print(f"{self.current_player.prev.name} has been skipped!")
                self.current_player = self.current_player.prev.prev
            self.skip_next = False
        else:
            # Normal turn rotation
            if self.direction == 1:
                self.current_player = self.current_player.next
            else:
                self.current_player = self.current_player.prev

        print(f"It's now {self.current_player.name}'s turn.")
        time.sleep(2)

    def skip(self):
        self.skip_next = True
        time.sleep(2)

    def reverse(self): #working
        self.direction *= -1
        self.rotate_turn()
        time.sleep(1)
        
    def can_play_card(self, card):
        if not self.top_card:
            return True
        top_color, top_value = self.top_card.split()
        card_color, card_value = card.split()
        return (card_color == top_color or card_value == top_value or "Wild" in card)

# Main loop start
UNOgame = UNOGame()
def show_menu():
    os.system('cls')
    print ("Welcome to UNO Game!, Developed by Julia Abigail Bautista, Josh Francis Yatco, and RJ Romero")
    print("\nThere are ({count} in the game)\n".format(count=get_player_count(UNOgame)))

    print("\n".join([
    "[0] To add a Player",
    "[1] To display Players",
    "[2] To remove a Player",
    "[3] Start the Game",
    "[4] To exit\n"
]))

def get_player_count(game):
    if not game.head:
        return 0
    count = 1
    temp = game.head.next
    while temp != game.head:
        count += 1
        temp = temp.next
    return count

def add_players_loop():
    while True:
        os.system('cls')
        name = input("Enter player name here: ").strip().replace(" ", "")
        if not name:
            print("Name can't be empty. Try again.")
            continue
#------------------------------------------------------------------------------------------------------
        if name.strip().lower() == "yatz":
            print("Hello! Mr. Developer.")
            time.sleep(2)
            continue
        if name.strip().lower() == "parel":
            print("Daddy Parel, the Partner-Developer of this game.")
            time.sleep(2)
            continue        
        if name.strip().lower() == "abigail":
            print("Julia Abigail Bautista, the Co-Developer of this game.")
            time.sleep(2)
            continue
        if name.strip().lower() == "rj":
            print("Rj Romero, the Co-Developer of this game.")
            time.sleep(2)
            exit()
#------------------------------------------------------------------------------------------------------
        if len(name) > 20:
            print("Player name too long. Try Again.")
            continue
        if not UNOgame.add_player(name):
            continue
        more = input("Add more players? (y/n): ").lower()
        if more != 'y':
            break

def remove_player():
    os.system('cls')
    name = input("Enter the name you want to remove: ").strip()
    UNOgame.remove_player(name)
    print ("successfully removed!")
    time.sleep(1.5)

def main_loop():
    while True:
        show_menu()
        choice = input("Enter Here > ").strip()

        if choice == '0':
            add_players_loop()

        elif choice == '1':
            os.system('cls')
            UNOgame.display_players()

        elif choice == '2':
            os.system('cls')
            remove_player()

        elif choice == '3':
            os.system('cls')
            UNOgame.start_game()
            input ("Press enter to play Uno!\n")
            
        elif choice == '4': 
            os.system('cls')
            print("Thank you for playing!")
            time.sleep(0.5)
            print("\nExiting the game...")
            time.sleep(0.5)
            break
        else:
            print("Wrong input. Try again.")
            time.sleep(1)
        os.system('cls')

main_loop()

#developed by Julia Abigail Bautista, Josh Francis Yatco, and RJ Romero
