sentence ="today  and tomorrow is all good day"
split = {word:len(word) for word in sentence.split()}
print(split)

weather = {
    "mon":24,
    "tue":33,
    "wed":87,
    "thus":54,
    "fri":36,
    "sat":95,
    "sun":48,
}

weather_dict = {day:tem*9.5+32 for(day,tem) in weather.items()}
print(weather_dict)

import random

names = ["alex","Beth","caroline","dave","eleanor","freddie"]
student_score = {student:random.randint(1,100) for student in names}
print(student_score)
pass_student = {student:score for (student,score) in student_score.items() if score > 60}
print(pass_student)
# for loop trong bình thường
student_dict = {
    "student":["angela","addy","nobia"],
    "score":[56,76,98]
}
print(student_dict)
for (key,value) in student_dict.items():
    print(key)
    print(value)

# làm việc với dataframe for liên tiếp giữa các cột
import pandas
student_data_frame = pandas.DataFrame(student_dict)
for (key,value) in student_data_frame.items():
    print(key)
    print(value)
#dataframe for liên tiếp giữa các hàng
for (index,row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)