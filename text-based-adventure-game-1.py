import random
import time

def print_slow(text):
    """Print text with a typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.score = 0

def game():
    # Game introduction
    print_slow("Welcome to the Mini Adventure!")
    print_slow("Enter your name, brave adventurer: ")
    player_name = input()
    player = Player(player_name)
    
    print_slow(f"\nWelcome, {player.name}! Your adventure begins...")
    
    while player.health > 0:
        # Main game loop
        print_slow("\nWhat would you like to do?")
        print("\n1. Explore")
        print("2. Check inventory")
        print("3. Check status")
        print("4. Quit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            explore(player)
        elif choice == "2":
            check_inventory(player)
        elif choice == "3":
            check_status(player)
        elif choice == "4":
            print_slow("\nThanks for playing! Goodbye!")
            break
        else:
            print_slow("\nInvalid choice. Please try again.")

def explore(player):
    events = [
        "found a treasure chest",
        "encountered a friendly merchant",
        "found a healing potion",
        "encountered a monster"
    ]
    
    event = random.choice(events)
    print_slow(f"\nYou {event}!")
    
    if event == "found a treasure chest":
        gold = random.randint(10, 50)
        player.score += gold
        print_slow(f"You found {gold} gold pieces!")
        
    elif event == "encountered a friendly merchant":
        print_slow("The merchant gives you a mysterious map!")
        player.inventory.append("mysterious map")
        
    elif event == "found a healing potion":
        print_slow("You drink the healing potion and feel better!")
        player.health = min(100, player.health + 30)
        
    elif event == "encountered a monster":
        damage = random.randint(10, 25)
        player.health -= damage
        print_slow(f"The monster attacks you for {damage} damage!")
        if player.health <= 0:
            print_slow("Game Over! You have been defeated!")

def check_inventory(player):
    if not player.inventory:
        print_slow("\nYour inventory is empty!")
    else:
        print_slow("\nYour inventory contains:")
        for item in player.inventory:
            print_slow(f"- {item}")

def check_status(player):
    print_slow(f"\nName: {player.name}")
    print_slow(f"Health: {player.health}")
    print_slow(f"Score: {player.score}")

if __name__ == "__main__":
    game()