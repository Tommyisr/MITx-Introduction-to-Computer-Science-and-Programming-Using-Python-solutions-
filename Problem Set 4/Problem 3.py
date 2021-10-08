def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    dic = hand.copy()
    for char in word:
        if (char not in dic):
            return False
        elif (dic[char] == 0):
            return False
        else:
            dic[char] -= 1

    if word not in wordList:
        return False
    return True