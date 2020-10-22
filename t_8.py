import sys
x = sys.argv[1].strip().capitalize().split(",")

l = len(x) - 2

sep = " "
x = sep.join(x).replace(" ", " и ").replace(" и ", ", ", l)

print(x)