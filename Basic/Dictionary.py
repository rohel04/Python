# user={
#     "name":"Rohel Shakya",
#     "faculty":"BCA"
# }
# print(user['name'])
# print(user.get('age'))
# user['name']="Rass Shakya"
# print(user['name'])
# user['age']=20
# print(user)

#Excerise

phone=input("Phone: ")
numbers_mapping={
    "1":"One",
    "2":"Two",
    "3":'Three',
    "4":"Four",
    "5":"Five"
}
output=''
for i in phone:
    output+=numbers_mapping.get(i,"!")+' '
print(output)