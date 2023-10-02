name = "Yosef"
age = 18
money = 450.5
happy  = True

person =  ["yosef", 18, 450.5, True]

# Dictionary (Hash Table)

# person = {'name':'yosef', 'age': 20,'money':450.5, 'happy' : False}
# person1 = {'name':'mohamed', 'age': 21,'money':300.5, 'happy' : True} 
# person2 = {'name':'ahmed', 'age': 18,'money':200.5, 'happy' : True} Or


persons = [{'name':'yosef', 'age': 20,'money':450.5, 'happy' : False},
           {'name':'mohamed', 'age': 21,'money':300.5, 'happy' : True},
            {'name':'ahmed', 'age': 18,'money':200.5, 'happy' : True}]
for index in range(0, len(persons)):
    print(persons[index]['name'])
    print(persons[index]['age'])

# print(person['name'])

# person['name'] = 'Mohamed'

# print(person['name'])