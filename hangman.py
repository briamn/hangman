import random

#This gets a random word from a file i made
word = random.choice(open('randwords.txt').read().split())

rack = []
board = ['_'] * len(word)

for i in word:
    rack.append(i)

print(rack)
print(board)

count = 0

while board != rack:
    guess = input("Guess a letter: ")

    for i in rack:
        if guess in board and guess == i:
            del board[rack.index(guess, rack.index(guess)+1)]
            board.insert(rack.index(guess, rack.index(guess)+1), guess)
        elif guess == i:
            del board[rack.index(guess)]
            board.insert(rack.index(guess,), guess)
            print(board)
        if board == rack:
            print(' '.join(board))
            print("Congrats you win nice good you did it wow.")
            break
        else:
            continue
