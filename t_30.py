import sys
users = [
    {"id": 17,  "active": False, "langs": ["python", "javascript"]},
    {"id": 156, "active": True,  "langs": ["php"]},
    {"id": 23,  "active": True,  "langs": ["java", "c++"]},
    {"id": 84,  "active": True,  "langs": ["python", "c++"]},
    {"id": 28,  "active": False, "langs": ["java", "php"]},
    {"id": 21,  "active": True,  "langs": ["java", "javascript"]},
    {"id": 55,  "active": True,  "langs": ["python", "c#"]},
    {"id": 88,  "active": True,  "langs": []},
    {"id": 287, "active": False, "langs": ["c++", "c#", "java"]},
    {"id": 481, "active": False, "langs": ["php", "javascript", "python"]},
    {"id": 134, "active": True,  "langs": ["c++", "python"]},
    {"id": 65,  "active": True,  "langs": ["php", "python"]},
]
lang = sys.argv[1]
print(users[0]["langs"][0])
new_list = []
for item in users:
    if item["active"] == 0:
        for item2 in item["langs"]:
            if item2 == lang:
                new_list.append(str(item["id"]))
print(", ".join(new_list))