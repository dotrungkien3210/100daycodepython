import random

true_num = random.randrange(1, 100, 1)
def check(num):
    output = False
    if(num==true_num):
        output = True
        print("so ban nhap la chinh xac")
    elif(num>true_num):
        print("so ban nhap dang qua lon")
    else:
        print("so ban nhap dang qua nho")
    return output

while True:
    guess_num = int(input("nhap so ban muon doan"))
    if(check(guess_num)==True):
        break

