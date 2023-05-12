str = input("Enter a string : ")
target = input("enter a target : ")

str = str.split()
count = 0

for i in str:
    if i==target:
        count += 1
print("count of target ",target," is : ",count)
