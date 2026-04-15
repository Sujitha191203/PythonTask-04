count = 0

for r10 in range(0, 2):          
    for r5 in range(0, 3):       
        for r2 in range(0, 6):   
            for r1 in range(0, 11): 
                
                total = r10*10 + r5*5 + r2*2 + r1*1
                
                if total == 10:
                    print("10₹:", r10, " 5₹:", r5, " 2₹:", r2, " 1₹:", r1)
                    count += 1

print("Total ways:", count)