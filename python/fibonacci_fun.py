# x = 10 ** (24 * 116) / 999999999999999999999998999999999999999999999999
spacing = 24
import decimal
precision = 2500
con = decimal.getcontext()
con.prec = precision
x = decimal.Decimal(1)  /  decimal.Decimal(999999999999999999999998999999999999999999999999)
s = '{:.{}f}'.format(x, precision)
s = s[26:]
for n in range(len(s)/spacing):
    print s[(n*spacing):((n+1)*spacing)]
