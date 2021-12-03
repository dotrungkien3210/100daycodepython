print("welcome to the tip calculator")
total_bill = float(input("what was the total bill"))
per_tip = int(input("what percentage tip would you like to give 10,12,15"))
people = int(input("how many people to split"))
money_per =total_bill*(100+per_tip)/100/people
round(money_per,2)# làm tròn đến 2 số sau thập phân
print("money per people: "+str(money_per))
print(f"each person pay {money_per} very easy")
