import random
#The game of Hi-lo
print('Welcome to Hi-Lo! If you ever want to give up, guess "give up"')
playagain = "Yes" 
while playagain == "Yes" or playagain == "yes":
    hum = "OwO"
    guesses = (int)(0)
    Max = (int)(input("How high should the computer go? "))
    com = random.randint(1, Max)
    playagain = (int)(0)
    while com != hum:
        hum = input("What is your guess? ")
        hum = hum.upper()
        if hum == "GIVE UP": break
        hum = int(hum)
        if hum < com:
            print("Too Low, try again")
        elif hum > com:
            print("Too High, try again")
        guesses += 1
    if hum == com and guesses == 1: print("You Win!\nit took you",guesses,"guess") 
    if hum == com and guesses != 1: print("You Win!\nit took you",guesses,"guesses")
    print(com,"was the correct answer")
    playagain = input("Do you want to play again? ")
print("Thank you for playing!")

