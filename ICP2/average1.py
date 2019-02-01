n=int(input("Enter the number of trees:"))
tarun = input("Enter the height of trees separated by space: ")
list  = tarun.split()
sum = 0
for num in list:
    sum += int (num)
print("Sum = ",sum)
avg = sum/n
print(avg)
round(avg,3)
print("avg = ",avg)