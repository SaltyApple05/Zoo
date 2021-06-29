import time
print('''
 ██████  ██    ██ ██ ███████ 
██    ██ ██    ██ ██    ███  
██    ██ ██    ██ ██   ███   
██ ▄▄ ██ ██    ██ ██  ███    
 ██████   ██████  ██ ███████ 
    ▀▀
Welcome to the video game quiz!
''')
time.sleep(2)
print("\nThis Quiz will have 20 questions the difficulty will be random the score will be out of 100%, you will also recevie a grade!")

# lists
questions_wrong = []
questions_right = []

# quiz
Question_1 = input("What year was Minecraft Java Edition released?\nA 2014\nB 2012\nC 2011\nD 2009\nANSWER: ")
Question_2 = input("What was Minecraft's original name?\nA Minecraft\nB Cave Game\nC Minecraft: Order of the Stone\nD Block World\nANSWER: ")