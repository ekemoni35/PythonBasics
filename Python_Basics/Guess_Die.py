import random

guess_Word = ""
Secrete_Word = ""

#Fxn Generate Random no 1-6
def rolldice():
   global Secrete_Word
   Secrete_Word = str(random.randint(1, 6))
   

#Call Fxn RollDice to generate a random no for player X to guess
rolldice()
print(Secrete_Word)



#Loop & Test Guesses
def PlayGame():
    guessTrial = 0
    for index in range(int(Guess)):
        guess_Word = input ('Guess the Die no: ')
        if guess_Word != Secrete_Word:
            print("Your guess is wrong, try again")
            guessTrial +=1
            if guessTrial == int(Guess):        
                print ("You're out of Guesses.");
            continue
        else:
            print("Hi " + PlayN + ", Congratulations. You're the Winner!!!. The Majic No is: " 
            + Secrete_Word)
        break


try:
        PlayN = input ('Please Enter your useranme: ')
        Guess = int(input('Enter the number of times you want to guess the Die Cast by the Computer: '))
        PlayGame()  
except ValueError as err:
    print("Please Enter a Valid No of Game Entry " )





