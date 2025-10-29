
bouncy = 19602
f = 21780

while (bouncy/f)*100 < 99:

	num_list = []
	for n in str(f):
		num_list.append(str(n))
	if (num_list != sorted(num_list) and  num_list != sorted(num_list, reverse = True)):
		bouncy += 1
	f += 1
	print((bouncy/f)*100)
		

print(bouncy)
print(f-1)


