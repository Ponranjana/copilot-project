import random
from enum import Enum
from abc import ABC, abstractmethod

# Clues and sensory experiences
clues = [
    "There is a faded tapestry depicting a battle long forgotten.",
    "There is a broken chalice lying in the dust, hinting at a lost celebration.",
    "There is a scorch mark on the stone, as if magic once raged here.",
    "There is a whisper of laughter echoing from unseen corners.",
    "There is a shattered mirror reflecting only shadows.",
    "There is a rusted key on the floor, untouched for ages.",
    "There is a cryptic symbol etched into the wall.",
    "There is a lingering scent of incense, as if a ritual was performed.",
    "There is a torn page from an ancient tome, half-buried under debris.",
    "There is a cold draft that seems to carry distant voices."
]

sense_exp = [
    "You see flickering candlelight casting eerie shadows.",
    "You hear distant footsteps echoing through the halls.",
    "You smell damp stone and old parchment.",
    "You feel a chill crawling up your spine.",
    "You sense a presence watching from the darkness.",
    "You hear the faint clinking of chains.",
    "You see dust motes swirling in a shaft of moonlight.",
    "You smell the faint aroma of burnt herbs.",
    "You feel the rough texture of ancient stone beneath your fingers.",
    "You sense a strange energy pulsing in the air.",
    "You hear a low, mournful wind whistling through cracks.",
    "You see a shadow dart across the far wall."
]

class RandomItemSelector:
    def __init__(self, items):
        self.items = list(items)
        self.used_items = []

    def add_item(self, item):
        self.items.append(item)

    def pull_random_item(self):
        available = [item for item in self.items if item not in self.used_items]
        if not available:
            self.used_items = []
            available = self.items.copy()
        if not available:
            return None
        item = random.choice(available)
        self.used_items.append(item)
        return item

    def reset(self):
        self.used_items = []

class SenseClueGenerator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SenseClueGenerator, cls).__new__(cls)
            cls._instance.clue_selector = RandomItemSelector(clues)
            cls._instance.sense_selector = RandomItemSelector(sense_exp)
        return cls._instance

    def get_senseclue(self):
        clue = self.clue_selector.pull_random_item()
        sense = self.sense_selector.pull_random_item()
        return f"{clue} {sense}"

class EncounterOutcome(Enum):
    CONTINUE = 1
    END = 2

class Encounter(ABC):
    @abstractmethod
    def run_encounter(self):
        pass

class DefaultEncounter(Encounter):
    def __init__(self):
        self.scg = SenseClueGenerator()

    def run_encounter(self):
        output = self.scg.get_senseclue()
        print(f"\n{output}\n")
        return EncounterOutcome.CONTINUE

class Room:
    def __init__(self, name, encounter):
        self.name = name
        self.encounter = encounter

    def visit_room(self):
        return self.encounter.run_encounter()

# Room names
room_names = [
    "Grand Hall",
    "Library of Whispers",
    "Armory of Shadows",
    "Moonlit Conservatory",
    "Dungeon Depths",
    "Royal Observatory"
]

rooms = [Room(name, DefaultEncounter()) for name in room_names]

class Castle:
    def __init__(self, rooms):
        self.room_selector = RandomItemSelector(rooms)

    def select_door(self):
        num_doors = random.randint(2, 4)
        print(f"\nYou see {num_doors} doors before you.")
        while True:
            choice = input(f"Choose a door (1-{num_doors}): ")
            if choice.isdigit() and 1 <= int(choice) <= num_doors:
                return int(choice)
            print("Invalid choice. Please try again.")

    def next_room(self):
        self.select_door()
        room = self.room_selector.pull_random_item()
        print(f"\nYou enter: {room.name}\n")
        return room.visit_room()

    def reset(self):
        self.room_selector.reset()

