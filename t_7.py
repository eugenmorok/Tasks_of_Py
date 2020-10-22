import sys
x = sys.argv[1].replace("?", "").replace(":", "").lower().strip().split()
sep = "-"
x = sep.join(x)
print(x)