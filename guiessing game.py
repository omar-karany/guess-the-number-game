import random

#start the game "welcome" the user and explain the game
user_name = input("enter your name please: ")
print(f"welcome {user_name} to guessing number game")


#count attempts and score by minumum attempts
attempts_count = []
attempts = 0

def score_count():
    if not attempts_count:
        print("there is no high score yet")
       
    else: print(f"the high score in game is after {min(attempts_count)} attempts")


#make pc choose random number
pc_number = random.randint(1, 10)


#ask user to input number and make if conditions to compare user and pc number
while True: 
    try:
        user_number = int(input("pick a number in range '1 to 10' "))
        attempts +=1
    
        if user_number >10 or user_number <1: 
          raise ValueError(f"invalid value! {user_name} please try again")
        
        elif pc_number > user_number :
           print("your number too low")
        elif pc_number < user_number:
           print("your number too high")


        
        if user_number == pc_number:
           attempts_count.append(attempts)
           print(f"you win '{user_name}' after {attempts} attempts")
           ask = input("you want to continue game? answer y or n ")
           if ask.lower == "n":
              score_count()
              print(f"good bye {user_name}")
              exit()
        
           else: 
              attempts = 0
              pc_number = random.randint(1, 10)
              continue

    except ValueError as err:
       print(err)






