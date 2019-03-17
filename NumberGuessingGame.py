#%%
import random

def guessing_game(guess):
    
    random_number = random.randint(0,100)
    
    print('This is a Guessing Game')
    print('I will think of a number between 1 and 100.')
    print('You will try to guess my number')
    print('If your guess is within 10 of my number, I will say "Warm".')
    print('If it is not, I will say "Cold"')
    print('If your subsequent guesses are closer to the number than your previous guess, I will say "Warmer"')
    print('If they are not, I will say "Colder"')
    print("Let's play!")
             
    num = [0]
    # num stores the guesses

    while True:
        
        guess = int(input("What's my number?"))
    
        if guess < 0 or guess > 100:
            print('Out of bounds!')
            continue
            
        if random_number == guess:
            print(f'Congratulations! You guessed {random_number} in only {len(num)-1} guesses!') 

            break

    # if guess is incorrect, add guess to the list
        num.append(guess)
        
    # when testing the first guess, guesses[-2]==0, which evaluates to False
    # and brings us down to the second section
                  
        if len(num) == 2:
            if abs(random_number-guess) >= 10:
                print('Cold')
                
            else:
                print('Warm')
                  
        else:
            if abs(random_number-guess) > abs(random_number-num[-2]):
                print('Colder')
        
            else:
                print('Warmer')


#%%
guessing_game(31)


#%%



