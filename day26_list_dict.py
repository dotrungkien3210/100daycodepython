numbers=[1,2,3]
new = [num*2 for num in numbers]
print(new)
name = "do trung kien"
letter = [word for word in name]
print(letter)
names = ["alex","Beth","caroline","eleanor","freddie"]
short_name = [name for name in names if(len(name)<5)]
print(short_name)

'''with open("file1.txt") as file1:
    file1_data = file1.readline()
with open("file2.txt") as file2:
    file2_data = file2.readline()
result = [int(num) for num in file1_data if num in file2_data]'''

#tương tự với dictionary
