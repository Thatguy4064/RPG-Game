'''
Author:Israel Flannery
Date:15/09/2020
Description:Story Starter
Version:2.0
'''

#--------Libraries-------#
import sqlite3
from sqlite3 import Error
import random

#------Functions--------#
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
        else:
            print('"Your wasting my time, please answer the question" the strange man says')
def nextroom():
    loopthree = True
    while loopthree:
        progress = input('Would you like to open the door and go to the next room [y]es or [n]o: ').lower()
        if progress == 'y' or progress == 'yes':
            print('you open the door and head into the next room')
            loopthree = False
        elif progress == 'n' or progress == 'no':
            print('You decide to have one more look around the room and find nothing, you head onto the next room')
            loopthree = False
        else:
            print('You think a bit more')

#-------Main------#
story()
