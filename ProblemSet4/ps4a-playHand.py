def playHand(hand, wordList, n):

    word = ''
    score = 0
    totalScore = 0
    
    print 'Current Hand:  ',
    displayHand(hand)
    word = raw_input ('Enter word, or a "." to indicate that you are finished: ')

    while (word != '.'):
                                    
        if not isValidWord(word, hand, wordList):
            word = ''
            print 'Invalid word, please try again.'
            break
                
        elif calculateHandlen(hand)>0:
            score = getWordScore(word, calculateHandlen(hand))
            totalScore += score
            hand=updateHand
            print
            print hand
            print
            print word + ' earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points'
            print 'Current Hand:  ', displayHand(hand)
            word = raw_input ('Enter word, or a "." to indicate that you are finished: ')            
        else:
            print 'Run out of letters. Total score: ' + str(totalScore) + ' points.'
            break        
        print 'Goodbye! Total score: ' + str(totalScore) + ' points.'
