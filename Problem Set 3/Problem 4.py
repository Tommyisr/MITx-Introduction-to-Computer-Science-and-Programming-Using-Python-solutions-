

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    letter_len = len(secretWord)
    attempts = 8
    lettersGuessed = []

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(letter_len) + ' letters long.')

    while attempts != 0 and '_' in getGuessedWord(secretWord, lettersGuessed):
        print('------------')
        print('You have ' + str(attempts) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        question = 'Please guess a letter: '
        c = input(question).lower()
        if c in lettersGuessed:
            print('Oops! You\'ve already guessed that letter: ' + getGuessedWord(secretWord, lettersGuessed))
        elif c in secretWord:
            lettersGuessed.append(c)
            print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))

        else:
            lettersGuessed.append(c)
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
            attempts -= 1

    print('------------')
    if '_' in getGuessedWord(secretWord, lettersGuessed):
        print('Sorry, you ran out of guesses. The word was else.')
    else:
        print('Congratulations, you won!')