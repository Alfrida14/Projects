import random

num=random.randint(1,10)
guess=None
attempts=0


while guess !=num:
    guess=int(input("Enter a Number between 1 to 10:"))
    attempts+=1
    
    if num>guess:
        print("Oops!, Number is Too High.")
    
    elif num<guess:
        print("LOL!, Number is Too Low.")
    
    else:
        print(f"Congrats!, You Guessed it Correct in {attempts} attempts.")
       

