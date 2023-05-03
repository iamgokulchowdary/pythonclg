num = eval(input("enter a number : "))
onum = num
sum = 0
while(num!=0):
    a = num%10
    sum = sum*10+a
    num = num//10
print("reverse number is ",sum)
