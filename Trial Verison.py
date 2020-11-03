'''
Author:Israel Flannery
Date:15/10/2020
Description:right Room 2
Version:6.0
'''

#--------Libraries-------#
import sqlite3
from sqlite3 import Error
import random

#------Functions--------#
def introduction():
    conn = None    
    db_file = "quiz.db"   

    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    c = conn.cursor()
    
    print('''
        Welcome to this RPG game, select your race and explore
        through this dungeon
        ''')
    loop = True
    while loop:
        choice1 = input('Would you like to start a [n]ew game: ')
        if choice1 == 'n' or choice1 == 'new':
            loop = False
            builder()    
        else:
            print('please enter a valid response')

def builder():
    
    loop = True
    while loop:
        newuser = input('Please enter your username: ')
        if newuser == '' or newuser == ' ':
            print('Please input a valid response')   
        else:
            loop = False
    loop = True
    while loop:
        newpass = input('Please enter your password: ')
        if newpass == '' or newpass == ' ':
            print('Please input a valid response')
        else:
            loop = False
    race_list = ['[G]oose', '[H]uman', '[O]rc', '[E]lf', '[D]ragonkin']
    loop = True
    print("""
            Welcome""",newuser, """to the character builder,
            here you can pick from an available
            race or class to help you in your quest
            """)
    while loop:
        print('Here are the avaliable races') 
        print(race_list)
        global user_race
        global race_skill
        global skillcount
        user_race = input('''
            please select from one of the races by entering the name or the
            the first letter of the name: 
            ''').lower()
        if user_race == 'g' or user_race == 'goose':
            print('''
                You are a goose, the special ability is Honk,
                Honk allows you to do a random damge effect ranging from
                massive damage to healing. Uses:2
                ''')
            skillcount = 2
            race_skill = skillcount
            loop = False
        elif user_race == 'h' or user_race == 'human':
            print('''
                    You are a Human, the special ability is Strength Of The Weak
                    This lets you do double your base damage. Uses:1
                    ''')
            skillcount = 1
            race_skill = skillcount
            loop = False
        elif user_race == 'o' or user_race == 'orc':
            print("""
                    You are an Orc, the special ability is called Warcry,
                    Warcry lets you do a basic attack without fail. uses:3
                    """)
            skillcount = 3
            race_skill = skillcount
            loop = False
        elif user_race == 'e' or user_race == 'elf':
            print("""
                    You are a Elf, the special ability is Elven Knowledge,
                    Elven knowlodge lets you attack with magic without fail. Uses:2
                    """)
            skillcount = 2
            race_skill = skillcount
            loop = False
        elif user_race == 'd' or user_race == 'dragonkin':
            print("""
                    You are a Dragonkin, the special ability is Dragons Breath
                    Dragonic Foresight lets you do double the usual amount of magic
                    damage. uses:1
                    """)
            skillcount = 1
            race_skill = skillcount
            loop = False
        else:
            loop = True
            print('please input a valid response')
    print('Now that you have built your character its time to name them')
    character_name = input('Please insert their name here:')
    conn = None    
    db_file = "quiz.db"   

    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    c = conn.cursor()
    user_list = [(newuser, newpass, character_name)]
    c.executemany("INSERT INTO players VALUES(?,?,?)",user_list)
    user_player = [character_name, user_race]
    story()

def story():
    conn = None    
    db_file = "quiz.db"   

    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    c = conn.cursor()
    print(''''You are an adventurer, with no adventure to go on. No quest to do,
no monsters to slay, you feel meanignless. The start of the day is like any other
day, sulking in the back of the tavern. However it ended up being different.
A strange man in black robes approaches you.''')
    print('''"Greetings young adventurer" The strange man says, "I know
of something that might interest you". You look at the man,
confused, yet interested to hear more. "Theres an ancient
dungeon that has been unexplored, I have been tasked by the
King to hire an adventurer to explore it" the strange man says,
holding out his arm.''')
    looptwo = True
    while looptwo:
        strangeman = input('Do you accept his deal [y]es or [n]o: ').lower()
        if strangeman == 'y' or strangeman == 'yes':
            looptwo = False
            print('''"Excellent, follow me and I shall lead you to the dungeon" the strange man says,
"Please follow me to the dungeon and we can talk about a reward for clearing the dungeon".''')
            print('''You follow the strange man to the dungeon. When you arrive the dungeon resembles
something of an old castle. "Now that we are here lets talk about a reward, I say 10 gold pieces" the strange man says.
"10 Gold Pieces" you think to yourself, "Thats hardly enough, but if i try to push my luck it could end badly"''')
            print('you decide to leave it be')
            print('''The strange man guides you into the first room and leaves.
You look around the room and notice this is nothing but an entrance hall. You notice a door.''')
            nextroom()
        elif strangeman == 'n' or strangeman == 'no':
            print('''"Well thats a shame, I guess no one does want to risk their life in an unexplored
dungeon, good day" the strange man walks off to find someone else. You sit there
alone, and in the next passing days you die of boredom...THE END''')
            looptwo = False
            score()
        else:
            print('"Your wasting my time, please answer the question" the strange man says')
