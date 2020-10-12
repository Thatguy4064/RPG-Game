'''
Author:Israel Flannery
Date:15/09/2020
Description:Introduction+Log in+Character Builder
Version:1.1.1
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
        Welcome to this RPG quiz based game, in this game,
        you will go around and defeat monsters by
        answering questions in order to complete the quest,
        avaliable classes and races will grant special abilities to help you in
        the questions
        ''')
    loop = True
    while loop:
        choice1 = input('Would you like to start a [n]ew game or [c]ontinue a game: ')
        if choice1 == 'n' or choice1 == 'new':
            loop = False
            builder()    
        elif choice1 == 'c' or choice1 == 'continue':
            print('good for you') #temporary response
            loop = False
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
    class_list = ['[W]arrior', '[M]age', '[T]hief', '[A]rcher', '[K]night, [F]armer']
    loop = True
    print("""
            Welcome""",newuser, """to the character builder,
            here you can pick from an available
            race or class to help you in your quest
            """)
    while loop:
        print('Here are the avaliable races') 
        print(race_list)
        user_race = input('''
            please select from one of the races by entering the name or the
            the first letter of the name: 
            ''').lower()
        if user_race == 'g' or user_race == 'goose':
            print('''
                You are a goose, the special ability is Honk,
                Honk allows you to skip a question twice per battle
                ''')
            loop = False
        elif user_race == 'h' or user_race == 'human':
            print('''
                    You are a Human, the special ability is Common Knowledge,
                    Common Knowlodge lets you do double damage when answering
                    a generic question
                    ''')
            loop = False
        elif user_race == 'o' or user_race == 'orc':
            print("""
                    You are an Orc, the special ability is called Warcry,
                    Warcry lets you do damage even if you get the question wrong,
                    this can only be used once per battle
                    """)
            loop = False
        elif user_race == 'e' or user_race == 'elf':
            print("""
                    You are a Elf, the special ability is Elven Knowledge,
                    Elven knowlodge lets you change a question to a generic question
                    once per battle
                    """)
            loop = False
        elif user_race == 'd' or user_race == 'dragonkin':
            print("""
                    You are a Dragonkin, the special ability is Dragonic Foresight
                    Dragonic Foresight lets you once per battle,
                    remove one wrong answer
                    """)
            loop = False
        else:
            loop = True
            print('please input a valid response')
    loop = True
    while loop:
        print('Now that you have your race its time to pick your class, a class will have a passive ability')
        print(class_list)

        user_class = input('''
                            Please select one of the classes by entering its name
                            or the first letter of its name
                            ''').lower()
        if user_class == 'w' or user_class == 'warrior':
            print("""
                        You have chosen the Warrior
                        your passive skill is Fury, Fury lets you do 1 damage on wrong answers
                        """)
            loop = False
        elif user_class == 'm' or user_class == 'mage':
            print("""
                        You have chosen the Mage,
                        your passive skill is Arcane Intelligence,
                        this skill lets you have a higher chance of advanced questions
                        """)
            loop = False
        elif user_class == 't' or user_class == 'thief':
            print("""you have chosen the Thief
                        your passive skill is Steal
                        Steal lets you take an item from the enemy once you defeat them""")
            loop = False
        elif user_class == 'a' or user_class == 'archer':
            print("""
                        you have chosen the Archer
                        your passive skill is Eagle Vision
                        A slight chance to only be 2 answers instead of 3
                        """)
            loop = False
        elif user_class == ('k' or 'knight'):
            print("""
                        you have chosen the Knight
                        your passive skill is Chivalry
                        Chivalry lets you come back after death at 3hp""")
            loop = False
        elif user_class == 'f' or user_class == 'farmer':
            print('''You have chosen the Farmer
                        your passive skill is Fertilize
                        Fertilize lets you steal a small bit of life after each correct answer''')
            loop = False
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
        
    c.execute("SELECT rowid,* FROM players")  #showing row id and other fields
    results = c.fetchall()   #you can use fetchone if you want just one result
    conn.commit()

        #for i in results:    # this will display the tuples in the list
            #print(i)            

      


        


#-------Main------#
introduction() 



