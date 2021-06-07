prime_list = list()
x = int(input("Enter Upperbound: "))
def prime_addition():
    sum = 0
    for i in prime_list:
        sum = sum + i
    return sum
def prime_checking(num):
    for i in range(2, num):
        if(num%i)==0:
            break
    else:
        prime_list.append(num)
        return True
for temp in range(2, x+1):
    prime_checking(temp)
print(prime_list)
print("Sum of all Primes: ", prime_addition())