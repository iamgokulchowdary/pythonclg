# armgstrong number

num = eval(input("enter a number : "))
onum = num
sum = 0
while(num!=0):
    a = num%10
    sum = sum+(a**3)
    num = num//10
    
if (sum == onum):
    print(num," Yes! Its a Armstrong Number")
elif(sum!=onum):
    print(num," NO! Its not a Armstrong Number")
