inputText = input("nhap vao doan text muon doan")
countText = len(inputText)
hiddenText = []
for i in range(countText):
    hiddenText.append("_")
print(hiddenText)
timedie = 0
countWord = 0
while(True):
    inputguess = input("nhap vao chu ban doan")
    for index,x in enumerate(inputText):
        if(inputguess==x):
            countWord += 1
            print("found {} in {} ".format(x,index+1))
            hiddenText[index] = inputguess
    print(hiddenText)
    countTrue = 0
    for i in range(len(inputText)):
        if(inputText[i]==hiddenText[i]):
            countTrue += 1
    if (countTrue == len(inputText)):
        print("you win the game")
        break
    if(countWord!=0):
        countWord=0
    else:
        print("khong co ki tu thoa man")
        timedie += 1
        if(timedie==7):
            print("ban da thua game")
            break
        else:
            print("sai {} lan".format(timedie))





