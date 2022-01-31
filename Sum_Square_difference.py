sum_0 = 0
for i in range(101):
    sum_0 += (i ** 2)

sum_1 = 0
for i in range(101):
    sum_1 += i

print(sum_1 ** 2 - sum_0)
