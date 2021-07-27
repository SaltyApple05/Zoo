import time
print('''
 ██████  ██    ██ ██ ███████ 
██    ██ ██    ██ ██    ███  
██    ██ ██    ██ ██   ███   
██ ▄▄ ██ ██    ██ ██  ███    
 ██████   ██████  ██ ███████ 
    ▀▀
Welcome to the Minecraft quiz! (1.17)
''')
time.sleep(2)
print("\nThis Quiz will have 20 questions the difficulty will be random the score will be out of 100%, you will also recevie a grade!")

# lists
questions_wrong = []
questions_right = []

# var
score = 0
txt = "Please choose from A, B, C or D"

# def
def get_response(error_message):
    while True:
        inpt = input().upper()
        if inpt == "A":
            return inpt
        elif inpt == "B":
            return inpt
        elif inpt == "C":
            return inpt
        elif inpt == "D":
            return inpt
        else:
            print(error_message)

def ask_question(question, error_message, correct):
    global score
    print(question)
    response = get_response(error_message)
    if response == correct:
        score += 1
    
# quiz

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
    ["Whats Minecrafts largest mob?\nA Ravagers\nB Ender Dragon\nC Elder Guardians", txt, 'B'],
    ["Whats Minecraft smallest mob?\nA Silverfish\nB Baby turtle\nC Bat\nD Pufferfish", txt, 'B'],
    ["How many iron ingots do you need for an anvil?\nA 25\nB 31\nC 30\nD 28", txt, 'B'],
    ["What is the name for the nether verison of the slime mob?\nA Magma cube\nB Lava slime\nC Lava cube\nD Magma cream", txt, 'A'],
    ["In a furnace how many items can 1 piece of coal smelt?\nA 10\nB 12\nC 8\nD 6", txt, 'C'],
    ["What is minecrafts rarest mob?\nA Blue Axolotl\nB Zombie with Full Gold Armor\nC Left-handed baby villager chicken jockey that can pick up items, has full diamond gear, each part enchanted at level 8, an iron sword enchanted at the same level\nD Chicken", txt, 'C'],
    ["What biome do Emeralds spawn in?\nA Extreme Hills Biomes\nB Lush Caves\nC Taiga\nD Plains", txt, 'A'],
    ["How many blocks can you fall without dying?\nA 22\nB 15\nC 10\nD 14", txt, 'A'],
    ["How many biome are in minecraft?\nA 41\nB 81\nC 73\nD 100", txt, 'B'],
    ["What is the rarest biome?\nA Badlands\nB Giant Tree Taiga\nC Modified Jungle Edge\nD Mushroom Fields", txt, 'C'],
]
for question, error_message, correct in all_questions:
    ask_question(question, error_message, correct)

# scoring after quiz

percent = (score/20)*100

print(f"You got {percent}%")
if percent == 100:
    print("100% WELL DONE!")
elif percent >= 50:
    print("Well done you passed!")
else:
    print("You failed, please play some Minecraft!")