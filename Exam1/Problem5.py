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

def generateFormNEW(story, listOfAdjs, listOfNouns, listOfVerbs):
    listStory = story.split()
    listOfLists = [listOfAdjs, listOfNouns, listOfVerbs]
    listTypes = ['[ADJ]', '[NOUN]', '[VERB]']
    for word in listStory:
        for list in listOfLists:
            if word in list:
                listStory[listStory.index(word)] = listTypes[listOfLists.index(list)]
    return ' '.join(i for i in listStory)


print story
print generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)
