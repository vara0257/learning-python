fibonacci = []



def series(n):

   if n <= 1:

       return n

   else:

       return(series(n-1) + series(n-2))



upperLimit = int(input("Enter a number: "))



if upperLimit <= 0:

   print("Enter any positive number")

else:

   print("series sequence:")

   for i in range(upperLimit):

       if series(i)<=upperLimit:

           fibonacci.append(series(i))



print(fibonacci)



def binarySearch(alist, item):

    first = 0

    last = len(alist)-1

    found = False



    while first<=last and not found:

        midpoint = (first + last)//2

        if alist[midpoint] == item:

            return True

            

        else:

            if item < alist[midpoint]:

                last = midpoint-1

            else:

                first = midpoint+1

    

    return False



item = int(input("Enter a number to found: "))



if binarySearch(fibonacci, item):

    print ("found")

else:
    
    print("Not Found!")