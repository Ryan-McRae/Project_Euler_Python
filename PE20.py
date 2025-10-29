#PE 20
n = 100
c = 1
ans = 0

for i in range(2,n+1):
	c *= i

cs = str(c)

for i in range(0,len(cs)):
	ans += int(cs[i])

print(ans)