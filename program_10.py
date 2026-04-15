nums = [4, 2, -3, 1, 6]

found = False

for start in range(len(nums)):
    total = 0
    
    for end in range(start, len(nums)):
        total += nums[end]
        
        if total == 0:
            found = True
            break
    
    if found:
        break

if found:
    print("Sublist with sum 0 exists")
else:
    print("No sublist with sum 0 found")