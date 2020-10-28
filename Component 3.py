'''
Author:Israel Flannery
Date:15/10/2020
Description:Second Room
Version:3.3
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
        hlook = input('You have some options look [a]round, take the [l]eft door or the [r]ight door: ').lower()
        if hlook == 'a' or hlook == 'look around':
            loop = False
            print('''You look around the room some more and discover a dusty crate,
you look inside the crate and find some useful things, you look on the side of the crate
and read the sign "Crate of Useful Things". {Acquired "Useful Things?"}''')
            print('''You approach the right door and spot a monster!!!
Upon further inspection the monster is an overgrown bat!!! "Bleh Bleh" it says.
Your not scared and ready your weapon to battle the overgrown bat...''')
            rightroomfight()
        elif hlook == 'l' or hlook == 'left door':
            loop = False
            print('''You approach the left door and spot a monster!!!
Upon further inspection the monster is a little green slime!!! "I'm not a bad
slime SLURP" it says. You suddenly are filled with guilt in needing to battle this
small green slime...''')
            leftroomfight()
        elif hlook == 'r' or hlook == 'right door':
            loop = False
            print('''You approach the right door and spot a monster!!!
Upon further inspection the monster is an overgrown bat!!! "Bleh Bleh" it says.
Your not scared and ready your weapon to battle the overgrown bat...''')
            rightroomfight()
        else:
            print('You sit around and do nothing')
            print('.....')
            print('Time to go')
def rightroomfight():
    playerhp = 100
    overgrownbat = 10
    playerweapon = 'Sword'
    print('You engage the Overgrown Bat')
    print('Your Health', playerhp)
    print('Overgrown Bat Health', overgrownbat)
    skill = 1
    while playerhp > 0 and overgrownbat > 0:
        playerattack = random.randint(3,5)
        playermagic = random.randint(1,6)
        batattack = random.randint(1,4)
        
        move = input("""Select an action
                        [a]ttack with """ +playerweapon+ """
                        [b]lock the attack
                        [m]agic attack
                        [s]kill
                        """).lower()
        if move == "a" or move == "attack":
            stunchance = random.randint(1,2)
            if stunchance == 1:
                overgrownbat = overgrownbat - playerattack
                print('you deal', playerattack, 'to the Overgrown Bat',  overgrownbat)
                playerhp = playerhp - batattack
                print('the Overgrown Bat attacks you dealing', batattack, 'to your', playerhp)
            elif stunchance == 2:
                overgrownbat = overgrownbat - playerattack
                print('you attack the Overgrown Bat and stun it dealing', playerattack, 'damage, Overgrown Bat hp', overgrownbat)
        elif move == 'b':
            deflectchance = random.randint(1,2)
            if deflectchance == 1:
                overgrownbat = overgrownbat - playerattack
                print('you deflect the attack, you deal', playerattack, 'to the Overgrown Bats health', overgrownbat)
            elif deflectchance == 2:
                playerhp = playerhp - batattack
                print('you attempt to deflect the attack but fail, he deals', batattack, 'to your hp',playerhp)
        elif move == 'm':
            fuzzlechance = random.randint(1,2)
            if fuzzlechance == 1:
                overgrownbat = overgrownbat - playermagic
                print('you casted a spell dealing', playermagic, 'to the Overgrown Bat', overgrownbat)
            elif fuzzlechance == 2:
                playerhp = playerhp - batattack
                print('your spell failed and the Overgrown Bat attacked dealing', batattack, 'to your hp', playerhp,)
        elif move == 's':

            if skill > 0:
                print('You use your skill, Strength of the Weak')
                overgrownbat = overgrownbat - playerattack*2
                print('you strike at the Overgrown bat dealing massive damage leaving the Overgrown Bat with', overgrownbat)
                skill = skill - 1
            else:
                playerhp = playerhp - batattack
                print('you cannot use that anymore')
                print('you stand still and get hit by the Overgrown Bat, he deals', batattack, 'to your hp', playerhp)
        else:
            playerhp = playerhp - batattack
            print('you stand still and get hit by the Overgrown Bat, he deals', batattack, 'to your hp', playerhp)
    if playerhp < 1:
        print('you died')
    elif overgrownbat < 1:
        print('you killed the Overgrown Bat')
def leftroomfight():
    playerhp = 100
    greenslime = 15
    playerweapon = 'Sword'
    print('You engage the Little Green Slime')
    print('Your Health', playerhp)
    print('Little Green Slime Health', greenslime)
    skill = 2
    while playerhp > 0 and greenslime > 0: #everything below this is the battle system
        playerattack = random.randint(3,5)
        playermagic = random.randint(1,6)
        slimeattack = random.randint(2,5)
        
        move = input("""Select an action
                        [a]ttack with """ +playerweapon+ """
                        [b]lock the attack
                        [m]agic attack
                        [s]kill
                        """).lower()
        if move == "a" or move == "attack":
            stunchance = random.randint(1,2) #stunning is a chance that can happen to help the player
            if stunchance == 1:
                greenslime = greenslime - playerattack
                print('you deal', playerattack, 'to the Little Green Slime',  greenslime)
                playerhp = playerhp - slimeattack
                print('the Little Green Slime attacks you dealing', slimeattack, 'to your', playerhp)
            elif stunchance == 2:
                greenslime = greenslime - playerattack
                print('you attack the Little Green Slime and stun it dealing', playerattack, 'damage, Little Green Slime hp', greenslime)
        elif move == 'b':
            deflectchance = random.randint(1,2) #you have a chance to deflect the attack dealing damage back to the enemy
            if deflectchance == 1:
                greenslime = greenslime - playerattack
                print('you deflect the attack, you deal', playerattack, 'to the Little Green Slimes health', greenslime)
            elif deflectchance == 2:
                playerhp = playerhp - slimeattack
                print('you attempt to deflect the attack but fail, it deals', slimeattack, 'to your hp',playerhp)
        elif move == 'm':
            fuzzlechance = random.randint(1,2) #Fuzzling is a mechanic where the spell fails
            if fuzzlechance == 1:
                greenslime = greenslime - playermagic
                print('you casted a spell dealing', playermagic, 'to the Little Green Slime', greenslime)
            elif fuzzlechance == 2:
                playerhp = playerhp - slimeattack
                print('your spell failed and the Little Green Slime attacked dealing', slimeattack, 'to your hp', playerhp,)
        elif move == 's':
            if skill > 0: #skills can only be used a set number of times resulting in it haveing none left
                print('You use your skill, HONK!')
                honk = random.randint(-20,30)
                greenslime = greenslime - honk
                print('you honk at the Overgrown dealing a random amount of damage leaving the Little Green Slime with', greenslime)
                skill = skill - 1
            else:
                playerhp = playerhp - slimeattack
                print('you cannot use that anymore')
                print('you stand still and get hit by the Little Green Slime, he deals', slimeattack, 'to your hp', playerhp)
        else:
            playerhp = playerhp - slimeattack
            print('you stand still and get hit by the Little Green Slime, he deals', slimeattack, 'to your hp', playerhp)
    if playerhp < 1:
        print('you died')
    elif greenslime < 1:
        print('you killed the Little Green Slime')
#-------Main------#
story()
