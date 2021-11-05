
import random
number = random.randint(1, 100)

while True:
    guess_number = int(input("Can you guess the number? Enter  it: "))

    if guess_number > number:
        guess_number = print(("You need to guess better. Decrease your number and enter it again:"))
    elif guess_number < number:
        guess_number = print(("You need to guess better. Increase your number and enter it again:"))
    else:
        print("Your prediction is true!")
        break

