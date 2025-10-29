
distinctions = []

for a in range(2,101):
    for b in range(2,101):
        distinctions.append(str(a**b))

cleaned_dis = list(dict.fromkeys(distinctions))

print(len(cleaned_dis))