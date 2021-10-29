def get_sum(numbers):
    total = 0
    for number in numbers: 
        total = total + number
        
    return total

s1 = get_sum([2, 5, 8, 3])
print(s1)