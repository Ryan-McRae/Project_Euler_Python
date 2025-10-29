def factoral(x):
    factor = 1
    for i in range(1,x+1):
        factor *= i
    return(factor)



summation = 0


for z in range(5,6):
    summ = 0
    for i in range(1,6):
        summ += factoral(z - i)
    summation += (summ % z)
    
print(summation)
#print(summation % p)