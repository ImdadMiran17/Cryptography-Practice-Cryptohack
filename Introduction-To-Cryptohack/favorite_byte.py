encoded = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for i in range(256):
	decoded = ''.join(chr(c^i) for c in encoded)
	if decoded.isprintable():
		print(i, decoded)

