onum = eval(input("enter a number : "))
num = onum
sum = 0
while(num!=0):
    a = num%10
    sum = sum*10+a
    num = num//10
if(sum==onum):
    print(onum," Yes! its a palindrome")
else:
    print(onum," No! its not a palindrome")
