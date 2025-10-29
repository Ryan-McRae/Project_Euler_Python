
current_sum = 0

for i in range(1,1001):
	current_sum += i**i

stringed = str(current_sum)
print(stringed[-10:])
