x = int(input("Enter Upperbound: "))
sum = 0
for temp in range(2, x+1):
    for i in range(2, temp):
        if(temp%i)==0:
            break
    else:
        sum = sum + temp
        print(temp)