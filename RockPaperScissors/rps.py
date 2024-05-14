import random
def main():
    print("""\t\tWelcome to Rock Paper Scissor Game
            \t\tSelect Game mode;
            \t\t\t1 - Single Player
            \t\t\t2 - Multi Player
          """)
    while True:    
        gamemode = input("Input 1 OR 2 for either modes, q to exit: ").lower()
        if gamemode == "1" :
            gamemode1()
        elif gamemode == "2":
            gamemode2()
        elif gamemode == "q":
            exit()
        else:
            print("Invalid Value Try again")

def gamemode1():
    answerList = ["rock", "paper", "scissors"]
    print("ROCK........PAPER........SCISSORS")
    score = 0
    pcScore = 0
    while True:
        print("Your POINTS: ", score)
        print("Pc Score: ", pcScore)

        userIO = input("ROCK PAPER SCISSORS pick one, q to quit or m for the main menu: ").lower()
        if userIO == "q":
            exit()
        elif userIO == "m":
            return
        elif userIO not in answerList:
            print("Wrong input, try again or q to exit\n\n")
            continue
        else:
            pcPick = random.choice(answerList)
        
        if userIO == pcPick:
            print("Drawwwwwwww go again")
            continue

        if winalgo(userIO, pcPick) == 1:
            pt = ["A taste of victory", "suck it up", "Haa!!!!", "I like this, thats what winers say"]
            response = random.choice(pt)
            print(f"You winnnnn\n{response}")
            score= score + 1
        else:
            pcScore = pcScore + 1
            pt = ["Cry Loser!!!!!!!!", "It's game over, You suck!!", "try playing chess nerd", 
                  "DO yourself a favour and quit nowm Your embarrassong Yourself", 
                  "Ha! thought you could win? Delusional","Back to square on Loser!!!"]
            response = random.choice(pt)
            print(f"\n{response}\n")


def gamemode2():
    answerList = ["rock", "paper", "scissors"]
    print("ROCK........PAPER........SCISSORS")
    score1 = 0
    score2 = 0
    while True:
        print(f"Player 1 POINTS: {score1} \n Player 2 POINTS {score2}")
        while True:
            userIO1 = input("ROCK PAPER SCISSORS pick one, q to quit or m for the main menu: ").lower()
            if userIO1 == 'q':
                exit()
            elif userIO1 == "m":
                return
            elif userIO1 not in answerList:
                print("Wrong Input Player 1, try again or q to quit")
                continue
            else:
                break
        while True:
            userIO2 = input("ROCK PAPER SCISSORS pick one, q to quit or m for the main menu: ").lower()
            if userIO2 == 'q':
                exit()
            elif userIO2 == "m":
                return
            elif userIO2 not in answerList:
                print("Wrong Input Player 2, try again ot q to quit")
                continue
            else:
                break
        if userIO1 == userIO2:
            print("Drawwwwwwww go again")
            continue
        
        if winalgo(userIO1, userIO2) == 1:
            print("Player 1 wins")
            score1= score1 + 1
        else:
            print("Prayer 2 wins")
            score2= score2 + 1

def winalgo(userIO1, userIO2):
    if userIO1 == "scissors":
        if userIO2 == "paper":
            return 1
        else:
            return 2
    if userIO1 == "paper":
        if userIO2 == "scissors":
            return 2
        else:
            return 1
    if userIO1 == "rock":
        if userIO2 == "paper":
            return 1
        else:
            return 2

if __name__ == "__main__":
    main()