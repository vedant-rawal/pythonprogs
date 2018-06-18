import random
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  0   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  0   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  0   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=========''', '''

  +---+
  |   |
 [0   |
 /|\  |
 / \  |
      |
=========''', '''

  +---+
  |   |
 [0]  |
 /|\  |
 / \  |
      |
=========''']

#myStr = 'ant gorilla dinasour bat bear giraffe camel cat cockroach cobra scorpio crocodile crow deer dog donkey duck eagle penguin fox frog goat goose hawk lion lizard mole monkey mouse mule owl panda parrot pigeon python rabbit rat rhino salmon seal shark sheep snake spider swan tiger toad turkey turtle weasel whale wolf zebra tortoise elephant leopard panther'
#words = myStr.split()
words = {'Colors':'red orange yellow green blue indigo violet white black brown magenta'.split(),
         'Shapes':'square triangle rectangle circle ellipse rhombus pentagon hexagon septagon octagon'.split(),
         'Fruits':'apple orange lemon lime pear watermelon grape mango cherry banana strawberry kiwi'.split(),
         'Animals':'ant gorilla dinasour bat bear giraffe camel cat cockroach cobra scorpio crocodile crow deer dog donkey duck eagle penguin fox frog goat goose hawk lion lizard mole monkey mouse mule owl panda parrot pigeon python rabbit rat rhino salmon seal shark sheep snake spider swan tiger toad turkey turtle weasel whale wolf zebra tortoise elephant leopard panther'.split()}

def getRandomWord(wordDict):
    # This function returns a random string from the passed Dictionary of list of strings.
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey])-1)
    return [wordDict[wordKey][wordIndex],wordKey]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range  (len(secretWord)): # replace blanks with correctly guessed letters:
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player
    # entered a single letter, and not something else.
    while True:
        print('Guess a letter: ')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again
    # otherwise it returns false
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord,secretKey = getRandomWord(words)
gameIsDone = False

while True:
    print('The secret word is of ' + secretKey + ' category')
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    #Let the player type in the letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        #check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        #Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter '
                  + str(len(missedLetters)) + ' missed guesses and '
                  + str(len(correctLetters)) +' correct guesses, the word was "'
                  + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord,secretKey = getRandomWord(words)
        else:
            break
