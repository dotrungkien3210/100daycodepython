alphabet =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def shiftword(inputWord,numShift):
    for index,word in enumerate(alphabet):
        if(inputWord==alphabet[index]):
            i = index+numShift
    return alphabet[i]

print(shiftword('b',5))