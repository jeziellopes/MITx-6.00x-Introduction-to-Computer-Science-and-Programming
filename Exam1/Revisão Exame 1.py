story = 'The ravenous zombies started attacking yesterday'
listOfAdjs = ['ravenous']
listOfNouns = ['zombies', 'humans', 'yesterday']
listOfVerbs = ['attacking', 'attacks']

story = 'At the creepy thrift store I found a pair of plaid pants that looked like something your grandpa might wear'
listOfAdjs = ['creepy', 'plaid']
listOfNouns = ['store', 'pants', 'something', 'grandpa']
listOfVerbs = ['found', 'looked']

def generateFormNEW(story, listOfAdjs, listOfNouns, listOfVerbs):
    listStory = story.split()
    listOfLists = [listOfAdjs, listOfNouns, listOfVerbs]
    listTypes = ['[ADJ]', '[NOUN]', '[VERB]']
    for word in listStory:
        for list in listOfLists:
            if word in list:
                listStory[listStory.index(word)] = listTypes[listOfLists.index(list)]
    return ' '.join(i for i in listStory)

def generateTemplatesNEW(madLibsForm):
    listMadLib = madLibsForm.split()
    newList = []
    for word in listMadLib:
        if word in ['[ADJ]', '[VERB]', '[NOUN]']:
           newList.append(word)
    return newList

def verifyWordNEW(userWord, madTemplate, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    userWord: a string, the word the user inputted
    madTemplate: string, the type of word the user was supposed to input
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs):

    returns: Boolean, whether or not the word is valid
    """
    listOfTypes = ['[ADJ]', '[VERB]', '[NOUN]']
    listOfLists = [listOfAdjs, listOfVerbs, listOfNouns]
    if madTemplate in ['[ADJ]', '[VERB]', '[NOUN]']:
        if userWord in listOfLists[listOfTypes.index(madTemplate)]:
            return True
    return False
    

print story
print generateFormNEW(story, listOfAdjs, listOfNouns, listOfVerbs)
print
print generateTemplatesNEW(generateFormNEW(story, listOfAdjs, listOfNouns, listOfVerbs))


listOfLists = [listOfAdjs, listOfVerbs, listOfNouns]
listOfTypes = ['[ADJ]', '[VERB]', '[NOUN]']
madTemplate = '[VERB]'

print verifyWordNEW('looked', madTemplate, listOfAdjs, listOfNouns, listOfVerbs)
