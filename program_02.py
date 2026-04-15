lst = [10, 501, 22, 37, 100, 999, 87, 351]

prime_list = []

for num in lst:
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
             prime_list.append(num)
count = len(prime_list)

print("prime Number:",prime_list)
print("count:",count)