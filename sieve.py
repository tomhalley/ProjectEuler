primes = [2, 3, 5]


def sieveOfErastosthenes():
	sum = 0
	for x in range(5, 2000000):
		if x%2==0 or x%3==0 or x%5==0 or x%7==0:
			continue
		else:
			primes.append(x)
			sum += x
	return sum

print sieveOfErastosthenes()