def nextroom():
    loopthree = True
    while loopthree:
        progress = input('Would you like to open the door and go to the next room [y]es or [n]o: ').lower()
        if progress == 'y' or progress == 'yes':
            print('you open the door and head into the next room')
            loopthree = False
            story1()
        elif progress == 'n' or progress == 'no':
            print('You decide to have one more look around the room and find nothing, you head onto the next room')
            loopthree = False
            story1()
        else:
            print('You think a bit more')
    
def story1():
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
    global skillcount
    global user_race
    global race_skill
    race_skill = skillcount
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
        elif move == 'b' or move == 'block':
            deflectchance = random.randint(1,2)
            if deflectchance == 1:
                overgrownbat = overgrownbat - playerattack
                print('you deflect the attack, you deal', playerattack, 'to the Overgrown Bats health', overgrownbat)
            elif deflectchance == 2:
                playerhp = playerhp - batattack
                print('you attempt to deflect the attack but fail, he deals', batattack, 'to your hp',playerhp)
        elif move == 'm' or move == 'magic':
            fuzzlechance = random.randint(1,2)
            if fuzzlechance == 1:
                overgrownbat = overgrownbat - playermagic
                print('you casted a spell dealing', playermagic, 'to the Overgrown Bat', overgrownbat)
            elif fuzzlechance == 2:
                playerhp = playerhp - batattack
                print('your spell failed and the Overgrown Bat attacked dealing', batattack, 'to your hp', playerhp,)
        elif move == 's' or 'skill':
            if user_race == 'g' or user_race == 'goose':
                if race_skill > 0: #skills can only be used a set number of times resulting in it haveing none left
                    print('You use your skill, HONK!')
                    honk = random.randint(-20,30)
                    overgrownbat = overgrownbat - honk
                    print('you honk at the Overgrown dealing a random amount of damage leaving the Overgrown Bat with', overgrownbat)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - batattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Overgrown Bat, he deals', batattack, 'to your hp', playerhp)
            elif user_race == 'h' or user_race == 'human':
                if race_skill > 0:
                    print('You use your skill, Strength of the Weak')
                    overgrownbat = overgrownbat - playerattack*2
                    print('you strike at the Overgrown bat dealing massive damage leaving the Overgrown Bat with', overgrownbat)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - batattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Overgrown Bat, he deals', batattack, 'to your hp', playerhp)
            elif user_race == 'o' or user_race == 'orc':
                if race_skill > 0:
                    print('You use your skill, Warcry')
                    overgrownbat = overgrownbat - playerattack
                    print('you scream at the Overgrown bat allowing you to gain the upper hand and attack for free', overgrownbat)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - batattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Overgrown Bat, he deals', batattack, 'to your hp', playerhp)
            elif user_race == 'e' or user_race == 'elf':
                if race_skill > 0:
                    print('You use your skill, Elven Knowlodge')
                    overgrownbat = overgrownbat - playermagic
                    print('you use your knowlodge of magic to cast a spell without fail to the Overgrown Bat', overgrownbat)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - batattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Overgrown Bat, he deals', batattack, 'to your hp', playerhp)
            elif user_race == 'd' or user_race == 'dragonkin':
                if race_skill > 0:
                    print('You use your skill, Dragons Breath')
                    overgrownbat = overgrownbat - playermagic*2
                    print('you breath fire at the Overgrown Bat dealing massive damage leaving the Overgrown Bat with', overgrownbat)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - batattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Overgrown Bat, she deals', batattack, 'to your hp', playerhp)
        else:
            playerhp = playerhp - batattack
            print('you stand still and get hit by the Overgrown Bat, he deals', batattack, 'to your hp', playerhp)
    if playerhp < 1:
        print('you died...THE END')
        score()
    elif overgrownbat < 1:
        print('you killed the Overgrown Bat')
        storyrightroom()
