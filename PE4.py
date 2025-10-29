numbers = []

for i in range(1,1000):
	numbers.append(i)
#print(numbers)


first_i = 0
prod_list = []

while True:
	for item in numbers:
		prod_list.append(item*numbers[first_i])
	first_i+=1
	if first_i == 999:
		break
#print(prod_list)




pali_list = []

def leng_5(number,list_):
	stringed_number = str(number)
	if (stringed_number[0] == stringed_number[-1]) and (stringed_number[1] == stringed_number[-2]):
		list_.append(int(stringed_number))


def leng_6(number,list_):
	stringed_number = str(number)
	if (stringed_number[0] == stringed_number[-1]) and (stringed_number[1] == stringed_number[-2]) and (stringed_number[2] == stringed_number[-3]):
		list_.append(int(stringed_number))

for number in prod_list:
	if len(str(number)) == 5:
		leng_5(number,pali_list)
	elif len(str(number)) == 6:
		leng_6(number,pali_list)

pali_list.sort()
print(pali_list[-1])