'''
try: tìm trong đoạn code xem có lỗi xuất hiện
except thực hiện điều gì nếu xảy ra lỗi
else: thực hiện nếu không xảy ra lỗi
finally làm dù bất kể có điều gì xảy ra
raise: thực hiện khi một except đã biêt
'''
try:
    file = open("file.txt")
    dict = {"key":"value"}
    print(dict["geget"])
except FileNotFoundError:
    file = open("file.txt","w")
    file.write("some thing")
except KeyError:
    print("this key does not exist")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError(" this error i made")
    file.close()
    print("chay bat ke dieu gi xay ra")