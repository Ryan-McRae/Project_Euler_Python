def factoral(x):
    factor = 1
    for i in range(1,x+1):
        factor *= i
    return(factor)

def binomial(constant,dependency):
    return( (factoral(constant)) / (factoral(dependency)*factoral(constant - dependency)))

def divisors(divisor):
    summation = 0
    for i in range(1,divisor+1):
        if divisor%i == 0:
            summation += i
            #print(i)
    return(summation)


total_summation = 0
n = 5

for i in range(1,n+1):
    prod = 1
    for z in range(0,i+1):
        #print(int(binomial(i,z)))
        prod *= binomial(i,z)
    total_summation += int(divisors(int(prod)))
print(total_summation)