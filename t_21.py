import sys
values = sys.argv[1:]
print(values)
new_values = []
m = "null"
j = 0

for item in values:
    if item == "null":
        print(m)
        j += 1
        new_values.append(m)
    elif item != 'null':
        print(item)
        m = values[j]
        j += 1
        new_values.append(item)
    else:
        break
new_values = " ".join(new_values)
print(new_values)


