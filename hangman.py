import random as rand
import string

#Declares variables
#guessed = []
mylines = []
#guesses = 8
#count = 0
#invalid = "Your guess was invalid."

#designates path to txt file and opens it
path = './myWords.txt'
file = open(path, "r")

#Fills list with words from txt file
with file as myfile:
    for myline in myfile:
        mylines.append(myline)
file.close()

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def play_game(my_word):
    #Declares random number, hangword as variable from list, removes all \n so accurate lengths will be returned, and creates hangdisplay variable based on length of random word
    hangword = [char.upper() for char in my_word.replace("\n", "")]
    hangwordlen = len(hangword)

    # Create hanglist with _ or space
    get_char = lambda c: ' ' if c == ' ' else '_'
    hanglist = [get_char(hangword[i]) for i in range(hangwordlen)]

    attempts = []
    count = 0

    while count < len(hangword):
        count += 1

        print('Guess a letter: ', ''.join(hanglist))
        guess = input("Please enter your guess: ").upper()

        # Basic checking of input data
        if len(guess) != 1 or guess.isalpha() != True:
            print('Invalid Input. Try again.')
            continue #restarts the while loop to promt new input

        if guess in attempts:
            print('You have already guessed this!')
            continue #restarts the while loop to promt new input

        if guess not in hangword:
            attempts.append(guess)
            print(guess, ' is not in the word! Try again.')
            continue

        if guess in hangword:
            indexes = find(hangword, guess)
            for i in indexes:
                hanglist[i] = guess
            
            if '_' not in hanglist:
                return 'You won! The word was ' + my_word.upper()
    
    return 'You guessed too many times and lost!'

while True:
    play = input('Play Hangman? (y/n)\n')

    if play == 'n':
        break
    elif play == 'y':
        r = rand.randint(0,len(mylines))
        print(play_game(mylines[r]))
    else:
        print('Invalid Input.')

# #Welcome message
# print("Welcome to hangman!\nTry to guess the letters that make up the hidden word.\nYou can only guess wrong " + str(guesses) + " times so choose wisely.\n" + "Word: " + hangDisplay +"\n")

# #sets amount of mistakes per game
# while count < guesses:
    
#     #Returns valid guess from user
#     i = 0
#     while (i == 0):
#         guess1 = input("Please enter your guess: ")

#         #determines if guess has already been guessed as an uppercase or lowercase letter
#         c = 0
#         guess1 = guess1.upper()
#         if guess1 in guessed:
#             c = c + 1
#         guess1 = guess1.lower()
#         if guess1 in guessed:
#             c = c + 1

#         #If guess has not been guessed
#         if c == 0:

#             #checks if length is invalid
#             if 1 != len(guess1):
#                 print(invalid)
#                 i = 0

#             #checks if length is valid
#             if len(guess1) == 1:

#                 #checks if guess is a letter
#                 if guess1 not in string.ascii_letters:
#                     print(invalid)
#                 if guess1 in string.ascii_letters:
#                     i = i + 1

#         #displays message if guess has been used before
#         else:
#             print("You've already guessed that\n"  + "Guesses: " + str(guessed) + "\n" + hangDisplay + "\n")

#     #Determines if lower case guess is in hangman word and appends character to guess list
#     c = 0
#     guess1 = guess1.lower()
#     if guess1 in hangword:
#         guessed.append(guess1)
#         i = 0
#         c = c + 1

#         #Determines where the guess is located and replaces "_" with it
#         while (i < hangwordlen):
#             if(hangword[i] == guess1):
#                 hangDisplay = hangDisplay[:i] + guess1 + hangDisplay[i + 1:]
#                 i = i + 1
#             else:
#                 i = i + 1

#     #Does the same as previous if statement except for upper case guess
#     guess1 = guess1.upper()
#     if guess1 in hangword:
#         guessed.append(guess1)
#         i = 0
#         c = c + 1
#         while (i < hangwordlen):
#             if(hangword[i] == guess1):
#                 hangDisplay = hangDisplay[:i] + guess1 + hangDisplay[i + 1:]
#                 i = i + 1
#             else:
#                 i = i + 1

#     #Appends list with guess, reduces remaining mistakes, and displays
#     if c == 0:
#         guess1 = guess1.lower()
#         guessed.append(guess1)
#         count = count + 1
#         print("Your guess was wrong. " + str(guesses - count) + " mistakes left.")
#         print("Guesses: " + str(guessed))
#         print(hangDisplay + "\n")

#         #displays losing message if out of guesses
#         if(count == guesses):
#             print("You lost!")
#             print(hangword + " was the word.")
            
#     if c != 0:
#         print("You got it!")
#         print("Guesses: " + str(guessed))
#         print(hangDisplay + "\n")

#     #displays winning message if complete word was guessed
#     if "_" not in hangDisplay:
#         print("You won!")
#         print(hangword)
#         count = guesses
