x = 12.5

def speed_to_pace(v):
    v = v ** (-1) * 60
    return "{1}:{0}".format(round(v%1*60), int(v))

print(speed_to_pace(x))