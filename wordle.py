import random
import os

def valid():
    valid = str(guess+'\n') in words
    return valid

os.system("clear")
word = random.randint(1,5757)
line = open('words.txt', 'r')
words = line.readlines()
solution = words[word]
solution = solution[0:-1]
line.close()
guess = input("Enter first guess: ")
game = open("game.html", "r")
out = game.readlines()
game.close()
line = 0
check = valid()
for x in range(5):
    response = []
    while (len(guess) != 5) or (check == False):
        if len(guess) != 5:
            guess = input("Guess must be 5 letters. Please try again: ")
        if (guess in words) == False:
            guess = input("Not a valid word. Please try again: ")
            check = valid()
    for x in range(5):
        gLetter = guess[x]
        sLetter = solution[x]
        if gLetter in solution:
            if gLetter == sLetter:
                out[(line*7)+16+x] = f'        <td><div class="correct">{gLetter}</div></td>'
            else:
                out[(line*7)+16+x] = f'        <td><div class="close">{gLetter}</div></td>'
        else:
            out[(line*7)+16+x] = f'        <td><div class="wrong">{gLetter}</div></td>'
        if x == 4:
            line = line + 1
    game = open("new.html", "w")
    game.writelines(out)
    game.close()
    if guess == solution:
        print("Correct!")
        exit()
    guess = input("Incorrect. Try again: ")
    check = valid()
print(f"You lose. The correct answer was {solution}")
