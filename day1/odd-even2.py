
count_even = 0
count_odd = 0
for i in range (1, 11):
    num = input("Enter number " + str(i) + ": ")
    
    num = int(num)
    
    if num % 2 == 0:
        count_even += 1
    else:
        count_odd +=1

print("Number of even numbers: " +  str(count_even))
print("Number of odd numbers: " +  str(count_odd))

