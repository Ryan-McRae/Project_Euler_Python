col_leng = 0
longest_chain = 0
corr_number = 0



for i in range(1,1000000):
	collatz_number = i
	col_leng += 1
	while collatz_number != 1:
		if (collatz_number%2) == 0:
			collatz_number = collatz_number/2
			col_leng += 1
		else:
			collatz_number = (3 * collatz_number) + 1
			col_leng += 1

	if col_leng > longest_chain:
		longest_chain = col_leng
		corr_number = i

	col_leng = 0 



print(corr_number)
print(longest_chain)































"""
collatz_number = 10
while collatz_number != 1:
	if (collatz_number%2) == 0:
		collatz_number = collatz_number/2
		collatz_list.append(collatz_number)
	else:
		collatz_number = (3 * collatz_number) + 1
		collatz_list.append(collatz_number)



print(collatz_list)

"""