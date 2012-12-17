f = open('Problem13_numbers.txt')

nums = []
total = 0

for line in f:
	nums.append(line[:50])

for x in nums:
	total += int(x)

print str(total)[:10]