def leftroomfight():
    playerhp = 100
    greenslime = 15
    playerweapon = 'Sword'
    print('You engage the Little Green Slime')
    print('Your Health', playerhp)
    print('Little Green Slime Health', greenslime)
    global skillcount
    global user_race
    global race_skill
    race_skill = skillcount
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
            if user_race == 'g' or user_race == 'goose':
                if race_skill > 0: #skills can only be used a set number of times resulting in it haveing none left
                    print('You use your skill, HONK!')
                    honk = random.randint(-20,30)
                    greenslime = greenslime - honk
                    print('you honk at the Little Green Slime dealing a random amount of damage leaving the Little Green Slime with', greenslime)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - slimeattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Little Green Slime, she deals', slimeattack, 'to your hp', playerhp)
            elif user_race == 'h' or user_race == 'human':
                if race_skill > 0:
                    print('You use your skill, Strength of the Weak')
                    greenslime = greenslime - playerattack*2
                    print('you strike at the Overgrown bat dealing massive damage leaving the Little Green Slime with', greenslime)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - slimeattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Little Green Slime, she deals', slimeattack, 'to your hp', playerhp)
            elif user_race == 'o' or user_race == 'orc':
                if race_skill > 0:
                    print('You use your skill, Warcry')
                    greenslime = greenslime - playerattack
                    print('you scream at the Little Green Slime allowing you to gain the upper hand and attack for free', greenslime)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - slimeattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Little Green Slime, she deals', slimeattack, 'to your hp', playerhp)
            elif user_race == 'e' or user_race == 'elf':
                if race_skill > 0:
                    print('You use your skill, Elven Knowlodge')
                    greenslime = greenslime - playermagic
                    print('you use your knowlodge of magic to cast a spell without fail to the Little Green Slime', greenslime)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - slimeattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Little Green Slime, she deals', slimeattack, 'to your hp', playerhp)
            elif user_race == 'd' or user_race == 'dragonkin':
                if race_skill > 0:
                    print('You use your skill, Dragons Breath')
                    greenslime = greenslime - playermagic*2
                    print('you breath fire at the Little Green Slime dealing massive damage leaving the Little Green Slime with', greenslime)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - slimeattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Little Green Slime, she deals', slimeattack, 'to your hp', playerhp)
            else:
            playerhp = playerhp - batattack
            print('you stand still and get hit by the Little Green Slime, she deals', slimeattack, 'to your hp', playerhp)
    if playerhp < 1:
        print('you died...THE END')
        score()
    elif greenslime < 1:
        print('you killed the Little Green Slime')
        storyleftroom
                    
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
    global skillcount
    global user_race
    global race_skill
    race_skill = skillcount
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
          if user_race == 'g' or user_race == 'goose':
                if race_skill > 0: #skills can only be used a set number of times resulting in it haveing none left
                    print('You use your skill, HONK!')
                    honk = random.randint(-20,30)
                    goat = goat - honk
                    print('you honk at the Goat dealing a random amount of damage leaving the Goat with', goat)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - goatattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Goat, it deals', goatattack, 'to your hp', playerhp)
            elif user_race == 'h' or user_race == 'human':
                if race_skill > 0:
                    print('You use your skill, Strength of the Weak')
                    goat = goat - playerattack*2
                    print('you strike at the Goat dealing massive damage leaving the Goat with', goat)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - goatattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Goat, it deals', goatattack, 'to your hp', playerhp)
            elif user_race == 'o' or user_race == 'orc':
                if race_skill > 0:
                    print('You use your skill, Warcry')
                    goat = goat - playerattack
                    print('you scream at the Goat allowing you to gain the upper hand and attack for free', goat)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - goatattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Goat, she deals', goatattack, 'to your hp', playerhp)
            elif user_race == 'e' or user_race == 'elf':
                if race_skill > 0:
                    print('You use your skill, Elven Knowlodge')
                    goat = goat - playermagic
                    print('you use your knowlodge of magic to cast a spell without fail to the Goat', goat)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - goatattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Goat, it deals', goatattack, 'to your hp', playerhp)
            elif user_race == 'd' or user_race == 'dragonkin':
                if race_skill > 0:
                    print('You use your skill, Dragons Breath')
                    goat = goat - playermagic*2
                    print('you breath fire at the Goat dealing massive damage leaving the Goat with', goat)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - goatattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Goat, she deals', goatattack, 'to your hp', playerhp)
            
        else:
            playerhp = playerhp - goatattack
            print('you stand still and get hit by the Goat, it deals', goatattack, 'to your hp', playerhp)
    if playerhp < 1:
        print('you died...THE END')
        score()
    elif goat < 1:
        print('you killed the Goat')
        bedchamber()

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
    global skillcount
    global user_race
    global race_skill
    race_skill = skillcount
    while playerhp > 0 and chair > 0:
        playerattack = random.randint(4,8)
        playermagic = random.randint(6,7)
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
            if user_race == 'g' or user_race == 'goose':
                if race_skill > 0: #skills can only be used a set number of times resulting in it haveing none left
                    print('You use your skill, HONK!')
                    honk = random.randint(-20,30)
                    chair = chair - honk
                    print('you honk at the Chair Mimic dealing a random amount of damage leaving the Chair Mimic with', chair)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - chairattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Chair Mimic, it deals', chairattack, 'to your hp', playerhp)
            elif user_race == 'h' or user_race == 'human':
                if race_skill > 0:
                    print('You use your skill, Strength of the Weak')
                    chair = chair - playerattack*2
                    print('you strike at the Chair Mimic dealing massive damage leaving the Chair Mimic with', chair)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - chairattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Chair Mimic, it deals', chairattack, 'to your hp', playerhp)
            elif user_race == 'o' or user_race == 'orc':
                if race_skill > 0:
                    print('You use your skill, Warcry')
                    chair = chair - playerattack
                    print('you scream at the Chair Mimic allowing you to gain the upper hand and attack for free', chair)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - chairattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Goat, she deals', chairattack, 'to your hp', playerhp)
            elif user_race == 'e' or user_race == 'elf':
                if race_skill > 0:
                    print('You use your skill, Elven Knowlodge')
                    chair = chair - playermagic
                    print('you use your knowlodge of magic to cast a spell without fail to the Chair Mimic', chair)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - chairattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Chair Mimic, it deals', chairattack, 'to your hp', playerhp)
            elif user_race == 'd' or user_race == 'dragonkin':
                if race_skill > 0:
                    print('You use your skill, Dragons Breath')
                    chair = chair - playermagic*2
                    print('you breath fire at the Chair Mimic dealing massive damage leaving the Chair Mimic with', chair)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - chairattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Chair Mimic, it deals', chairattack, 'to your hp', playerhp)
        else:
            playerhp = playerhp - chairattack
            print('you stand still and get hit by the Chair Mimic, it deals', chairattack, 'to your hp', playerhp)
    if playerhp < 1:
        print('you died..THE END')
        score()
    elif chair < 1:
        print('you killed the Chair Mimic')
        kitchen()


