# a program to remove duplicate in a list.

numbers = [2,5,2,7,6,7,4,9,6,8,10,20,5,8]
unique_nums = []
for number in numbers:
    if number not in unique_nums:
        unique_nums.append(number)
print(unique_nums)