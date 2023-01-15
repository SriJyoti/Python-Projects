#Step 1 
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# import os

def matchFunc(aim,guess,hidden):
    for i in range(0,len(aim)):
        if guess==aim[i]:
            hidden[i]=guess
    return hidden

from hangman_words import word_list

# Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

SpaceList=[] #tostore the blanks
repeatavoid=[] # to check the repetation
lives=7
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word=random.choice(word_list)
# print(chosen_word)
for char in chosen_word:
    SpaceList.append("-")
# blank_list = ''.join([str(elem) for elem in SpaceList])
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess=input("Guess a letter\n").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
matchdOutput=[]
while lives > 0 :
    # os.system('cls' if os.name == 'nt' else 'clear')
    # currentString = "".join(SpaceList)
    print("".join(SpaceList) + "    Chances left : " + str(lives))
    guess=input("Guess a letter : ").lower()
    if guess in repeatavoid:
        print("This letter has already been entered")
        continue
    else:
        repeatavoid.append(guess)
    if guess in chosen_word:
        matchdOutput=matchFunc(chosen_word,guess,SpaceList)
        if "-" not in matchdOutput:
            break
    else:
        from hangman_art import stages
        print(stages[lives-1])
        print(f" '{guess}' is not in the word")
        lives -= 1
if "-" not in matchdOutput and lives!=0:
    print(f"You Win, you guessed the word '{chosen_word}' ")
elif lives==0:
    print(f"You lost, the word was: {chosen_word}")







