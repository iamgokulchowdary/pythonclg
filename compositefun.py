def sum(a,b):
    sum=a+b
    return sum
def avg(sum):
    avg=sum/2
    return avg

a = eval(input("Enter A value : "))
b = eval(input("Enter B value : "))

avg= avg(sum(a,b))
print("Average : ",avg)
