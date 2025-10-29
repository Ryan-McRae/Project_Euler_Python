from typing import Counter


f_n_1 = 1
f_n_2 = 1

Counter = 2
length = 1

while length < 1000:
    f_new = f_n_2 + f_n_1
    f_n_1 = f_n_2
    f_n_2 = f_new
    length = len(str(f_new))
    Counter +=1
    #print("The " + str(Counter) + " term is : " + str(f_new))
    
    
print(Counter)