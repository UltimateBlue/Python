nums = input('Enter numbers to calculate their average: ')
temp = nums.split(',')

sum = 0
maxim = int(temp[0])
for x in temp:
    sum += int(x)
    if maxim<int(x):
        maxim = int(x)
print(f"Average is {sum/len(temp)}")
print(f"maximum value is {maxim}")

# write a program which add up even numbers between 1 to 100
sum = 0
for i in range(2,101,2):
    sum+=i
print(sum)

