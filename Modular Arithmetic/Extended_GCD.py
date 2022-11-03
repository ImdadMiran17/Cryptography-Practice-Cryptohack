def gcd_extended(a,b):
	if a == 0:
		return b,0,1;

	gcd,x1,y1 = gcd_extended(b%a, a)

	x = y1 - (b//a)*x1
	y = x1

	return gcd, x, y

gcd, x, y = gcd_extended(26513, 32321)
print(f"GCD = {gcd}, X = {x}, Y = {y}")
