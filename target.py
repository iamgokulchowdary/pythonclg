str = input("Enter a string : ")

str = str.split()

list = []

for i in str:
    if i in list:
        pass
    else:
        list.append(i)

for i in range(len(list)):
    count = 0
    for j in str:
        if list[i] == j:
            count += 1
    
str = input("Enter a string : ")



str = str.split()



list = []



for i in str:

    if i in list:

        pass

    else:

        list.append(i)

maxstring = ""

maxcount = 0

for i in range(len(list)):

    count = 0

    for j in str:

        if list[i] == j:

            count += 1

    print("Letter : ",list[i]," is repeted : ",count)

    

    if maxcount<count:

        maxcount = count

        maxstring = list[i]

print("The word",maxstring, " is repeated for the maximum of times")
