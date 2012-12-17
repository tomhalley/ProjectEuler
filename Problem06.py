def SumOfSquares():
	total = 0
	i = 1
	while i <= 100:
		total += (i**2)
		i += 1
	return total

def SquareOfSum():
	sum = 0
	i = 1
	while i <= 100:
		sum += i
		i += 1
	return sum**2

print SquareOfSum() - SumOfSquares()