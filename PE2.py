
fib_list = [1,2]

i = 0

while True:
	tn = fib_list[i] + fib_list[i+1]
	if (tn >= 4*(10**6)):
		even_list = []
		for item in fib_list:
			if (item%2) == 0:
				even_list.append(item)
		print(sum(even_list))
		break
	else:
		fib_list.append(tn)
		i+=1
