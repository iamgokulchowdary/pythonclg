def gcd(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range(1, (smaller+1)):
        if (x%i==0) and (y%i==0):
            gcd = i
    return gcd

x = eval(input("Enter value for X : "))
y = eval(input("Enter value for Y : "))

print("GCD of is ",gcd(x,y))
