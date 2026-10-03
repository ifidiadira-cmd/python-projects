import random
#imported so that the number is actually random each time
name = input('What is your name?: ')
print('Great! Hello '+name+'! Welcome to Guess the Secret Number!')
print('The game is simple.\nI have picked a number between 1 and 20\nTry and guess it!')

play_again = 'Y'
#to ensure that as long as play_again is Y the game continues
while play_again == 'Y':
    secret_number = random.randint(1, 20)
    attempts = 0
    guess = None
    max_attempts = 5
    #restricts the number of tries but it also means the minimum score is really 15
    while guess != secret_number and attempts < max_attempts:
        #While the guess is not the secret number AND the attempts is less than 5, loop continues
        guess = int(input('Enter your guess: '))
        attempts += 1
        #Each loop increases attempts by 1
        if guess < secret_number:
            print('Too low, try again')
        elif guess > secret_number:
            print('Too high, try again')
        if guess == secret_number:
            print('Congratulations! You got it!')
        
        if guess != secret_number and attempts == max_attempts:
            print('Womp Womp. Game Over. The secret number was', secret_number)
        
    score = max(1, 20 - attempts)
    #Gives a socre no matter what, ensures pity points as well
    print('Your score is: %d' % score)
    #Tells te user wat their score was
    print('The secret number was %d' % secret_number)
    #tells the user what the secret number was
    print('Attempts: %d' % attempts)
    #tells the user the number of attempts
    play_again = input('Play again? (Y/N): ')
    #This will ask the user if they want to play again and updates the variable play_again to determine if loop restarts 

print('Thanks for playing '+name+ ' and Goodbye!')
