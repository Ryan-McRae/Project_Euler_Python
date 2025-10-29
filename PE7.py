user_prime = int(input())
import time

def primer(number):
	divisors = 0
	for i in range(1,number+1):
		if number%i == 0:
			#print(str(i) + " - is a proper divisor")
			divisors += 1
	if divisors == 2:
		#print(str(number) + " is a prime")
		return(True)

final = 2
primes = 0 
prime = 0

start = time.time()
while primes < user_prime:
	for i in range(final,final+1):
		if primer(i) == True:
			#print(str(i) + " is a prime")
			primes += 1
			prime = i
	final += 1
end = time.time()

print(str(user_prime) + " prime: " + str(prime))
print("\nTime elapsed: " + str(end-start))