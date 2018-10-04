from random import randint
num = randint(0, 100)
count = 0

while count < 8:
    guess = int(input("Select a number from 0 to 100"))
    count += 1
    if guess in list(range(0,101)):
        if guess == num:
            print("You are correct!")
            break
        if guess < num:
            print("Sorry, your guess is too low")
        else:
            print("Sorry, your guess is too high")
    else:
        print("invalid guess, pick a number from 0 to 100")
        continue


else:
    print("Sorry, no more tries left")
