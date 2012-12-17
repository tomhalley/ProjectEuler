sum = 0
ps = [2, 3, 5]

def isPrime(n):
	if i % 3 == 0 or i % 5 == 0:
		return False
	for p in ps:
		if i % p == 0:
			return False
	return True

i = 5
while i < 50000:
	if isPrime(i):
		sum += i
		ps.append(i)
	i += 2

print sum