from random import randint

print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!\n")

attempts = 0
n = randint(1,99)

while 1:
    guess = input("What's your guess between 1 and 99?\n")
    attempts += 1
    if guess.isnumeric():
        x = int(guess)
        if x < 1 or x > 99:
            print("That number is not in the range.")
        else:
            if x == n:
                if (n == 42):
                    print("The answer to the ultimate question of life, the universe and everything is 42.")
                if (attempts == 1):
                    print("Congratulations! You've got it on your first try!")
                else:
                    print("Congratulations, you've got it!\nYou won in %d attempts!" %(attempts))
                break
            elif x < n:
                print("Too Low!")
            else:
                print("Too high!")
    else:
        if guess == "exit":
            print("Goodbye!")
            break
        else:
            print("That's not a number.")
