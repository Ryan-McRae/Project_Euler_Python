import inflect

p = inflect.engine()

summ = 0

for n in range(1,1001):
    name = p.number_to_words(n)
    for i in name:
        if i != "-" and  i != " ":
            summ += 1

print(summ)
        