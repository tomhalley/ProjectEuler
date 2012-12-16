initial_primes = [2]

def isPrime(n):
	for prime in initial_primes:
		if n % prime == 0:
			return False
	return True

def erasto(n):
	for candidate in xrange(3, n, 2):
		if isPrime(candidate): 
			if candidate**2 > n:
				break
			initial_primes.append(candidate)

	numbers = [True]*n
	
	for p in initial_primes:
		for x in xrange(p, n, p):
			if p != x:
				numbers[x] = False
	
	numbers[1] = False
	primes = []

	for x in xrange(0, n):
		if numbers[x]:
			primes.append(x)

	return primes

print sum(erasto(2000000))
