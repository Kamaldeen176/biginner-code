
import random
guess = random.randint(1, 10)
prompt = "Guess a target number within a range of 0 and 10\n and Let's see you are good at guessing: "
attempts = 0
message = "" 
while attempts < 3:
    message = int(input(prompt))
    
    if (message == guess):
        print("Wow you are a good guesser!!!")
        break
    
    elif (message < guess):
        print("oops!! your number is below the target")
        attempts += 1
        continue
    
    elif message > guess:
        print("oops!! your number is above the target")
        attempts += 1
        continue
if (message != guess) or (message < guess) or (message > guess):
    print("gameover")
        
    
 
    