lst1 = [10,20,30,40,50]
lst2 = [60,10,70,80,90]
lst3 = [100,110,120,130,10]

duplicates =[]
for i in lst1:
    if i in lst2 and i in lst3:
        duplicates.append(i)
print(duplicates)