count = 0

for z in range(30000000,300000000):
	for i in range(1,21):
		if z%i == 0:
			count+=1
			if count == 20:
				print(z)
	count = 0