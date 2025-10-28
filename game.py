import random
num = random.randint(1, 10)
n=3
while n>0:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == num:
        print("Congratulations! You guessed the number.")
        break
    else:
        n -= 1
        print(f"Wrong guess. You have {n} tries left.")
        
print(f"The number was {num}.")