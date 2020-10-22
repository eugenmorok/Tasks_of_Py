import sys
input_price = int(sys.argv[1])
m_price = float(input_price) % 99
#f_price = "%.f" % m_price
if m_price != 0:
    print(input_price )
else:
    print(input_price + 1)
print(m_price)
#print(f_price)