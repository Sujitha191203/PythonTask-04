nums = [40,8,22,43,9,70]

min_element = nums[0]

for i in nums:
    if i < min_element:
        min_element = i

print("Minimum element:", min_element)