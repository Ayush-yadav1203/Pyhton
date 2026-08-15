'''
Snake Water Gun Game
'''

import random
while(True):
    computer =random.choice([-1,0,1])
    youstr=input("Enter your choice (s,w,g)  ")
    youDict={"s":1,"w":-1,"g":0}
    revdict={1:"Snake",-1:"Water",0:"Gun"}
    if youstr not in youDict:
        print("Invalid choice! Try again.")
        

    you=youDict[youstr]
    print(f"You choose{revdict[you]} and computer choose {revdict[computer]}")
    if(computer==you):
        print("It's Draw !")
    else:
        if(computer==-1 and you==0):
            print("You Lose !")
        elif(computer==-1 and you==1):
            print("You Win !")
        elif(computer==1 and you==-1):
            print("You Lose !")
        elif(computer==1 and you==0):
            print("You Win !")
        elif(computer==0 and you==1):
            print("You Lose !")
        elif(computer==0 and you==-1):
            print("You Win !")
        else:
            print("Something went Wrong !")

    again = input("Do you want to play again? (y/n): ")

    if again.lower() in "abcdefghijklmnopqrstuvwxz":
        print("Game Over!")
        break
