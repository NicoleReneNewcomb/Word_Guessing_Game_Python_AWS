#! /usr/bin/env python3.6
#Word guessing game created by Nicole-Rene

import os.path
import random
import string

#Open external txt file containing dictionary words
openFile = open(os.path.join(os.path.dirname(__file__), "8_nounlist.txt"))

#Read file word entries as strings
dictionary = openFile.read()

#Declare dictionary to contain words
dictionaryByLength = dict()

#Group words into dictionary using word lengths as keys
for word in dictionary.split('\n'):
    dictionaryByLength.setdefault(len(word), []).append(word)

#Output game header with instructions  
print()
print()
print("========================================================")
print("This Word Guessing Game is brought to you by Nicole-Rene")
print("========================================================")
print()
print("You may enter a difficulty/word length entry between 3-14")

#Request user input for difficulty/word length
#Checks if value is integer
try:
    userLevel = int(input("\nHow many letters would you like in the word? "))
except:
    print("\nYou must enter a number.")
    userLevel = 0

#Check if entry is numeric and integer in range
while userLevel not in range(3,15):
    try:
        userLevel = int(input("\nPlease enter a number between 3 and 14: "))
    except:
        pass

#Assign number of incorrect guesses allowed before losing
match userLevel:
    case 3 | 4 | 5:
        wrongGuesses = 16

    case 5 | 6 | 7:
        wrongGuesses = 14

    case 8 | 9 | 10:
        wrongGuesses = 10

    case 11 | 12 | 13 | 14:
        wrongGuesses = 8

#Output user's entry and number of incorrect guesses allowed
print("\nYour word will have", userLevel, "letters.")
print("\nYou will lose if you make", wrongGuesses, "wrong guesses.")

#Select secret word based on user's desired difficulty/length
secretWord = random.choice(dictionaryByLength[int(userLevel)])

#Create guessable word template
wordImage = "_" * userLevel

#Create list to hold previous guesses
previousGuesses = '-'

#Create player guess loop
while wrongGuesses > 0:
  if "_" not in wordImage:
      break
  print("\nYou have", wrongGuesses, "wrong guesses left.")
  print("\nHere is the word so far:", wordImage)
  
  #Input validation to ensure user enters single letter
  userCharacter = '-'
  while userCharacter not in string.ascii_lowercase:
    userCharacter = input("\nEnter a letter: ").lower()
    
    #If multiple characters entered, use first one
    if len(userCharacter) > 1:
        userCharacter = userCharacter[0]
    
    #If item entered not a letter, inform user
    if userCharacter not in string.ascii_lowercase:
        print("\nThat didn't seem to be a letter.")

  #If user re-enters previously guessed character  
  if userCharacter in wordImage or userCharacter in previousGuesses:
      print("\nYou've already guessed that letter.")

  #If user character is in secret word
  elif userCharacter in secretWord:
      print("\nCongrats, that letter is in the word!")
      previousGuesses += userCharacter
      
      #Fill in wordImage with guessed character
      #Find multiple instances of characters in word
      charInWord = True

      while charInWord == True:
        charIndex = secretWord.find(userCharacter)
        if charIndex == -1:
          charInWord = False
          continue
        secretWord = secretWord[:charIndex] + '1' + secretWord[charIndex+1:]
        wordImage = wordImage[:charIndex] + userCharacter + wordImage[charIndex+1:]

  #If user character not in secret word
  elif userCharacter not in secretWord:
      print("\nSorry, that letter isn't in the word.")
      previousGuesses += userCharacter
      wrongGuesses -= 1

  else:
      print("\nOops. Something went wrong.")

#If out of guesses, you lose
if wrongGuesses == 0:
    print("\nSorry, you lost this time. Please try again.")
    print(r"""
__   __                     _                  _   
\ \ / /                    | |                | |  
 \ V /   ___   _   _       | |      ___   ___ | |_ 
  \ /   / _ \ | | | |      | |     / _ \ / __|| __|
  | |  | (_) || |_| |      | |____| (_) |\__ \| |_ 
  \_/   \___/  \__,_|      \_____/ \___/ |___/ \__|
                                                           
""")

#If wordImage filled in, you win
elif '_' not in wordImage:
    print("\nCongratulations! You've won!\n")
    print("Your winning word was:", wordImage, "\n")
    print(r"""
 _    _  _                           
| |  | |(_)                          
| |  | | _  _ __   _ __    ___  _ __ 
| |/\| || || '_ \ | '_ \  / _ \| '__|
\  /\  /| || | | || | | ||  __/| |   
 \/  \/ |_||_| |_||_| |_| \___||_|   

                                 
""")