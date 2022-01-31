n1 = 0
n2 = 1
total = 0

for i in range(4000000):
    n3 = n1 + n2
    if (n3 <= 4000000) and (n3 % 2) == 0:
        total += n3
    n1 = n2
    n2 = n3
    print(total)
    if total > 4000000:
        break
