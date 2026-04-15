nums = [4, 5, 1, 2, 0, 5, 4, 1, 2, 9]

for i in nums:
    if nums.count(i) == 1:
        print("First non-repeating element:", i)
        break
