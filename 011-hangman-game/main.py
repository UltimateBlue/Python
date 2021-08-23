from random import randint
from random import choice
# from replit import clear
from hangman_art import hangmanLogo, hangmanShow, parts, indexes
from hangman_words import txt


hangTimes = 0

# Function declarations
wordOnScreen = ''
isCompleted = False
stillAlive = True

def init(word):
  global wordOnScreen
  wordOnScreen = wordOnScreen.join('_ ' for c in word)
  print(hangmanLogo+'\n')
  print(hangmanShow+'\n')
  print(wordOnScreen+'\n')

  
def updateWord(word, newChar):
  global wordOnScreen, stillAlive, isCompleted
  placeHolders = wordOnScreen
  i=0
  for c in word:
    # placeHolders = placeHolders.join(c+' ' if c==newChar else wordOnScreen[i]+' ')
    placeHolders = placeHolders[0:i] + (c if c==newChar else wordOnScreen[i]) + placeHolders[i+1:]
    i+=2
  print('\n* ' + placeHolders + ' *')
  if placeHolders != wordOnScreen:
    printSameHangman()
    # guessedWord =''
    # guessedWord = ''.join(c for c in placeHolders.split(' '))
    # if  guessedWord == word:
    if '_' not in placeHolders:
      isCompleted = True
  else:
    printMoreHangman()
    if hangTimes == 6:
      stillAlive = False
  wordOnScreen = placeHolders
    

def printSameHangman():
  print('Correct!')
  print(hangmanShow)

def printMoreHangman():
  global hangTimes, hangmanShow,stillAlive
  print('Incorrect!')
  hangmanShow = hangmanShow[0: indexes[hangTimes]] + parts[hangTimes] + hangmanShow[indexes[hangTimes]+1:]
  hangTimes+=1
  print(hangmanShow)

newTxt = ''.join(e for e in txt if (e.isalnum() or e==' '))

words = newTxt.split(" ")
# index = randint(0,len(words))
# randomWord = words[index]
randomWord = choice(words)
init(randomWord)
# print(newTxt + '\n' + randomWord)
# print(randomWord)

# while all the words are determined

while ((not isCompleted) and stillAlive):
  playerGuess = input('Guess a character: ').lower()
  updateWord(randomWord , playerGuess)
  # clear()
if isCompleted: 
  print('You Win!')
elif (not stillAlive):
  print('You loose!')