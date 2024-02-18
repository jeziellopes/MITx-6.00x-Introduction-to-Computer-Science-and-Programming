story = 'The ravenous zombies started attacking yesterday'
listOfAdjs = ['ravenous']
listOfNouns = ['zombies', 'humans', 'yesterday']
listOfVerbs = ['attacking', 'attacks']

story = 'At the creepy thrift store I found a pair of plaid pants that looked like something your grandpa might wear'
listOfAdjs = ['creepy', 'plaid']
listOfNouns = ['store', 'pants', 'something', 'grandpa']
listOfVerbs = ['found', 'looked']

def generateForm(story, listOfAdjs, listOfNouns, listOfVerbs):
    """
    story: a string containing sentences
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs

    For each word in story that is in one of the lists,
    * replace it with the string '[ADJ]' if the word is in listOfAdjs
    * replace it with the string '[VERB]' if the word is in listOfVerbs
    * replace it with the string '[NOUN]' if the word is in listOfNouns

    returns: string, A Mad-Libs form of the story."""
    
    if story.find(' ') != -1:
        word = story[:story.find(' ')]
        start = story.find(' ')+1
        if word in listOfAdjs:
            return '[ADJ] ' + generateForm(story[start:], listOfAdjs, listOfNouns, listOfVerbs)
        elif word in listOfNouns:
                return '[NOUN] ' + generateForm(story[start:], listOfAdjs, listOfNouns, listOfVerbs)
        elif word in listOfVerbs:
            return '[VERB] ' + generateForm(story[start:], listOfAdjs, listOfNouns, listOfVerbs)
        else:
            return word + ' ' + generateForm(story[start:], listOfAdjs, listOfNouns, listOfVerbs)
    elif story in listOfAdjs:
        return '[ADJ]'
    elif story in listOfNouns:
        return '[NOUN]'
    elif story in listOfVerbs:
        return '[VERB]'
    else:
        return story


def generateForm(story, listOfAdjs, listOfNouns, listOfVerbs):
    """
    story: a string containing sentences
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs

    For each word in story that is in one of the lists,
    * replace it with the string '[ADJ]' if the word is in listOfAdjs
    * replace it with the string '[VERB]' if the word is in listOfVerbs
    * replace it with the string '[NOUN]' if the word is in listOfNouns

    returns: string, A Mad-Libs form of the story."""
    
    if story.find(' ') != -1:
        word = story[:story.find(' ')]
        start = story.find(' ')+1
        if word in listOfAdjs:
            return '[ADJ] ' + generateForm(story[start:], listOfAdjs, listOfNouns, listOfVerbs)
        elif word in listOfNouns:
                return '[NOUN] ' + generateForm(story[start:], listOfAdjs, listOfNouns, listOfVerbs)
        elif word in listOfVerbs:
            return '[VERB] ' + generateForm(story[start:], listOfAdjs, listOfNouns, listOfVerbs)
        else:
            return word + ' ' + generateForm(story[start:], listOfAdjs, listOfNouns, listOfVerbs)
    elif story in listOfAdjs:
        return '[ADJ]'
    elif story in listOfNouns:
        return '[NOUN]'
    elif story in listOfVerbs:
        return '[VERB]'
    else:
        return story

def generateTemplates(madLibsForm):
    """ 
    madLibsForm: string, in a Mad-Lib form. See output of `generateForm`

    returns: a list of '[ADJ]', '[VERB]', and '[NOUN]' strings, in
    the order they appear in the madLibsForm.
    """
    # Your Code Here
    
    listMT = []
    start = madLibsForm.find('[')
    end = madLibsForm.find(']')+1

    while madLibsForm.find('[', start) != -1:
        word = madLibsForm[madLibsForm.find('[', start):madLibsForm.find(']', start)+1]
        if word == '[ADJ]' or word == '[NOUN]' or word == '[VERB]':
            listMT.append(word)
            start = madLibsForm.find('[', end)
            end = madLibsForm.find(']', end)+1
            
    return listMT

def verifyWord(userWord, madTemplate, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    userWord: a string, the word the user inputted
    madTemplate: string, the type of word the user was supposed to input
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs):

    returns: Boolean, whether or not the word is valid
    """
    # Your Code Here
    if madTemplate == '[ADJ]':
        if userWord in listOfAdjs:
            return True
    elif madTemplate == '[VERB]':
        if userWord in listOfVerbs:
            return True
    elif madTemplate == '[NOUN]':
        if userWord in listOfNouns:
            return True
    return False


def generateStoryFromFormAndWords (form, listWords)












