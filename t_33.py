import sys
str = sys.argv[1]

def strip(s):
    return " ".join(s.strip().split())

print(strip(str))
