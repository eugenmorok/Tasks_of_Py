import sys
input_list = list(sys.argv[1:])
len_list = len(input_list)
empty_list = []
a = 0
input_list.insert(0, 0)
print(input_list)
#print(len_list)

for i in range(1, len_list + 1):
    a = int(a) + int(input_list[i])
    #print(a)
    empty_list.append(str(a))
    #print(empty_list)
    i += 1
print(", ".join(empty_list))




