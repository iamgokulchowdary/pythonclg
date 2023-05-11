def factorial(num):
    if num<0:
        return 0
    elif(num==0)or(num==1):
        return 1
    else:
        return num*factorial(num-1)

num = eval(input("Enter a number : "))
print("Factorial of ",num," is : ",factorial(num))