def bedchamber():
    print('''you look down at the dead goat and wonder if its gonna come back.
Upon entering the room you reach a bed chamber,
at the end is a door''')
    loop = True
    while loop:
        hlook = input('You have some options look [a]round or head to the [d]oor: ').lower()
        if hlook == 'a' or hlook == 'look around':
            print('''You look around the bed chamber, its hard to imagine something this beautiful
being in a dirty old dungeon like this, you look at the bed and notice it is neatly made, you decide to jump on it and rest a bit.''')
        elif hlook == 'd' or hlook == 'door':
            loop = False
            print('''You approach the door and spot a monster!!!
Upon further inspection the monster is a Imp!!! "Oi get out of my room Im playing Blockcraft." he says.
The Imp readys a strange device with lightning sparking off it...''')
            impfight()
        else:
            print('You sit around and do nothing')
            print('.....')
            print('Time to go')


def impfight():
    playerhp = 100
    imp = 20
    playerweapon = 'Sword'
    print('You engage the Imp')
    print('Your Health', playerhp)
    print('Imp Health', imp)
    global skillcount
    global user_race
    global race_skill
    race_skill = skillcount
    while playerhp > 0 and imp > 0:
        playerattack = random.randint(6,8)
        playermagic = random.randint(6,10)
        impattack = random.randint(14,21)
        
        move = input("""Select an action
                        [a]ttack with """ +playerweapon+ """
                        [b]lock the attack
                        [m]agic attack
                        [s]kill
                        """).lower()
        if move == "a" or move == "attack":
            stunchance = random.randint(1,2)
            if stunchance == 1:
                imp = imp - playerattack
                print('you deal', playerattack, 'to the Imp',  imp)
                playerhp = playerhp - impattack
                print('the Imp attacks you dealing', impattack, 'to your', playerhp)
            elif stunchance == 2:
                imp = imp - playerattack
                print('you attack the imp and stun it dealing', playerattack, 'damage, Imp hp', imp)
        elif move == 'b':
            deflectchance = random.randint(1,2)
            if deflectchance == 1:
                imp = imp - playerattack
                print('you deflect the attack, you deal', playerattack, 'to the Imps health', imp)
            elif deflectchance == 2:
                playerhp = playerhp - impattack
                print('you attempt to deflect the attack but fail, he deals', impattack, 'to your hp',playerhp)
        elif move == 'm':
            fuzzlechance = random.randint(1,2)
            if fuzzlechance == 1:
                imp = imp - playermagic
                print('you casted a spell dealing', playermagic, 'to the Imp', imp)
            elif fuzzlechance == 2:
                playerhp = playerhp - impattack
                print('your spell failed and the Imp attacked dealing', impattack, 'to your hp', playerhp,)
        elif move == 's':
             if user_race == 'g' or user_race == 'goose':
                if race_skill > 0: #skills can only be used a set number of times resulting in it haveing none left
                    print('You use your skill, HONK!')
                    honk = random.randint(-20,30)
                    imp = imp - honk
                    print('you honk at the Imp dealing a random amount of damage leaving the Imp with', imp)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - impattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Imp, it deals', impattack, 'to your hp', playerhp)
            elif user_race == 'h' or user_race == 'human':
                if race_skill > 0:
                    print('You use your skill, Strength of the Weak')
                    imp = imp - playerattack*2
                    print('you strike at the Imp dealing massive damage leaving the Imp with', imp)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - impattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Imp, it deals', impattack, 'to your hp', playerhp)
            elif user_race == 'o' or user_race == 'orc':
                if race_skill > 0:
                    print('You use your skill, Warcry')
                    imp = imp - playerattack
                    print('you scream at the Imp allowing you to gain the upper hand and attack for free', imp)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - impattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Imp, it deals', impattack, 'to your hp', playerhp)
            elif user_race == 'e' or user_race == 'elf':
                if race_skill > 0:
                    print('You use your skill, Elven Knowlodge')
                    imp = imp - playermagic
                    print('you use your knowlodge of magic to cast a spell without fail to the Imp', imp)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - impattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Imp, it deals', impattack, 'to your hp', playerhp)
            elif user_race == 'd' or user_race == 'dragonkin':
                if race_skill > 0:
                    print('You use your skill, Dragons Breath')
                    imp = imp - playermagic*2
                    print('you breath fire at the Imp dealing massive damage leaving the Imp with', imp)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - impattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Imp, it deals', impattack, 'to your hp', playerhp)
        else:
            playerhp = playerhp - impattack
            print('you stand still and get hit by the Imp, he deals', impattack, 'to your hp', playerhp)
    if playerhp < 1:
        print('you died...THE END')
        score()
    elif imp < 1:
        print('you killed the Imp')
        bosschamber()


