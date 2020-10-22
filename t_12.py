import sys
input_value = sys.argv[1]

print(input_value)

new_list = input_value.split()

new_list.append('0')

print(new_list)

j = 0

f = 0

#f = f + int(new_list[f])

print("переменная f1 = {}".format (f))

n = int(new_list.index('0'))
print("переменная n = {}".format (n))

while True:


    if j == n:
        break
    f = f + int(new_list[j])
    j = j + 1


print("переменная f2 = {}".format (f))