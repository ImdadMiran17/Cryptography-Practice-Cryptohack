given = "label"
dig = 13
new = ([chr(ord(c)^dig) for c in given])
flag = ''.join(new)
print(flag)
