import actors import Creature, Dragon, Wizard
import random


def main():
    print_header()
    game_loop()
    
def print_header():
    print('-------------------------------')
    print('          WIZARD GAME          ')
    print('-------------------------------')
    print()

def game_loop():
    creatures = [
            Creature('Bat', 5),
            Creature('Toad', 1),
            Creature('Tiger', 12),
            Dragon('Black Dragon', 50, scaliness=2, breathes_fire=False),
            Wizard('Evil Wizard', 1000),
    ]
    
    hero = Wizard('Gandolf', 75)
    
    while True:
        
        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest...'
              .format(active_creature.name, active_creature.value))
        
        
        #ask user for action
        if win or exit:
            break
        
    print("Goodbye")
    
class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        
    def defensive_roll(self):
        roll = random.randint(1, 12)
        return roll * self.level
    
