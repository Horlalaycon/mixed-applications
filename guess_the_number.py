# This is a project developed by devhorla a.k.a Horlalaycon @ Github
import random


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
secret_number = random.randint(0, len(numbers) - 1)
print(secret_number)
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    user_guess = int(input("Enter the secret number\n"))
    guess_count += 1
    if user_guess == secret_number:
        print("you won!!")
        break
    elif guess_count > guess_limit:
        print("sorry guess limit reached")
