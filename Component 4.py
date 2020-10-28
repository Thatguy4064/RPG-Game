'''
Author:Israel Flannery
Date:15/10/2020
Description:Split Rooms
Version:4.0
'''

#--------Libraries-------#
import sqlite3
from sqlite3 import Error
import random

#------Functions--------#
def storyrightroom():
    print('''You look down at the overgrown bat and decide to continue on past and head
through the right door, on the other side is just a long hallway with a door at the end''')
    loop = True
    while loop:
        hlook = input('You have some options look [a]round, head to the [d]oor: ').lower()
        if hlook == 'a' or hlook == 'look around':
            print('''You look around and find nothing of note, no secret
passages, no secret items, no secret doors, its just a regular hallway''')
        elif hlook == 'd' or hlook == 'door':
            loop = False
            print('''You approach the door and spot a monster!!!
Upon further inspection the monster is a Goat!!! "MEEEEEEEAH" it says dinging its bell
threateningly. You have never seen a creature like this before, but surely its not that hard, right?''')
            goatfight()
        else:
            print('You sit around and do nothing')
            print('.....')
            print('Time to go')
def goatfight():
    playerhp = 100
    goat = 15
    playerweapon = 'Sword'
    print('You engage the Goat')
    print('Your Health', playerhp)
    print('Goat Health', goat)
    skill = 3
    while playerhp > 0 and goat > 0:
        playerattack = random.randint(6,8)
        playermagic = random.randint(6,12)
        goatattack = random.randint(6,10)
        
        move = input("""Select an action
                        [a]ttack with """ +playerweapon+ """
                        [b]lock the attack
                        [m]agic attack
                        [s]kill
                        """).lower()
        if move == "a" or move == "attack":
            stunchance = random.randint(1,2)
            if stunchance == 1:
                goat = goat - playerattack
                print('you deal', playerattack, 'to the Goat',  goat)
                playerhp = playerhp - goatattack
                print('the Goat attacks you dealing', goatattack, 'to your', playerhp)
            elif stunchance == 2:
                goat = goat - playerattack
                print('you attack the Goat and stun it dealing', playerattack, 'damage, Goat hp', goat)
        elif move == 'b':
            deflectchance = random.randint(1,2)
            if deflectchance == 1:
                goat = goat - playerattack
                print('you deflect the attack, you deal', playerattack, 'to the Goats health', goat)
            elif deflectchance == 2:
                playerhp = playerhp - goatattack
                print('you attempt to deflect the attack but fail, he deals', goatattack, 'to your hp',playerhp)
        elif move == 'm':
            fuzzlechance = random.randint(1,2)
            if fuzzlechance == 1:
                goat = goat - playermagic
                print('you casted a spell dealing', playermagic, 'to the Goat', goat)
            elif fuzzlechance == 2:
                playerhp = playerhp - goatattack
                print('your spell failed and the Goat attacked dealing', goatattack, 'to your hp', playerhp,)
        elif move == 's':
            if skill > 0:
                print('You use your skill, Warcry')
                goat = goat - playerattack
                print('you scream at the goat allowing you to gain the upper hand and attack for free', goat)
                skill = skill - 1
            else:
                playerhp = playerhp - goatattack
                print('you cannot use that anymore')
                print('you stand still and get hit by the Goat, he deals', goatattack, 'to your hp', playerhp)
        else:
            playerhp = playerhp - goatattack
            print('you stand still and get hit by the Goat, he deals', goatattack, 'to your hp', playerhp)
    if playerhp < 1:
        print('you died')
    elif goat < 1:
        print('you killed the Goat')

def storyleftroom():
    print('''You look down at the Little Green Slime and you begin to be filled with sadness...
after having a good cry you decide to continue on past and headthrough the left door,
on the other side is just a long hallway with a door at the end''')
    loop = True
    while loop:
        hlook = input('You have some options look [a]round, head to the [d]oor: ').lower()
        if hlook == 'a' or hlook == 'look around':
            print('''You look around and find nothing of note, no secret
passages, no secret items, no secret doors, its just a regular hallway, except for a
strangley out of place wooden chair.''')
        elif hlook == 'd' or hlook == 'door':
            loop = False
            print('''You approach the door and spot a monster!!!
Upon further inspection its just a wooden chair... "CREEEEEAK" the chair says as you sit down on it?
What, the chair reveals itself to be a chair mimic and you engage in combat.''')
            chairfight()
        else:
            print('You sit around and do nothing')
            print('.....')
            print('Time to go')

def chairfight():
    playerhp = 100
    chair = 15
    playerweapon = 'Sword'
    print('You engage the Chair Mimic')
    print('Your Health', playerhp)
    print('Chair Mimic Health', chair)
    skill = 2
    while playerhp > 0 and chair > 0:
        playerattack = random.randint(6,8)
        playermagic = random.randint(6,12)
        chairattack = random.randint(8,12)
        move = input("""Select an action
                        [a]ttack with """ +playerweapon+ """
                        [b]lock the attack
                        [m]agic attack
                        [s]kill
                        """).lower()
        if move == "a" or move == "attack":
            stunchance = random.randint(1,2)
            if stunchance == 1:
                chair = chair - playerattack
                print('you deal', playerattack, 'to the Chair Mimic',  chair)
                playerhp = playerhp - chairattack
                print('the Chair Mimic attacks you dealing', chairattack, 'to your', playerhp)
            elif stunchance == 2:
                chair = chair - playerattack
                print('you attack the Chair Mimic and stun it dealing', playerattack, 'damage, Chair Mimic hp', goat)
        elif move == 'b':
            deflectchance = random.randint(1,2)
            if deflectchance == 1:
                chair = chair - playerattack
                print('you deflect the attack, you deal', playerattack, 'to the Chair Mimic health', goat)
            elif deflectchance == 2:
                playerhp = playerhp - chairattack
                print('you attempt to deflect the attack but fail, he deals', chairattack, 'to your hp',playerhp)
        elif move == 'm':
            fuzzlechance = random.randint(1,2)
            if fuzzlechance == 1:
                chair = chair - playermagic
                print('you casted a spell dealing', playermagic, 'to the Chair Mimic', chair)
            elif fuzzlechance == 2:
                playerhp = playerhp - chairattack
                print('your spell failed and the Chair Mimic attacked dealing', chairattack, 'to your hp', playerhp,)
        elif move == 's':
            if skill > 0:
                print('You use your skill, Elven Knowlodge')
                chair = chair - playermagic
                print('you use your knowlodge of magic to cast a spell without fail to the Chair Mimic', chair)
                skill = skill - 1
            else:
                playerhp = playerhp - chairattack
                print('you cannot use that anymore')
                print('you stand still and get hit by the Chair Mimic, he deals', chairattack, 'to your hp', playerhp)
        else:
            playerhp = playerhp - chairattack
            print('you stand still and get hit by the Chair Mimic, he deals', chairattack, 'to your hp', playerhp)
    if playerhp < 1:
        print('you died')
    elif chair < 1:
        print('you killed the Chair Mimic')




#-------Main------#
storyrightroom()
