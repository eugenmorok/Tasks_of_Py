import sys
x = sys.argv[1].strip().split()
x.sort(key=len)
print(x[-1])

