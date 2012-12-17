primes = [2]

def isPrime(n):
	for p in primes:
		if i % p == 0:
			return False
	return True

i = 3
while len(primes) < 10001:
	if isPrime(i):
		primes.append(i)
	i += 1

print primes[10000]