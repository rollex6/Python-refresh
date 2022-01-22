# Hangeman Game

import random

def hangman():
    word = random.choice(['rawlings','rollex', 'stem', 'alex', 'machine', 'gorilla', 'spider', 'python'])
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''
    
    while len(word) > 0:
        main = ''
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main +letter
            else:
                main = main + '_' + ' '
        if main == word:
            print(main)
            print('you win')
            break
        print('guess the word:', main)
        guess = input()

        if guess in validletters:
            guessmade = guessmade + guess
        else:
            print('enter a valid letter')
            guess = input()
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print('9 turns left')
                print('-------')
            if turns == 8:
                print('8 turns left')
                print('-------')
                print('   O   ')
            if turns == 7:
                print('7 turns left')
                print('-------')
                print('   O   ')
                print('   |   ')
            if turns == 6:
                print('6 turns left')
                print('-------')
                print('   O   ')
                print('   |   ')
                print('  /    ')
            if turns == 5:
                print('5 turns left')
                print('-------')
                print('   O   ')
                print('   |   ')
                print('  / \  ')
            if turns == 4:
                print('4 turns left')
                print('-------')
                print(' \ O   ')
                print('   |   ')
                print('  / \  ')
            if turns == 3:
                print('3 turns left')
                print('-------')
                print(' \ O / ')
                print('   |   ')
                print('  / \  ')
            if turns == 2:
                print('2 turns left')
                print('-------')
                print(' \ O /|')
                print('   |   ')
                print('  / \  ')
            if turns == 1:
                print('1 turns left')
                print('last breath counting...be careful')
                print('-------')
                print(' \ O_|/')
                print('   |   ')
                print('  / \  ')
            if turns == 0:
                print('GAME OVER!!')
                print('you let the man die')
                print('-------')
                print('   O_| ')
                print('  /|\  ')
                print('  / \  ')
                break


name = input('Please enter your name ')
print('Welcome', name)
print('------------')
print('Try to enter the word in less han 10 trys')
hangman()
print()