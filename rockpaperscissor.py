#get one input from computer and one input from user to play rocks paper scissors
import random
    
def displaymessage():
    status=True
    while(status):
        menu()
        yesno=input("Do you wish to play again? Press 'y' for yes and 'n' for no:")
        if yesno=='y':
            status=True
        elif yesno=='n':
            status=False
        else:
            print("Invalid Choice.. Going back to main menu!")

def menu():
    message="WELCOME TO ROCK PAPER SCISSORS"
    print(message.center(100))

    t1="1) Press 1 to PLAY"
    print(t1.center(99))
    t2="2) Press 2 to EXIT"
    print(t2.center(99))
    
    while True:
        choice=int(input("Enter your choice:"))
        if choice==1:
            play()
            break

        elif choice==2:
            exit()
        else:
            print("Invalid choice,enter again!!")

rps=['r','p','s']

def play():
    user1=input("Press 'p' for paper, press 'r' for rock and press 's' for scissors:")
    print("USER 1:",user1)
    user2= random.choice(rps)
    print("(COMPUTER GENERATED) USER 2:",user2)
    print("\n")


    if user1 == 'r':
        if user2 == 'r':
            print("RESULT DRAWN")
        elif user2 == 'p':
            print("PAPER WINS! USER 2 is winner!!!")
        elif user2 == 's':
            print("ROCK WINS! USER 1 is winner!!!")
            
    if user1 == 'p':
        if user2 == 'p':
            print("RESULT DRAWN")
        elif user2 == 'r':
            print("PAPER WINS! USER 1 is winner!!!")
        elif user2 == 's':
            print("SCISSOR WINS! USER 2 is winner!!!")
    
    if user1 == 's':
        if user2 == 's':
            print("RESULT DRAWN")
        elif user2 == 'r':
            print("ROCK WINS! USER 2 is winner!!!")
        elif user2 == 'p':
            print("SCISSOR WINS! USER 1 is winner!!!")
    
 






displaymessage()