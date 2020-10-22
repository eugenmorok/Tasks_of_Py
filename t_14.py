users = [
    {"id": 17, "first_name": "Дмитрий", "last_name": "Иванов", "lang": "python"},
    {"id": 156, "first_name": "Виктор", "last_name": "Осипов", "lang": "php"},
    {"id": 23, "first_name": "Алёна", "last_name": "Гордеева", "lang": "java"},
    {"id": 84, "first_name": "Семён", "last_name": "Васильев", "lang": "python"},
    {"id": 21, "first_name": "София", "last_name": "Зинько", "lang": "java"},
    {"id": 55, "first_name": "Антон", "last_name": "Ватутин", "lang": "python"},
    {"id": 287, "first_name": "Виталий", "last_name": "Новиков", "lang": "c++"}
]
import sys
in_lan = sys.argv[1]

#print(users[0]["lang"])

i = 0

while True:
    if users[i]["lang"] == in_lan:
        break
    i = i + 1
print("{1} {0}".format(users[i]["last_name"], users[i]["first_name"]))