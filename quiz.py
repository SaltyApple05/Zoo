# importing time for the countdown and loading, os for clearing the screen to make quiz easier to read importing random for loading time
import time
import os
import random

# 1st Title
print('''
 ██████  ██    ██ ██ ███████ 
██    ██ ██    ██ ██    ███  
██    ██ ██    ██ ██   ███   
██ ▄▄ ██ ██    ██ ██  ███    
 ██████   ██████  ██ ███████ 
    ▀▀
Welcome to the Minecraft quiz! (1.17)
''')

# A countdown to start the quiz
time.sleep(1)
print("Ready")
time.sleep(1)
print("Set")
time.sleep(1)
print("Go!")
time.sleep(0.5)

# 2nd Title
print("\nThis Quiz will have 20 questions the difficulty will be random the score will be out of 100%, you will also recevie a grade!")

# Making lists for storing answers
questions_wrong = []
user_answer = []

# Making Varibles for grading loading time and loading bar
score = 0
txt = "Please choose from A, B, C or D" # A shortcut varible
loading = 0
loading_time = random.randint(1, 2)
loadingbar = "."

# def for checking answers and getting a valid input
def get_response(error_message):
    global user_answer
    while True:
        inpt = input().upper()
        if inpt in "ABCD" and len(inpt) == 1:
            user_answer.append(inpt)
            return inpt
        else:
            print(error_message)

# def for asking the user a question checking the input and adding score and adding wrong and right answers to the lists above
def ask_question(question, error_message, correct, question_number):
    global score
    global questions_wrong
    print(question)
    response = get_response(error_message)
    if response == correct:
        score += 1
    else:
        questions_wrong.append(question_number)

#def for checking that the input they give for getting their grade is valid
def get_yes_or_no():
    while True:
            inpt = input("Would you like to know what you got wrong?\n").upper()
            if inpt.isalpha():
                if inpt == "YES" or inpt == "NO":
                    return inpt
            else:
                print("Please enter yes or no ")

    
# the full list of questions for the quiz

all_questions = [
    ["What year was Minecraft Java Edition released?\nA 2014\nB 2012\nC 2011\nD 2009", txt, 'C'],
    ["What was Minecraft's original name?\nA Minecraft\nB Cave Game\nC Minecraft: Order of the Stone\nD Block World", txt, 'B'],
    ["What was Minecraft's latest update called?\nA Caves & Cliffs\nB Nether Update\nC Buzzy Bees\nD Caves and Cliffs", txt, 'A'],
    ["Who was Minecraft's first Dev?\nA Jens Bergensten\nB Markus Persson\nC Jasper Boerstra\nD Apple", txt,'B'],
    ["Which update did they not add -Removed Herobrine from the patch notes?\nA The Update That Changed The World\nB Village and Pillage\nC Nether Update\nD The Pretty Scary Update", txt,'C'],
    ["When was Minecraft brought by a certain company?\nA 2016\nB 2017\nC 2015\nD 2014", txt, 'D'],
    ["How much did this company buy Minecraft for?\nA $2.5 billion\nB $3.2 billion\nC $500 million\nD $1 billion", txt, 'A'],
    ["Who brought Minecraft/Mojang from Notch?\nA Jeb\nB Sony\nC Apple\nD Mircosoft", txt, 'D'],
    ["Which of these Minecraft mobs is the fastest?\nA Horse\nB Silverfish\nC Vindicator\nD Vex", txt, 'D'],
    ["Which of these Minecraft mobs is the slowest?\nA Cow\nB Snow golem\nC Llama\nD Polar bear", txt, 'C'],
    ["Whats Minecrafts largest mob?\nA Ravagers\nB Ender Dragon\nC Elder Guardians\nD Sheep", txt, 'B'],
    ["Whats Minecraft smallest mob?\nA Silverfish\nB Baby turtle\nC Bat\nD Pufferfish", txt, 'B'],
    ["How many iron ingots do you need for an anvil?\nA 25\nB 31\nC 30\nD 28", txt, 'B'],
    ["What is the name for the nether verison of the slime mob?\nA Magma cube\nB Lava slime\nC Lava cube\nD Magma cream", txt, 'A'],
    ["In a furnace how many items can 1 piece of coal smelt?\nA 10\nB 12\nC 8\nD 6", txt, 'C'],
    ["What is minecrafts rarest mob?\nA Blue Axolotl\nB Zombie with Full Gold Armor\nC Left-handed baby villager chicken jockey that can pick up items, has full diamond gear, each part enchanted at level 8, an iron sword enchanted at the same level\nD Chicken", txt, 'C'],
    ["What biome do Emeralds spawn in?\nA Extreme Hills Biomes\nB Lush Caves\nC Taiga\nD Plains", txt, 'A'],
    ["How many blocks can you fall without dying?\nA 23\nB 15\nC 20\nD 14", txt, 'A'],
    ["How many biome are in minecraft?\nA 41\nB 81\nC 73\nD 100", txt, 'B'],
    ["What is the rarest biome?\nA Badlands\nB Giant Tree Taiga\nC Modified Jungle Edge\nD Mushroom Fields", txt, 'C'],
]
# the quiz
question_number = 0
for question, error_message, correct in all_questions:
    ask_question(question, error_message, correct, question_number)
    question_number += 1

# loading text and loading time for user to have a short break
print("Please wait calculating results")
time.sleep(1.5)
while loading != loading_time:
    os.system("clear")
    print("Loading")
    time.sleep(0.5)
    os.system("clear")
    print("Loading"+loadingbar*1)
    time.sleep(0.5)
    os.system("clear")
    print("Loading"+loadingbar*2)
    time.sleep(0.5)
    os.system("clear")
    print("Loading"+loadingbar*3)
    time.sleep(0.5)
    loading += 1
os.system("clear")

# turing the percent of score into a grade
percent = (score/20)*100
# a = 100 ~ 90 b = 89 ~ 80 c = 79 ~ 70 d = 69 ~ 60 e = 59 ~ 50 f = 49 ~ 0 - Gradeing
if percent >= 90:
   grade = "A"
elif 80 <= percent <= 89:
    grade = "B"
elif 70 <= percent <= 79:
    grade = "C"
elif 60 <= percent <= 69:
    grade = "D"
elif 50 <= percent <= 59:
    grade = "E"
else:
    grade = "F"

# showing user results
print(f"You got {percent}%!\nYour Grade is :{grade}")
if percent == 100:
    print("100% WELL DONE!")
elif percent >= 50:
    print("Well done you passed!")
else:
    print("You failed, please play some Minecraft!")

# asking if they want to know if they got certain questions wrong
askgrade = get_yes_or_no()
if askgrade == "YES":
    os.system("clear")
    if percent == 100:
        print("Well done you didnt get a single question wrong!")
    elif percent != 100:
        for i in questions_wrong:
            print(all_questions[i][0] + "\nYour answer was " + user_answer[i] + "\nThe real answer is " + all_questions[i][2] + "\n")
else:
    print("Okay")