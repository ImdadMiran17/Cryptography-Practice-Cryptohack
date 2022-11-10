ints = [14, 6, 11]
p = 29

for i in range(p - 1):
	if pow(i,2)%29 == ints[0]:
		print(f"Found Quadratic Residue. Square Root {i}")
	elif pow(i,2)%29 == ints[1]:
		print(f"Found Quadratic Residue. Square Root {i}")
	elif pow(i,2)%29 == ints[2]:
		print(f"Found Quadratic Residue. Square Root {i}")

#Alternative Solution

p = 29
ints = [14, 6, 11]

qr = [a for a in range(p) if pow(a,2,p) in ints]
print(f"flag {min(qr)}")
