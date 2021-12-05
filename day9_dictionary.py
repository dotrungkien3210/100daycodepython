studen_score = {
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62,
}
# dictionary gồm key và value
for student in studen_score:
    print(student)
for student in studen_score:
    print(studen_score[student])
''' value có thể là list cũng có thể là dictionary luôn gọi là NEST
vd {
key1:[list], 
key2:{dictionary},
 }
 '''
travel = {
    "France":["Paris","Lille","Dịjio"],
    "Capitals":{"France":"Paris","Germany":"Berlin"}
}
print(travel)
'''tuy nhiên ta phải tổ chức sao cho khoa học và đễ trích xuất thông tin hơn
đây là list nằm trong dictionary'''
travel_log = {
    "France":{"city_visited":["Paris","Lille","Dịjio"],"total_visits":12},
    "Germany":{"city_visited":["Berlin","Hamburg","Stuttgart"],"total_visits":5}
}
print(travel_log)
'''dưới này là dictionary nằm trong list'''

travel_log = [
    {"Country":"France",
     "city_visited":["Paris","Lille","Dịjio"],
     "total_visits":12
     },
     {"Country":"Germany",
      "city_visited":["Berlin","Hamburg","Stuttgart"],
      "total_visits":5
      }
]
print(travel_log)
def add_new(country_visited,time_visited,cities_visited):
    new_country = {}
    new_country["Country"] = country_visited
    new_country["city_visited"] =cities_visited
    new_country["total_visits"]= time_visited
    travel_log.append(new_country)
add_new("Russia",2,["moscow","saint petecbua"])
print(travel_log)
