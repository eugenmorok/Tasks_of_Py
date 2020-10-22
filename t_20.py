import sys

#input_list = sys.argv[1:]
empty_list = []
#for i in input_list:
#    i = int(i)
#    print(i)
#    empty_list.append(i)
#print("max is {}".format(max(empty_list)))

max_val = int(sys.argv[1])
j = 0

while j < len(sys.argv[1:]):
    j += 1
    if max_val <= int(sys.argv[j]):
        print("max old {}".format(max_val))
        max_val = int(sys.argv[j])
        print("max new {}".format(max_val))

print("new cycle")
for item in sys.argv[1:]:
    a = int(item) - max_val
    a = str(a)
    print(a)
    empty_list.append(a)

empty_list = " ".join(empty_list)
print(empty_list)


import sys

values = sys.argv[1:]

# Сперва вычисляем лучший месяц.
max_value = int(values[0])
for value in values[1:]:
    value = int(value)
    if value > max_value:
        max_value = value
print(max_value)