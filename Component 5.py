
'''
Author:Israel Flannery
Date:15/10/2020
Description:left Room 2
Version:5.0
'''

#--------Libraries-------#
import sqlite3
from sqlite3 import Error
import random

#------Functions--------#
def story():
    print('''you look down at the remains of the chair mimic, it looked just
like a regular chair. Upon entering the room you reach a dining hall,
at the end is a door''')
    loop = True
    while loop:
        hlook = input('You have some options look [a]round or head to the [d]oor: ').lower()
        if hlook == 'a' or hlook == 'look around':
            print('''You look around the dining room, its hard to imagine something this beautiful
being in a dirty old dungeon like this, you look at the table and see freshly made food,
roasted chicken, hamburgers, fried chips and more. You take a bite of everything on the table.''')
        elif hlook == 'd' or hlook == 'door':
            loop = False
            print('''You approach the door and spot a monster!!!
Upon further inspection the monster is a Gremlin Granny!!! "You better eat your brussel sprouts sonny." she says.
The Gremlin Granny readys what looks to be a brussel sprout into her laddle to toss it at you...''')
            grannyfight()
        else:
            print('You sit around and do nothing')
            print('.....')
            print('Time to go')


def grannyfight():
    playerhp = 100
    granny = 25
    playerweapon = 'Sword'
    print('You engage the Gremlin Granny')
    print('Your Health', playerhp)
    print('Gremlin Granny Health', granny)
    skill = 1
    while playerhp > 0 and granny > 0:
        playerattack = random.randint(3,5)
        playermagic = random.randint(3,12)
        granattack = random.randint(14,21)
        
        move = input("""Select an action
                        [a]ttack with """ +playerweapon+ """
                        [b]lock the attack
                        [m]agic attack
                        [s]kill
                        """).lower()
        if move == "a" or move == "attack":
            stunchance = random.randint(1,2)
            if stunchance == 1:
                granny = granny - playerattack
                print('you deal', playerattack, 'to the Gremlin Granny',  granny)
                playerhp = playerhp - granattack
                print('the Gremlin Granny attacks you dealing', granattack, 'to your', playerhp)
            elif stunchance == 2:
                granny = granny - playerattack
                print('you attack the Gremlin Granny and stun it dealing', playerattack, 'damage, Gremlin Granny hp', granny)
        elif move == 'b':
            deflectchance = random.randint(1,2)
            if deflectchance == 1:
                granny = granny - playerattack
                print('you deflect the attack, you deal', playerattack, 'to the Gremlin Grannys health', granny)
            elif deflectchance == 2:
                playerhp = playerhp - granattack
                print('you attempt to deflect the attack but fail, she deals', granattack, 'to your hp',playerhp)
        elif move == 'm':
            fuzzlechance = random.randint(1,2)
            if fuzzlechance == 1:
                granny = granny - playermagic
                print('you casted a spell dealing', playermagic, 'to the Gremlin Granny', granny)
            elif fuzzlechance == 2:
                playerhp = playerhp - granattack
                print('your spell failed and the Gremlin Granny attacked dealing', granattack, 'to your hp', playerhp,)
        elif move == 's':
            if skill > 0:
                print('You use your skill, Dragons Breath')
                granny = granny - playermagic*2
                print('you breath fire at the Gremlin Granny dealing massive damage leaving the Gremlin Granny with', granny)
                skill = skill - 1
            else:
                playerhp = playerhp - batattack
                print('you cannot use that anymore')
                print('you stand still and get hit by the Gremlin Granny, she deals', granattack, 'to your hp', playerhp)
        else:
            playerhp = playerhp - granattack
            print('you stand still and get hit by the Gremlin Granny, she deals', granattack, 'to your hp', playerhp)
    if playerhp < 1:
        print('you died')
    elif granny < 1:
        print('you killed the Gremlin Granny')


#--------Main----------#
story()
