def findminX(num,rem,k):
	x = 1
	while(True):
		j = 0
		while(j<k):
			if x%num[j]!=rem[j]:
				break
			j += 1

		if j == k:
			return x

		x += 1

num = [5, 11, 17]
rem = [2, 3, 5]

k = len(num)
print(f"X is: {findminX(num,rem,k)}")
