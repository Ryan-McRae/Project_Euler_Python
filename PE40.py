constant = "01"

adder = 1

while len(constant) < 1000005:
    adder += 1 
    constant = constant + str(adder)
    

#print(constant)
#print(constant[12])


mulitiple = int(constant[1]) * int(constant[10]) * int(constant[100]) * int(constant[1000]) * int(constant[10000])* int(constant[100000])* int(constant[1000000])
print(mulitiple)
