import sys
n = int(sys.argv[1])
a = float(0)
for i in range (0, n):
    a = a + ((-1)**i) / (2*i + 1) * 4
print("{:5f}".format(a))