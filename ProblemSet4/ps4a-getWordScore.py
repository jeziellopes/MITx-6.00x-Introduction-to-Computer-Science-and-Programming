def getWordScoreRecur(word, n):
    if len(word) == n:
        return 50 + len(word)*getWordScore(word, n+1)
    elif len(word) == 0:        
        return 0
    elif len(word) > 0:
        return SCRABBLE_LETTER_VALUES[word[0]] + getWordScore(word[1:],n)
