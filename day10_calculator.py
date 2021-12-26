

def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def divide(a,b):
    return a/b
num1 = int(input("nhap vao so nguyen 1"))
num2 = int(input("nhap vao so nguyen 2"))
calc = input("nhap vao phep tinh ( + - * / )")
if(calc=="+"):
    result = add(num1,num2)
elif(calc=="-"):
    result = minus(num1,num2)
elif(calc=="*"):
    result = multiplication(num1,num2)
elif(calc=="/"):
    result = divide(num1,num2)
else:
    print("khong thoa man")
print(result)