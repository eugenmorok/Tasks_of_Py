import sys
x = sys.argv[1].strip().replace(",", "").split()
x.reverse()
x = " ".join(x)
print(x)
