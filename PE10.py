# Prime checker

import math
likely_prime = []
primes = [1, 2, 3, 5, 7, 11, 13, 17, 19]

for i in range(21, 2000000, 2):  
    for n in range(2, 6):  
        if i % n == 0:  
            break
    else:
        likely_prime.append(i)
print(len(likely_prime))
for i in likely_prime:
    is_prime = True
    for j in likely_prime:
        if j >= i:
            break  # only check smaller numbers
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

