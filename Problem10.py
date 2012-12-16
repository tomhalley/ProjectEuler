import math

def erasto(n):
	numbers = [True]*n
	for i in range(2, int(math.ceil(math.sqrt(n)))):
		if numbers[i]:
			for j in range(i*i, n, i):
				numbers[j] = False

	primes = []
	for x in range(2, n):
		if numbers[x]:
			primes.append(x)

	return primes

print sum(erasto(2000000))
