

def ami(n):
	summ = 0
	for i in range(1,n):
		if n%i == 0:
			summ += i
	return(summ)

amis = 0


for i in range(1,10000):
	if i == ami(ami(i)) and i != ami(i):
		print(str(i) + " - " + str(ami(i)))
		amis += i
#		if ami(i) > 10000:
#			amis += ami(i)

print(amis)