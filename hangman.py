import random
word = ("hello")
def start ():
    print ('     _________     ')
    print ('     |/      \|    ')
    print ('     |        |    ')
    print ('     |             ')
    print ('     |             ')
    print ('     |             ')
    print ('     |             ')
    print ('     |             ')
    print ('     |             ')
    print ('-----------        ')
def onewrong():
    print ('     _________     ')
    print ('     |/      \|    ')
    print ('     |        |    ')
    print ('     |        O    ')
    print ('     |             ')
    print ('     |             ')
    print ('     |             ')
    print ('     |             ')
    print ('     |             ')
    print ('-----------        ')
def twowrong():
    print ('     _________     ')
    print ('     |/      \|    ')
    print ('     |        |    ')
    print ('     |        O    ')
    print ('     |        |    ')
    print ('     |             ')
    print ('     |             ')
    print ('     |             ')
    print ('     |             ')
    print ('-----------        ')
def threewrong():
    print ('     _________     ')
    print ('     |/      \|    ')
    print ('     |        |    ')
    print ('     |        O    ')
    print ('     |       /|    ')
    print ('     |             ')
    print ('     |             ')
    print ('     |             ')
    print ('     |             ')
    print ('-----------        ')
def fourwrong():
    print ('     _________     ')
    print ('     |/      \|    ')
    print ('     |        |    ')
    print ('     |        O    ')
    print ('     |       /|\   ')
    print ('     |             ')
    print ('     |             ')
    print ('     |             ')
    print ('     |             ')
    print ('-----------        ')
def fivewrong():
    print ('     _________     ')
    print ('     |/      \|    ')
    print ('     |        |    ')
    print ('     |        O    ')
    print ('     |       /|\   ')
    print ('     |       /     ')
    print ('     |             ')
    print ('     |             ')
    print ('     |             ')
    print ('-----------        ')
def dead():
    print ('     _________     ')
    print ('     |/      \|    ')
    print ('     |        |    ')
    print ('     |        O    ')
    print ('     |       /|\   ')
    print ('     |       / \   ')
    print ('     |             ')
    print ('     |             ')
    print ('     |             ')
    print ('-----------        ')

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 6

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for char in word:      

    # see if the character is in the players guesses
        if char in guesses:    
        # print then out the character
            print (char, end='')    

        else:
        # if not found, print a dash
        
            print ("_ ", end='')     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print ("You won")  

    # exit the script
        break   

    # ask the user go guess a character
    guess = input("guess a character:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:
        # turns counter decreases with 1 (now 9)
        turns -= 1
        if turns == 5:
            onewrong()
        if turns == 4:
            twowrong()
        if turns == 3:
            threewrong()
        if turns == 2:
            fourwrong()
        if turns == 1:
            fivewrong()
        if turns == 0:
            dead()
        # print wrong
        print("Wrong")    
        # how many turns are left
        print ("You have", + turns, 'more guesses')
        # if the turns are equal to zero
        if turns == 0:           
        # print ("You Loose")
                print ("You Loose, The Word Was " + word)
                break
