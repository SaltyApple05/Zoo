import time
print('''
 ██████  ██    ██ ██ ███████ 
██    ██ ██    ██ ██    ███  
██    ██ ██    ██ ██   ███   
██ ▄▄ ██ ██    ██ ██  ███    
 ██████   ██████  ██ ███████ 
    ▀▀
Welcome to the Minecraft quiz!
''')
time.sleep(2)
print("\nThis Quiz will have 20 questions the difficulty will be random the score will be out of 100%, you will also recevie a grade!")

# lists
questions_wrong = []
questions_right = []

# score
score = 0

# quiz
Question_1 = input("What year was Minecraft Java Edition released?\nA 2014\nB 2012\nC 2011\nD 2009\nANSWER: ")
if Question_1 == "C":
    score += 1
else:
    print("wrong")
Question_2 = input("What was Minecraft's original name?\nA Minecraft\nB Cave Game\nC Minecraft: Order of the Stone\nD Block World\nANSWER: ")
if Question_2 == "B":
    score += 1
else:
    print("wrong")
Question_3 = input("What was Minecraft's latest update called?\nA Caves & Cliffs\nB Nether Update\nC Buzzy Bees\nD Caves and Cliffs\nANSWER: ")
if Question_3 == "A":
    score += 1
else:
    print("wrong")
Question_4 = input("Who was Minecraft's first Dev?\nA Jens Bergensten\nB Markus Persson\nC Jasper Boerstra\nD Apple\nANSWER: ")
if Question_4 == "B":
    score += 1
else:
    print("wrong")
Question_5 = input("Which update did they not add -Removed Herobrine from the patch notes?\nA The Update That Changed The World\nB Village and Pillage\nC Nether Update\nD The Pretty Scary Update\nANSWER: ")
if Question_5 == "C":
    score += 1
else:
    print("wrong")
Question_6 = input("When was Minecraft brought by a certain company?\nA 2016\nB 2017\nC 2015\nD 2014\nANSWER: ")
if Question_6 == "D":
    score += 1
else:
    print("wrong")
Question_7 = input("How much did this company buy Minecraft for?\nA $2.5 billion\nB $3.2 billion\nC $500 million\nD $1 billion\nANSWER: ")
if Question_7 == "A":
    score += 1
else:
    print("wrong")
Question_8 = input("Who brought Minecraft/Mojang from Notch?\nA Jeb\nB Sony\nC Apple\nD Mircosoft\nANSWER: ")
if Question_8 == "D":
    score += 1
else:
    print("wrong")
Question_9 = input("Which of these Minecraft mobs is the fastest?\nA Horse\nB Silverfish\nC Vindicator\nD Vex\nANSWER: ")
if Question_9 == "D":
    score += 1
else:
    print("wrong")
Question_10 = input("Which of these Minecraft mobs is the slowest?\nA Cow\nB Snow golem\nC Llama\nD Polar bear\nANSWER: ")
if Question_10 == "C":
    score += 1
else:
    print("wrong")
Question_11 = input("Whats Minecrafts largest mob?\nA Ravagers\nB Ender Dragon\nC Elder Guardians\nD Ghasts\nANSWER: ")
if Question_11 == "B":
    score += 1
else:
    print("wrong")
Question_12 = input("Whats Minecraft smallest mob?\nA Silverfish\nB Baby turtle\nC Bat\nD Pufferfish\nANSWER: ")
if Question_12 == "B":
    score += 1
else:
    print("wrong")
Question_13 = input("How many iron ingots do you need for an anvil?\nA 25\nB 31\nC 30\nD 28\nANSWER: ")
if Question_13 == "B":
    score += 1
else:
    print("wrong")
Question_14 = input("What is the name for the nether verison of the slime mob?\nA Magma cube\nB Lava slime\nC Lava cube\nD Magma cream\nANSWER: ")
if Question_14 == "A":
    score += 1
else:
    print("wrong")
Question_15 = input("In a furnace how many items can 1 piece of coal smelt?\nA 10\nB 12\nC 8\nD 6\nANSWER: ")
if Question_15 == "C":
    score += 1
else:
    print("wrong")
Question_16 = input("What is minecrafts rarest mob?\nA Blue Axolotl\nB Zombie with Full Gold Armor\nC Left-handed baby villager chicken jockey that can pick up items, has full diamond gear, each part enchanted at level 8, an iron sword enchanted at the same level\nD Chicken\nANSWER: ")
if Question_16 == "C":
    score += 1
else:
    print("wrong")
Question_17 = input("What biome do Emeralds spawn in?\nA Extreme Hills Biomes\nB Lush Caves\nC Taiga\nD Plains\nANSWER: ")
if Question_17 == "A":
    score += 1
else:
    print("wrong")
Question_18 = input("How many blocks can you fall without dying?\nA 22\nB 15\nC 10\nD 14\nANSWER: ")
if Question_18 == "A":
    score += 1
else:
    print("wrong")
Question_19 = input("How many biome are in minecraft?\nA 41\nB 81\nC 73\nD 100\nANSWER: ")
if Question_19 == "B":
    score += 1
else:
    print("wrong")
Question_20 = input("What is the rarest biome?\nA Badlands\nB Giant Tree Taiga\nC Modified Jungle Edge\nD Mushroom Fields\nANSWER: ")
if Question_20 == "C":
    score += 1
else:
    print("wrong")

# scoring after quiz

if score >= 10:
    print("You passed!")
else:
    print("You failed!")