def kitchen():
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
    global skillcount
    global user_race
    global race_skill
    race_skill = skillcount
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
            if user_race == 'g' or user_race == 'goose':
                if race_skill > 0: #skills can only be used a set number of times resulting in it haveing none left
                    print('You use your skill, HONK!')
                    honk = random.randint(-20,30)
                    granny = granny - honk
                    print('you honk at the Gremlin Granny dealing a random amount of damage leaving the Gremlin Granny with', granny)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - granattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Gremlin Granny, she deals', granattack, 'to your hp', playerhp)
            elif user_race == 'h' or user_race == 'human':
                if race_skill > 0:
                    print('You use your skill, Strength of the Weak')
                    granny = granny - playerattack*2
                    print('you strike at the Gremlin Granny dealing massive damage leaving the Gremlin Granny with', granny)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - granattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Gremlin Granny, she deals', granattack, 'to your hp', playerhp)
            elif user_race == 'o' or user_race == 'orc':
                if race_skill > 0:
                    print('You use your skill, Warcry')
                    granny = granny - playerattack
                    print('you scream at the Gremlin Granny allowing you to gain the upper hand and attack for free', granny)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - granattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Gremlin Granny, it deals', granattack, 'to your hp', playerhp)
            elif user_race == 'e' or user_race == 'elf':
                if race_skill > 0:
                    print('You use your skill, Elven Knowlodge')
                    granny = granny - playermagic
                    print('you use your knowlodge of magic to cast a spell without fail to the Gremlin Granny', granny)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - granattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Gremlin Granny, it deals', granattack, 'to your hp', playerhp)
            elif user_race == 'd' or user_race == 'dragonkin':
                if race_skill > 0:
                    print('You use your skill, Dragons Breath')
                    granny = granny - playermagic*2
                    print('you breath fire at the Gremlin Granny dealing massive damage leaving the Gremlin Granny with', granny)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - granattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Gremlin Granny, it deals', granattack, 'to your hp', playerhp)
        else:
            playerhp = playerhp - granattack
            print('you stand still and get hit by the Gremlin Granny, she deals', granattack, 'to your hp', playerhp)
    if playerhp < 1:
        print('you died...THE END')
    elif granny < 1:
        print('you killed the Gremlin Granny')
        bosschamber()
