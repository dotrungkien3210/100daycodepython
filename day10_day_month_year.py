def format_name(fname,lname):
    formated_f_name = fname.title()
    formated_l_name = lname.title()
    return f"{formated_f_name} {formated_l_name}"
result = format_name("kien","do")
print(result)
def check_year(year):
    if(year%4==0):
        print("leap year")
    else:
        print("not a leap year")
def day_of_month(month):
    month_day = [31,28,31,30,31,30,31,31,30,31,30,31]
    print(f"thang {month} co {month_day[month-1]} ngay")
year = int(input("nhap vao so nam"))
month = int(input("nhap vao thang"))
check_year(year)
day_of_month(month)