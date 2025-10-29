#PE 3

primes = []

n = 2
d = 8043252

while (n != d):

	if(d%n == 0):
		d = d/n
		if(d%n != 0):
			primes.append(n)
	else:
		n += 1





primes.append(n)
print(primes)