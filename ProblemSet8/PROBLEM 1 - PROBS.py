def getSpace3Mounths():
    space = []
    daysList = 'D1 D2 D3 D4 D5 D6 D7 D8 D9 F'.split(' ')
    for i in daysList:
        for j in daysList:
            for k in daysList:
                space.append((i, j, k))
    return space


def getProbs():
    space = getSpace3Mounths()
    flu = 0

    for i in space:
        
        

        '1. He catches the flu in September, October and November.'
        
        #if i[0]=='F' and i[1]=='F' and i[2]=='F':
        #    flu += 1

        '2. He catches the flu in September and then again in November, but not in October.'

        #if i[0]=='F' and i[1]!='F' and i[2]=='F':
        #    flu += 1
        #    print i

        '3. He catches the flu exactly once in the three months from September through November.'
        
        #if i[0]=='F' and i[1]!='F' and i[2]!='F' \
        #or i[0]!='F' and i[1]=='F' and i[2]!='F' \
        #or i[0]!='F' and i[1]!='F' and i[2]=='F':
        #    flu += 1

        '4. He catches the flu in two or more of the three months from September through November.'

        if i[0]=='F' and i[1]=='F' and i[2]!='F' \
        or i[0]=='F' and i[1]!='F' and i[2]=='F' \
        or i[0]!='F' and i[1]=='F' and i[2]=='F' \
        or i[0]=='F' and i[1]=='F' and i[2]=='F':
            flu += 1

    return flu/float(len(space))

print getProbs()
