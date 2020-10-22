import sys
str = float(sys.argv[1])
print("{:.>16s}".format("{:0>8.2f}".format(str)))