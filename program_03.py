nums = [10, 501, 22, 37, 100, 999, 87, 351]

happy_numbers = []

for num in nums:
    n = num
    seen = []   
    
    if n != 1 and n not in seen:
        seen.append(n)
        
        total = 0
        for digit in str(n):
            total += int(digit) ** 2
        
        n = total
    
    if n == 1:
        happy_numbers.append(num)

print("Happy numbers:", happy_numbers)
print("Count:", len(happy_numbers))