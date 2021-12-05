from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux
    else:
        _ = system('clear')

bid = {}
continue_bid = True


while continue_bid:
    name = input("nhap vao ten cua ban")
    price = input("nhap vao muc gia ban mong muon")
    bid[name] = price
    flag =  input("are any more bid yes/no")
    if(flag=="no"):
        continue_bid = False
    elif(flag=="yes"):
        clear()


