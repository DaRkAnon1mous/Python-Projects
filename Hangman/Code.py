import random
def hangman():

    word = random.choice(["pugger" , "littlepugger" , "tiger" , "superman" , "thor" , "pokemon" , "avengers" , "savewater" , "earth" , "annable" ])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'  ##valid characters that can be guessed by the player.
    turns = 10
    guessmade = ''  ##empty string to keep track of all the letters guessed by the player so far.

    while len(word) > 0:
        main = "" ##used to build the current state of the guessed word.
        missed = 0

        for letter in word:
            if letter in guessmade: ##if the current letter has already been guessed by the player (if it is in guessmade).
                main = main + letter  ##If the letter has been guessed, it is added to the main string.
            else:
                main = main + "_" + " "  ##adds an underscore and a space to the main string to represent an unguessed letter.
        if main == word:
            print(main)
            print("You win!")
            break

        print("Guess the word:" , main) ##showing the current state of guessed letters.
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess   ##If the guess is valid, it is added to the guessmade string.
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break


name = input("Enter your name")
print("Welcome" , name )
print("-------------------")
print("try to guess the word in less than 10 attempts")
hangman()
print()
