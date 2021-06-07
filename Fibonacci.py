fibonacci = []

def series(n):
   if n <= 1:
       return n
   else:
       return(series(n-1) + series(n-2))

upperLimit = int(input("Enter a number: "))

if upperLimit <= 0:
   print("Enter any positive numper")
else:
   print("series sequence:")
   for i in range(upperLimit):
       fibonacci.append(series(i))

print(fibonacci)