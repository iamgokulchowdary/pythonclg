startrange = eval(input("start range : "))
stoprange = eval(input("stop range : "))

for i in range(startrange,(stoprange+1)):
    num = i
    onum = num
    sum = 0
    while(num!=0):
        a = num%10
        sum = sum+(a**3)
        num = num//10
    
    if (sum == onum):
        print(onum)
    

