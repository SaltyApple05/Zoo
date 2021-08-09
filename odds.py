import random
import keyboard

red_hair = random.randint(1, 100)
brownblack_hair = random.randint(7, 10)
blonde_hair(3, 100)

print("Welcome to chances!\n")

user_chance = input("Please chosse between red hair (1) brown/black hair (2) blonde (3)\n")
if user_chance == 1:
    print("You have chosen Red Hair please press ENTER to roll the dice")
    
elif user_chance == 2:
    print("You have chosen Brown / Black Hair please press ENTER to roll the dice")
else:
    print("You have chosen Blonde Hair please press ENTER to roll the dice")