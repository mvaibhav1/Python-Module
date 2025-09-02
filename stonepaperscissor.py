'''
-1 for scissor
0 for stone 
1 for paper
'''
import random
computer_commands=[1,0,-1]
computer=random.choice(computer_commands)

my_command ={
    "sc":-1 , "st":0 , "p": 1 }

rev_command= {
    -1 : "Scissor" , 0: "Stone ", 1: "Paper"}
print(''' 
enter 'sc' for scissor
Enter st for stone 
Enter p for paper
             ''')

your_choice =input("Enter your choice  : ")
you=my_command[your_choice]

print(f"You choose {rev_command[you]} \nComputer choose {rev_command[computer]}")
if(you == computer):
    print("It is a Tie..")
else:
    if(you==-1 and computer ==0):
        print("You lose !")
    elif(you== -1 and computer==1):
        print("you win !")   
    elif(you== 0 and computer==-1):
        print("You Win !")    
    elif(you ==0 and computer==1):
        print(" You win !")
    elif(you == 1 and computer==-1):
        print("You Lose !")
    elif(you==1 and computer==0):
        print("You Lose !")
