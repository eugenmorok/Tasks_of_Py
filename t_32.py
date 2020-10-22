import sys
s = int(sys.argv[1])
f = 1
for i in range(s):
    f += f * i
print(f)