def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here

    if (len(aStr)==1 and aStr!=char):
        return False

    meio = len(aStr)/2
  
    if (char == aStr[meio]):
        return True
    
    elif (char < aStr[len(aStr)/2]):        
        return isIn(char, aStr[:meio])
    
    elif (char > aStr[len(aStr)/2]):
        return isIn(char, aStr[meio:])
    
    else:
        return False
