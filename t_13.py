users = [
    {"id": 17, "first_name": "Дмитрий", "last_name": "Иванов"},
    {"id": 156, "first_name": "Виктор", "last_name": "Осипов"},
    {"id": 23, "first_name": "Алёна", "last_name": "Гордеева"},
    {"id": 84, "first_name": "Семён", "last_name": "Васильев"},
    {"id": 21, "first_name": "София", "last_name": "Зинько"},
    {"id": 55, "first_name": "Антон", "last_name": "Ватутин"},
    {"id": 287, "first_name": "Виталий", "last_name": "Новиков"}
]

import sys
name_id = int(sys.argv[1])

i = 0

while i < len(users):
    if users[i]["id"] == name_id:
        break
    else:
        i = i + 1
        print(users[i]["first_name"] + ' ' + users[i]["last_name"])