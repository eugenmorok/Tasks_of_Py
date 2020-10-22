import sys
users = [
    {"email": "user1@domain.com", "password": "password1"},
    {"email": "user2@domain.com", "password": "abcde"},
    {"email": "user3@domain.com", "password": "123456"},
    {"email": "user4@domain.com", "password": "lovelove"},
    {"email": "user5@domain.com", "password": "kdmUdmk84M"}
]
mail = sys.argv[1].lower()
password = sys.argv[2]

is_user = 0
is_pass = 0

for j in range(len(users)):
    if mail in users[j]["email"]:
        is_user += 1
        if password in users[j]["password"]:
            is_pass += 1

if is_user != 0 and is_pass != 0:
    print ("Доступ открыт")
elif is_user != 0 and is_pass == 0:
    print ("Доступ закрыт")
else:
    print("Пользователь не найден")
