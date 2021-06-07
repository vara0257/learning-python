grade = int(input("What was your score?"))

if grade >=90 and grade <=100:
    print("A+")
elif grade >=85 and grade <=89:
    print("A")
elif grade >=80 and grade <=84:
    print("B+")
elif grade >=75 and grade <=80:
    print("B")
elif grade >=70 and grade <=74:
    print("C+")        
elif grade >=65 and grade <=69:
    print("C")
elif grade >=60 and grade <=64:
    print("D+")
elif grade >=50 and grade <=59:
    print("D")
else:
    print("Fail")