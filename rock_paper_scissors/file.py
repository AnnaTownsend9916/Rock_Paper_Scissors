import random
#Welcome Message
wins = 0
ties = 0
losses = 0
print("Welcome to the ultimate game of Rock, Paper, Scissors!")
print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))
print("Do you dare to continue?")

#Initalize user, computer choices
computer = random.randint(1,3)
user = int(input("[1] Rock [2] Paper [3] Scissors [9] Quit\n"))
    #Important to remember input is being saved as string by default
    #

#gameplay Loop
while not user == 9:
    #user chose rock
    if user == 1:
        if computer == 1:
            print("Computer chose rock...Tie!")
            ties +=1
        elif computer ==2:
            print("Computer chose paper... Computer is a winner winner chicken dinner")
            losses +=1
        else:
            print("Computer chose scissors...You win this round!")
            wins +=1
    
#user chose paper
    elif user == 2:
        if computer == 1:
            print("Computer chose rock...You are ahead!")
            wins +=1
        elif computer ==2:
            print("Computer chose paper... TIE")
            ties +=1
        else:
            print("Computer chose scissors...Computer wins this round!")
            losses += 1
   
#user chose scissors 
    elif user == 3:
        if computer == 1:
            print("Computer chose rock... Computer laughs at you")
            losses += 1 
        elif computer == 2:
            print("Computer chose paper... Laugh at computer")
            wins =+1
        else:
            print("Computer chose scissors... tieee!")
            ties =+ 1
    else: 
        print("Invalid choice")
    #print updated stats
    print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))

    #prompt user to make another choice
    print("Please choose to continue...")
    #Initalize user, computer choices
    computer = random.randint(1,3)
    user = int(input("[1] Rock [2] Paper [3] Scissors  [9]Quit\n"))

    #Game overrrr, save results
    save_results = (wins, ties, losses)   
