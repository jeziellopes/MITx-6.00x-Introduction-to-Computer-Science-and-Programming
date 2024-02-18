low = 0
high = 100
ans = (high + low)/2
resp = 'a'

print('Please think of a number between 0 and 100!')

while resp != 'c':

    print('Is your secret number ' + str(ans) + '?')
    resp = (raw_input("Enter 'h' to indicate the guess is too high. "
                  + "Enter 'l' to indicate the guess is too low. "
                  + "Enter 'c' to indicate I guessed correctly. "))

    if resp =='h':
        high = ans
    elif resp == 'l':
        low = ans
    elif resp != 'c':
        print('Sorry, I did not understand your input.')
        
    ans = (high + low)/2
            
print('Game over. Your secret number was: ' + str(ans))
