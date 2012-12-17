def findSmallestProduct():
	i = 21
	while(True):
		if isDivisible(i):
			return i
		i += 1

def isDivisible(n):
	for x in range(1, 21):
		if n % x != 0:
			return False
	return True

print findSmallestProduct()