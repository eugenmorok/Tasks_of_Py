import sys
string = sys.argv[1]
letters = "abcdefghijklmnopqrstuvwxyz"
lowercase = []
uppercase = []
for char in string:
    if char in letters:
        lowercase.append(char)
    else:
        uppercase.append(char)
case = "".join(lowercase + uppercase)
print(case)