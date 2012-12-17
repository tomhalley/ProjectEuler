import math

def isPalindrome(n):
	n = str(n)
	cs = list(n)
	i = 0
	m = 0

	# Even numbers
	if len(cs) % 2 == 0:
		m = len(cs) / 2
		i = 0
	# Odd numbers 
	else:
		m = int(math.ceil(len(cs) / 2) + .1) + 1
		i = 1
		
	# General Logic
	for x in range(m, len(cs)):
		if cs[x] != cs[m - (i + 1)]:
			return False
		i += 1
	return True

max = 0

for x in range(999, 0, -1):
	for y in range(999, 0, -1):
		if isPalindrome(x * y):
			if (x * y) > max:
				max = x * y

print max