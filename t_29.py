import sys
users = [
    {"id": 17,  "lang": "python", "active": False},
    {"id": 156, "lang": "php",    "active": True},
    {"id": 23,  "lang": "java",   "active": True},
    {"id": 84,  "lang": "python", "active": True},
    {"id": 28,  "lang": "java",   "active": False},
    {"id": 21,  "lang": "java",   "active": True},
    {"id": 55,  "lang": "python", "active": True},
    {"id": 88,  "lang": "python", "active": True},
    {"id": 287, "lang": "c++",    "active": False},
    {"id": 481, "lang": "php",    "active": False},
    {"id": 134, "lang": "c++",    "active": True},
    {"id": 65, "lang": "php",    "active": True},
]
lang = sys.argv[1]
list = []
for item in users:
    if item["active"] == 1 and item["lang"] == lang:
        list.append(item["id"])
list.sort()
list = [str(i) for i in list]
print(", ".join(list))

