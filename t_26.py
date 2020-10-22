import sys
products = [
    {"name": "Гречка", "price": 69},
    {"name": "Хлеб", "price": 34},
    {"name": "Молоко", "price": 57},
    {"name": "Яйца", "price": 78},
    {"name": "Рис", "price": 88},
    {"name": "Макароны", "price": 49},
    {"name": "Сахар", "price": 22},
    {"name": "Яблоки", "price": 79},
    {"name": "Картофель", "price": 18},
    {"name": "Свинина", "price": 120},
    {"name": "Масло", "price": 66},
    {"name": "Помидоры", "price": 64}
]
new_list = []
a = int(sys.argv[1])

for j in range(0, len(products)):

    if a - products[j]["price"] >= 0:
        new_list.append(str(products[j]["name"]))
        a = a - products[j]["price"]

    j += 1
new_list = " ".join(new_list)
print(new_list)