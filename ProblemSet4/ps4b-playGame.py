def playGame(wordList):
    hand = {}
    op = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
    while op != 'e':
        if op == 'n' or op == 'r' and hand != {}:
            if op == 'n':                
                hand = dealHand(HAND_SIZE)
            print
            op2 = raw_input('Enter u to have yourself play, c to have the computer play: ')
            while op2 == 'u' or 'c':
                if op2 == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                    print
                    op = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
                    break
                elif op2 == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                    print
                    op = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
                    break
                else:
                    print 'Invalid command.'
                    print
                    op2 = raw_input('Enter u to have yourself play, c to have the computer play: ')
            
        else:
            if op == 'r' and hand == {}:
                print 'You have not played a hand yet. Please play a new hand first!'
            elif op != 'n':
                print 'Invalid command.'
            print
            op = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
