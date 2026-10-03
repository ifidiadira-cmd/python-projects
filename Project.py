#ITSS 3311 – Object-Oriented Programming
#Final Project: Text Adventure Game
#Author: Adira Ifidi
#Date: 24th November 2025
##Description: This program simulates a text adventure game where the player makes
##choices to navigate through a story with multiple paths and endings.

def get_name():
    global name

    while True:
        name = input('Enter your name(ENTER LETTERS): ').strip()

        if name.isalpha():
            return name
        
        print("Invalid input. ENTER LETTERS")


def print_welcome(name):
    print(f"Welcome to the text CYOA game, {name}")
    print("Rules:\n - Make choices by entering the number of the options")
    print(" - Enter valid input or else you redo the choice")
    print(" - Your decision determines your fate\n GOOD LUCK")



def start_game():
    print("You wake up in a forest, dizzy. Your memories return\nSomeone hit you")
    print("You check yourself for any serious inuries.\nYou feel dried blood by your ear.")
    print("You pat yourself, you find your phone. It's dead")
    print("You seem to be in a forest. It's dark but you can see two paths")

    print("1. Take the left path")
    print("2. Take the right path")

    choice = input("Enter your choice(1 or 2): ").strip()

    while choice not in ['1', '2']:
        print("Invalid input. ENTER 1 OR 2")
        choice = input("Enter your choice(1 or 2): ").strip()

    if choice == "1":
        return "left_path"
    
    if choice == "2":
        return "right_path"



def make_choice(path):
    if path == 'left_path':
        print('You go left... The ground crunches but you hear a distant crunch. Someone is following you.')
        print('You start running but something blocks your path...')
        return "left_dead"
        
    elif path == 'right_path':
        print("You take the right path...")
        print("The ground feels solid beneath you")
        print("You arrive at a massive tree with inscriptions.\nThere's arrows poiting to either side")
        
        print("1. Go left")
        print("2. Go right")

        choice = input("Enter your choice(1 or 2): ").strip()
        while choice not in ['1', '2']:
            print("Invalid input. ENTER 1 OR 2")
            choice = input("Enter your choice(1 or 2): ").strip()

        if choice == '1':
            return "tree_left_dead"
        
        else:
            return "tree_right_house"
        
    elif path == "tree_left_dead":
        print('the path isn’t as straightforward as you hoped, and it’s getting darker')
        print('You see a figure ahead...it is not a tree')
        return "tree_left_dead"
    
    elif path == "tree_right_house":
        print('You keep walking until you see the house. It is eerie and dilapitated')
        print('You press on and open the door. Dust blows your face, it stings')
        print('You look around, thhe house is clearly abandoned\n do you..:')

        print('1. Search the house')
        print('2. Leave')

        choice = input("Enter your choice(1 or 2): ").strip()
        while choice not in ['1', '2']:
            print("Invalid input. ENTER 1 OR 2")
            choice = input("Enter your choice(1 or 2): ").strip()

        if choice == '1':
            return 'house_search_1'
        
        else:
            return 'house_leave_dead'


def get_story(path):
    stories = {"house_leave_dead":"You leave the house. Darkness blinds you. You trip and see a figure overhead...",
               'house_search_1':"You search the house and find a backpack. Inside is a flashlight",
               "leave_flash_dead":"You leave without testing the flashlight. Something hits your head.",
               "keep_searching_battery":"You find batteries under the bed. You put them in the flashlight.\nIt works!",
               "house_search_2_dead":"You keep searching. A white bearded man enters. He's not happy. He attacks",
               "leave_w_flashlight":"You leave the house cautiously with your working flashlight",
               "dark_move":"You move in the dark. You trip. Your anke hurts. You turn on the flashlight anyway",
               "Turn_On":"You turn on the flashlight. You see a way out. This must be it",
               "highway_alive":"You stumble onto the highway. Stick your thumb out. A car slows down beside. Inside... a white bearded man",
               "get_in_first_car":"He drives and asks oddly pointed questions. You realize he's driving you back to the forest.\nThe car door is locked.",
               "refuse_first_car":"You refuse the first man. A friendly couple pulls up",
               "no_second_car":"You refuse them. No one else comes.\nSomething drags you back.",
               "get_in_second_car":"They're friendly people. They're even going back to your town!",
               "after_second_car_question": "They ask if you want to go home or to the police station.",
               "good_ending_police":"They take you to the police station. You file a report then go home",
               "good_ending_home":"They take you home. Your parents run to you."
    }
    return stories.get(path, "")

def get_choices(path):
    choices = {"house_search_1":["Keep searching", "Leave"],
               "keep_searching_battery":["Keep searching", "Leave"],
               "leave_w_flashlight":["Move in darkness", "Turn on the flashlight"],
               "highway_alive":["Get in the car", "Don't get in"],
               "refuse_first_car":["Get in the second car", "Don't get in"],
               "after_second_car_question": ["Police station", "Home"]
    }

    return choices.get(path, [])

def play_again():
    while True:
        answer = input('Play again? (Y/N): ').strip().upper()
        if answer == 'Y':
            return True
        elif answer == 'N':
            return False
        else:
            print('Enter a valid input(Y/N)')


def print_end_message(name, ending):
    if ending == "safe":
        print(f"Congratulations, {name}! You're safe")

    else:
        print("You died. Womp Womp")



def main():
    name = get_name()
    print_welcome(name)

    input("Press Enter to begin...")

    while True:
        path = start_game()

        while True:
            if path in ["left_path", "right_path", "tree_left_dead", "tree_right_house"]:
                path = make_choice(path)

                if path in ["left_dead", "tree_left_dead"]:
                    print_end_message(name, "dead")
                    break
            else:


                if path in ["dark_move", "Turn_On"]:
                    print("\n" + get_story(path))
                    path = "highway_alive"
                    continue

                print("\n"+ get_story(path))
                opts = get_choices(path)


                if path == "get_in_second_car":
                    path = "after_second_car_question"
                    continue
                
                if not opts:
                    if path in ["good_ending_home", "good_ending_police"]:
                        print_end_message(name, "safe")

                    else:
                        print_end_message(name, "dead")

                    break

                for i, option in enumerate(opts, 1):
                    print(f"{i}. {option}")

                choice = input("Enter your choice: ").strip()

                while choice not in ["1", "2"]:
                    choice = input("Enter 1 or 2: ").strip()


                if path == "house_search_1":
                    if choice == "1":
                        path = "keep_searching_battery"
                    else:
                        path = "leave_flash_dead"

                elif path == "keep_searching_battery":
                    if choice == "1":
                        path = "house_search_2_dead"

                    else:
                        path = "leave_w_flashlight"

                elif path == "leave_w_flashlight":
                    if choice == '1':
                        path = "dark_move"

                    else:
                        path = "Turn_On"
                
                elif path in ["dark_move", "Turn_On"]:
                    path = "highway_alive"
                
                elif path == "highway_alive":
                    if choice == "1":
                        path = "get_in_first_car"
                    else: 
                        path = "refuse_first_car"
                
                elif path == "refuse_first_car":
                    if choice == "1":
                        path = "get_in_second_car"

                    else:
                        path = "no_second_car"


                elif path == "after_second_car_question":
                    if choice == "1":
                        path = "good_ending_police"
                    else:
                        path = "good_ending_home"

        if not play_again():
            print("\nThanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()