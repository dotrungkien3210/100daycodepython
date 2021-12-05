import pandas as pd
'''có 2 loại cấu trúc pandas là series và dataframe
dataframe tương đương với 1 table excel có thể chuyển thành định dạng dataframe
series tương đương với một list tức một cột trong table có thể chuyển 1 cột thành định dạng list
kham khảo các hàm tại https://pandas.pydata.org/docs/reference/
'''
#data = pd.read_csv("weather_data.csv")
'''print(data)
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].tolist()
print(temp_list)'''

'''lấy các thành phần cụ thể
print(data[data.day == "Monday"])
print(data[data.temp==data.temp.max()])
lấy ra những ô nhỏ nhất
monday = data[data.day == "Monday"]
print(monday.condition)
'''

'''# xuất thông tin ra csv
data_csv = {
    "students":["amy","jame","angela"],
    "score":[76,56,65]
}
data = pd.DataFrame(data_csv)
data.to_csv("new_data.csv", index=False)'''

data = pd.read_csv("park.csv")
grey_squirrel = len(data[data["Primary Fur Color"]=="Gray"])
print(grey_squirrel)