class Game:
    def __init__(self, rooms):
        self.castle = Castle(rooms)

    def play_game(self):
        print("Welcome to the Castle Adventure!")
        print("Your objective: Navigate through the castle and find the treasure to win.\n")
        while True:
            result = self.castle.next_room()
            if result == EncounterOutcome.END:
                self.castle.reset()
                print("\nGame Over.\n")
                again = input("Would you like to explore a different castle? (y/n): ")
                if again.lower() != 'y':
                    print("Farewell, adventurer!")
                    break
            # Otherwise, continue loop

# ==== Task 5 ====

class TreasureEncounter(Encounter):
    def run_encounter(self):
        print("\nYou have found the treasure! You have won the game!\n")
        return EncounterOutcome.END

treasure_room = Room("Treasure Vault", TreasureEncounter())
rooms.append(treasure_room)

# Red Wizard Spell Battle
spell_options = ["Fireball", "Ice Shard", "Wind Gust", "Lightning Bolt", "Earthquake"]
spell_game_rules = {
    "Fireball": ["Ice Shard", "Lightning Bolt"],
    "Ice Shard": ["Wind Gust", "Earthquake"],
    "Wind Gust": ["Lightning Bolt", "Fireball"],
    "Lightning Bolt": ["Earthquake", "Ice Shard"],
    "Earthquake": ["Fireball", "Wind Gust"]
}

class RedWizardEncounter(Encounter):
    def run_encounter(self):
        print("\nYou face the Red Wizard! Prepare for a spell battle!\n")
        while True:
            print("Choose your spell:")
            for idx, spell in enumerate(spell_options, 1):
                print(f"{idx}. {spell}")
            user_choice = input("Your spell: ")
            if not user_choice.isdigit() or not (1 <= int(user_choice) <= len(spell_options)):
                print("Invalid choice. Try again.")
                continue
            user_spell = spell_options[int(user_choice)-1]
            wizard_spell = random.choice(spell_options)
            print(f"\nYou cast {user_spell}. The Red Wizard casts {wizard_spell}.\n")
            if user_spell == wizard_spell:
                print("It's a draw! The battle continues...\n")
                continue
            elif wizard_spell in spell_game_rules[user_spell]:
                print("You have vanquished the Red Wizard from this castle!\n")
                return EncounterOutcome.CONTINUE
            else:
                print("The Red Wizard has vanquished you from this castle!\n")
                return EncounterOutcome.END

red_wizard_room = Room("The Red Wizard's Lair", RedWizardEncounter())
rooms.append(red_wizard_room)

# Blue Wizard - Fantasy alternatives to Rock, Paper, Scissors
blue_spell_options = ["Magic Shield", "Enchanted Blade", "Mystic Scroll"]
blue_spell_game_rules = {
    "Magic Shield": ["Enchanted Blade"],
    "Enchanted Blade": ["Mystic Scroll"],
    "Mystic Scroll": ["Magic Shield"]
}

class BlueWizardEncounter(Encounter):
    def run_encounter(self):
        print("\nYou face the Blue Wizard! Prepare for a magical duel!\n")
        while True:
            print("Choose your magical item:")
            for idx, spell in enumerate(blue_spell_options, 1):
                print(f"{idx}. {spell}")
            user_choice = input("Your item: ")
            if not user_choice.isdigit() or not (1 <= int(user_choice) <= len(blue_spell_options)):
                print("Invalid choice. Try again.")
                continue
            user_spell = blue_spell_options[int(user_choice)-1]
            wizard_spell = random.choice(blue_spell_options)
            print(f"\nYou use {user_spell}. The Blue Wizard uses {wizard_spell}.\n")
            if user_spell == wizard_spell:
                print("It's a draw! The duel continues...\n")
                continue
            elif wizard_spell in blue_spell_game_rules[user_spell]:
                print("You have vanquished the Blue Wizard from this castle!\n")
                return EncounterOutcome.CONTINUE
            else:
                print("The Blue Wizard has vanquished you from this castle!\n")
                return EncounterOutcome.END

blue_wizard_room = Room("The Blue Wizard's Lair", BlueWizardEncounter())
rooms.append(blue_wizard_room)

# Run the game
if __name__ == "__main__":
    game = Game(rooms)
    game.play_game()