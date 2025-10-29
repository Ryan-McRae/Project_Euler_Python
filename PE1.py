#/bin/etc

mult_list = []
for i in range(1000):
	if (i%5 == 0) or (i%3 == 0):
		mult_list.append(i)
print(sum(mult_list))