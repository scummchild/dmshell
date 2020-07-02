from random import randint

import colorama

mobname = 'Goblin'
mob_dexterity = 2
roll = randint(1,20) + mob_dexterity

print(colorama.Fore.WHITE + f'The {mobname} rolled a {roll} for initiative')