users = [
    {"id": 17,  "lang": "python", "active": False},
    {"id": 156, "lang": "php",    "active": True},
    {"id": 23,  "lang": "java",   "active": True},
    {"id": 84,  "lang": "python", "active": True},
    {"id": 21,  "lang": "java",   "active": False},
    {"id": 55,  "lang": "python", "active": True},
    {"id": 88,  "lang": "python", "active": True},
    {"id": 287, "lang": "c++",    "active": False},
    {"id": 481, "lang": "php",    "active": False},
    {"id": 134, "lang": "c++",    "active": True}
]
import sys
in_lang = sys.argv[1]
i = 0
while True:
    if users[i]["lang"] == in_lang and users[i]["active"] == True:
        break
    i += 1
print(users[i]["id"])