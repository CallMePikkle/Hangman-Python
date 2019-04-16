import random
from functions import *
word = random.choice(list(open('dict.txt'))).rstrip('\n')
guesses = ''
turns = 6
while turns > 0:         
    failed = 0               
    for char in word:      
        if char in guesses:    
            print (char, end='')    
        else:
            print ("_ ", end='')     
            failed += 1    
    if failed == 0:        
        print ("You won")  
        break   
    guess = input("guess a character:") 
    guesses += guess                    
    if guess not in word:
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
        print("Wrong")    
        print ("You have", + turns, 'more guesses')
        if turns == 0:           
                print ("You Loose, The Word Was " + word)
                break
