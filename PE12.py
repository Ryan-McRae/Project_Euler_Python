def div(n):
	count = 0
	for i in range(1,n+1):
		if n%i == 0:
			count += 1
	return(count)

div_count = 0
p = 1
diff =2
while div_count < 500:
	div_count = div(p)
	p += diff
	diff += 1
	print(p)

print(p-diff+1)

"""
p = 1
diff = 2
while p < 30:
	print(p)
	p += diff
	diff += 1
"""