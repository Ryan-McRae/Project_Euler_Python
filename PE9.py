import math

results = []

for b in range(1, 500):
    numerator = 1000 * b - 500 * 1000
    denominator = b - 1000
    
    if denominator == 0:
        continue  # avoid division by zero

    a = numerator / denominator

    if a > 0 and a.is_integer() and b > a:
        results.append((int(a), b))

# Print results
for a_val, b_val in results:
    print(f"a = {a_val}, b = {b_val}")
    c = math.sqrt(math.pow(a_val,2)+math.pow(b_val,2))
    print(f"c = {c}")
    print(a_val * b_val * c)
