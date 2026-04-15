lst=[10,501,22,37,100,999,87,351]

even_list = []
odd_list = []

for i in lst:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(even_list)
print(odd_list)


