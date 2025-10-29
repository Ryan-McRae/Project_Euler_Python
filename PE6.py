square_list = []
number_list = []

for i in range(1,101):
	number_list.append(i)
	square_list.append(i**2)

print((sum(number_list)**2) - (sum(square_list)))