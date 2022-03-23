# correct_guess=9
# guess_limit=3
# guess_count=3

# while guess_count>0:
#     guess=input("Guess: ")
#     guess_count-=1
#     if(int(guess) == correct_guess):
#         print("You won the guess!!")
#         break
    
        
correct_guess=8
guess_limit=3
guess_count=0

while guess_count < guess_limit:
    guess=input("Guess: ")
    guess_count+=1
    if(int(guess)==correct_guess):
        print("You won the guess!!!")
        break
else:
    print("Sorry! You are out of guesses")