import random

# Define the rooms and their descriptions
rooms = {
    'start': "You are standing at the entrance of a mysterious cave.",
    'cave': "You're in a dark cave. You can hear water dripping from somewhere deep inside.",
    'crossroads': "You've reached a crossroads. There are three paths ahead of you.",
    'treasure': "You've found the treasure room! It's filled with gold and jewels.",
    'dragon': "You've stumbled upon a sleeping dragon. Be very quiet...",
    'trap': "You fell into a trap! You're now stuck.",
    'riddle': "You encounter a mysterious riddle. Solve it to proceed.",
    'exit': "Congratulations! You've successfully escaped from the cave!"
}

# Define the actions available in each room
actions = {
    'start': ['Go deeper into the cave', 'Leave the cave'],
    'cave': ['Go back to the entrance', 'Go further into the cave'],
    'crossroads': ['Go left', 'Go straight ahead', 'Go right'],
    'treasure': ['Take the treasure', 'Leave the treasure room'],
    'dragon': ['Sneak past the dragon', 'Fight the dragon'],
    'trap': ['Try to escape the trap', 'Wait for rescue'],
    'riddle': ['Attempt to solve the riddle'],
}

# Define items available in the game
items = {
    'sword': "A sharp sword",
    'key': "A rusty key",
    'map': "A mysterious map",
    'torch': "A bright torch",
    'rope': "A sturdy rope",
    'potion': "A healing potion"
}

# Define a function to handle player input
def get_choice(room):
    print("\nWhat will you do?\n")
    for i, action in enumerate(actions[room]):
        print(f"{i + 1}: {action}")
    choice = input("\nEnter your choice: ")
    return int(choice) - 1

# Define a function to handle random encounters
def random_encounter():
    encounter_chance = random.random()
    if encounter_chance < 0.3:
        print("You encounter a group of bats! They swoop down and steal your torch.")
        return 'torch'
    elif encounter_chance < 0.6:
        print("You find a hidden stash of gold!")
        return 'gold'
    else:
        print("You stumble upon a secret passage.")
        return 'secret_passage'

# Define the main game function
def play_game():
    current_room = 'start'
    inventory = []

    while True:
        print("\n" + rooms[current_room])
        
        # Handle special room events
        if current_room == 'trap':
            if random.random() < 0.5:
                print("A rescue team finds you and pulls you out of the trap. You're free!")
                current_room = 'start'
            else:
                print("You're still stuck in the trap. Try again later.")
        elif current_room == 'riddle':
            print("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?")
            answer = input("\nEnter your answer: ").lower()
            if answer == 'echo':
                print("Correct! The passage opens up, and you proceed.")
                current_room = 'exit'
            else:
                print("Incorrect! The walls start closing in. You barely escape, but you're back in the cave.")
                current_room = 'cave'
        elif current_room == 'cave':
            item_found = random_encounter()
            if item_found:
                print(f"You found {items[item_found]}!")
                inventory.append(item_found)
        
        # Get player choice
        choice = get_choice(current_room)
        
        # Handle player choices
        if current_room == 'start':
            if choice == 0:
                current_room = 'cave'
            elif choice == 1:
                print("You leave the cave. Game over!")
                break
        elif current_room == 'cave':
            if choice == 0:
                current_room = 'start'
            elif choice == 1:
                current_room = 'crossroads'
        elif current_room == 'crossroads':
            if choice == 0:
                current_room = 'treasure'
            elif choice == 1:
                current_room = 'dragon'
            elif choice == 2:
                current_room = 'cave'
        elif current_room == 'treasure':
            if choice == 0:
                print("Congratulations! You've taken the treasure. You win!")
                break
            elif choice == 1:
                current_room = 'crossroads'
        elif current_room == 'dragon':
            if choice == 0:
                print("You try to sneak past the dragon... and succeed! You escape!")
                break
            elif choice == 1:
                print("You attempt to fight the dragon...")
                if 'sword' in inventory:
                    print("With your sword in hand, you slay the dragon!")
                    current_room = 'exit'
                else:
                    print("You don't have a sword! The dragon devours you. Game over!")
                    break
        elif current_room == 'trap':
            if choice == 0:
                print("You try to escape the trap...")
                if 'rope' in inventory:
                    print("Using the rope, you manage to climb out of the trap.")
                    current_room = 'start'
                else:
                    print("You don't have anything to help you escape. You wait for rescue.")
            elif choice == 1:
                print("You decide to wait for rescue.")
        elif current_room == 'riddle':
            if choice == 0:
                print("You attempt to solve the riddle...")
                # The riddle handling is done separately above
                pass

# Start the game
play_game()
