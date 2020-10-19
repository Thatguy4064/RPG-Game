'''
Author:Israel Flannery
Date:15/10/2020
Description:Second Room
Version:3.0
'''

#--------Libraries-------#
import sqlite3
from sqlite3 import Error
import random

#------Functions--------#
def story():
    print('''The second room is a massive hall, looking around there are
multiple doors you can take...''')
    loop = True
    while loop:
        bhlook = input('You have some options look [a]round, take the [l]eft door or the [r]ight door: ').lower()
        if hlook == 'a' or hlook == 'look around':
            loop = False
            print('''You look around the room some more and discover a dusty crate,
you look inside the crate and find some useful things, you look on the side of the crate
and read the sign "Crate of Useful Things". {Acquired "Useful Things?"}''')
            print('''You approach the right door and spot a monster!!!
Upon further inspection the monster is an overgrown bat!!! "Bleh Bleh" it says.
Your not scared and ready your weapon to battle the overgrown bat...''')
            leftroomfight()
        elif hlook == 'l' or hlook == 'left door':
            loop = False
            print('''You approach the left door and spot a monster!!!
Upon further inspection the monster is a little green slime!!! "I'm not a bad
slime SLURP" it says. You suddenly are filled with guilt in needing to battle this
small green slime...''')
        elif hlook == 'r' or hlook == 'right door':
            loop = False
            print('''You approach the right door and spot a monster!!!
Upon further inspection the monster is an overgrown bat!!! "Bleh Bleh" it says.
Your not scared and ready your weapon to battle the overgrown bat...''')
            leftroomfight()
        else:
            print('You sit around and do nothing')
            print('.....')
            print('Time to go')
def leftroomfight():
    playerhp = 100
    overgrownbat = 10
    questions = [
{ 'What do ears do': ('Help you hear', 'help you eat', 'help you see', 2, 3)
'How do winged animals fly': ('With wings', 'By jumping', 'using psychic powers', 2, 3)
'Whos the best superhero': ('Batman', 'Batmam', 'bAtman', 2, 3)
},

{'The best fruit salad recipe': ('Dont you have a degree in a fruit', 'All the fruit', 'Just google it', 3, 4)
 'In theory if I couldnt see a thing and I looked in the mirror, what would I look like':('you look uh...charming?', 'Disgusting', 'Like a rat', 3, 4)
 'I have eyesight problems, how could I fix this': ('Wear glasses')
    },

{},

{},

{},
]
    #Their are 5 tiers of questions, unique to the monsters but follow the basic plan, generic, advanced, monster based, difficult and maths
    #the questions are within the dictionaries and in the brackets will be answers, damage the monster does and damage you can do
#-------Main------#
story()