def bosschamber():
    print('''you open the grandoise door and enter, its a massive chamber and inside is a massive pile of gold''')
    loop = True
    while loop:
        hlook = input('You have some options look [a]round, head to the [g]old or check the [d]oor: ').lower()
        if hlook == 'a' or hlook == 'look around':
            loop = False
            print('''You look around the massive chamber and spot a piece of paper on the ground...
you pick it up and read it...
"The L__h _as go__ and d_s_u__ed _ims_lf to fool the s_rface
__ m__t _e s___p__"
The note is smudged and hard to read... You head towards the pile of gold.''')
            bossfight()
        elif hlook == 'd' or hlook == 'door':
            print('''You try to reopen the door but fail, you kick the door a couple of times and still nothing.''')
        elif hlook == 'g' or hlook == 'gold':
            print('''you walk down towards the pile of gold...''')
            loop = False
            bossfight()
        else:
            print('You sit around and do nothing')
            print('.....')
            print('Time to go')


def bossfight():
    playerhp = 100
    dragon = 50
    playerweapon = 'Sword'
    print('''You walk around on the pile of gold when you start to hear light breathing.
You look down and an eye opens... You jump back in panic and a massive Ancient Gold Dragon rises from the pile.''')
    print('You engage the Ancient Gold Dragon')
    print('Your Health', playerhp)
    print('Ancient Gold Dragon Health', dragon)
    global skillcount
    global user_race
    global race_skill
    race_skill = skillcount
    while playerhp > 0 and dragon > 0:
        playerattack = random.randint(3,5)
        playermagic = random.randint(3,12)
        goldattack = random.randint(20,30)
        move = input("""Select an action
                        [a]ttack with """ +playerweapon+ """
                        [b]lock the attack
                        [m]agic attack
                        [s]kill
                        """).lower()
        if move == "a" or move == "attack":
            stunchance = random.randint(1,2)
            if stunchance == 1:
                dragon = dragon - playerattack
                print('you deal', playerattack, 'to the Ancient Gold Dragon',  dragon)
                playerhp = playerhp - goldattack
                print('the Ancient Gold Dragon attacks you dealing', goldattack, 'to your', playerhp)
            elif stunchance == 2:
                dragon = dragon - playerattack
                print('you attack the Ancient Gold Dragon and stun it dealing', playerattack, 'damage, Ancient Gold Dragon hp', dragon)
        elif move == 'b':
            deflectchance = random.randint(1,2)
            if deflectchance == 1:
                dragon = dragon - playerattack
                print('you deflect the attack, you deal', playerattack, 'to the Ancient Gold Dragons health', dragon)
            elif deflectchance == 2:
                playerhp = playerhp - goldattack
                print('you attempt to deflect the attack but fail, he deals', goldattack, 'to your hp',playerhp)
        elif move == 'm':
            fuzzlechance = random.randint(1,2)
            if fuzzlechance == 1:
                dragon = dragon - playermagic
                print('you casted a spell dealing', playermagic, 'to the Ancient Gold Dragon', dragon)
            elif fuzzlechance == 2:
                playerhp = playerhp - goldattack
                print('your spell failed and the Ancient Gold Dragon attacked dealing', goldattack, 'to your hp', playerhp,)
        elif move == 's':
             if user_race == 'g' or user_race == 'goose':
                if race_skill > 0: #skills can only be used a set number of times resulting in it haveing none left
                    print('You use your skill, HONK!')
                    honk = random.randint(-20,30)
                    dragon = dragon - honk
                    print('you honk at the Ancient Gold Dragon dealing a random amount of damage leaving the Ancient Gold Dragon with', dragon)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - goldattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Ancient Gold Dragon, it deals', goldattack, 'to your hp', playerhp)
            elif user_race == 'h' or user_race == 'human':
                if race_skill > 0:
                    print('You use your skill, Strength of the Weak')
                    dragon = dragon - playerattack*2
                    print('you strike at the Ancient Gold Dragon dealing massive damage leaving the Ancient Gold Dragon with', dragon)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - goldattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Ancient Gold Dragon, it deals', goldattack, 'to your hp', playerhp)
            elif user_race == 'o' or user_race == 'orc':
                if race_skill > 0:
                    print('You use your skill, Warcry')
                    dragon = dragon - playerattack
                    print('you scream at the Ancient Gold Dragon allowing you to gain the upper hand and attack for free', dragon)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - goldattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Ancient Gold Dragon, it deals', goldattack, 'to your hp', playerhp)
            elif user_race == 'e' or user_race == 'elf':
                if race_skill > 0:
                    print('You use your skill, Elven Knowlodge')
                    dragon = dragon - playermagic
                    print('you use your knowlodge of magic to cast a spell without fail to the Ancient Gold Dragon', dragon)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - goldattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Ancient Gold Dragon, it deals', goldattack, 'to your hp', playerhp)
            elif user_race == 'd' or user_race == 'dragonkin':
                if race_skill > 0:
                    print('You use your skill, Dragons Breath')
                    dragon = dragon - playermagic*2
                    print('you breath fire at the Ancient Gold Dragon dealing massive damage leaving the Ancient Gold Dragon with', dragon)
                    race_skill = race_skill - 1
                else:
                    playerhp = playerhp - goldattack
                    print('you cannot use that anymore')
                    print('you stand still and get hit by the Ancient Gold Dragon, it deals', goldattack, 'to your hp', playerhp)
        else:
            playerhp = playerhp - goldattack
            print('you stand still and get hit by the Ancient Gold Dragon, he deals', goldattack, 'to your hp', playerhp)
    if playerhp < 1:
        print('you died...THE END')
        score()
    elif dragon < 1:
        print('you defeated the Ancient Gold Dragon')
        ending()
