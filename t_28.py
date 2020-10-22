import sys
s = sys.argv[1:]
print(s)
new_list = []
for item in s:
    if int(item) < 0:
        new_list.append(str(item))
for item in s:
    if int(item) >= 0:
        new_list.append(str(item))

print(" ".join(new_list))