def ending():
    print('''You watch as the Ancient Gold Dragon falls to the ground,
"Please Adventurer, spare my life and I will tell you the truth behind your quest"
The Ancient Gold Dragon says weakly''')
    ending = input('Will you -[s]pare the dragon, or will you [k]ill it to fulfil your quest').lower()
    if ending == 's' or ending == 'spare':
        print('You spare the dragon as it recovers its strength')
        print('"Thank you adventurer, the truth behind your quest is that the man who hired you is an evil lich, together we shall defeat him"')
        print('''You hop on the dragons back and ride it out of the dungeon.
The Strange Man sees this and starts cursing at you, the Ancient Gold Dragon lands on the strange man killing him...
THE END''')
        score()
    elif ending == 'k' or ending == 'kill':
        print('You raise your sword up high and slash down on the dragon...')
        print('You return to the strange old man and recieve the 10 gold pieces')
        print('"HAHAHAHAHAHAHA, you dumb cretin, you absolute bufoon, you fell for my trick" The strange old man says')
        print('''The world is plunged into darkness...
THE END''')
        score()
    else:
        print('''The dragon eats you...
THE END''')
        score()

def score():
    conn = None    
    db_file = "quiz.db"   

    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    c = conn.cursor()
    print('You wake up in a room with a singular chest and open it, it shows information of previous heros, including unique codes')
    c.execute("SELECT rowid,* FROM players")  #showing row id and other fields
    results = c.fetchall()   #you can use fetchone if you want just one result
    conn.commit()

    for i in results:    # this will display the tuples in the list
        print(i)            



#--------Main--------#
user_race = None
race_skill = None
skillcount = None
introduction()
