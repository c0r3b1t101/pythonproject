
"""
    Students  |  Grades  |  Letters
   ------------|----------|----------
     George    |  46      |  F
     Michell   |  80      |  B
     Josh      |  12      |  F
     Chloe     |  68      |  D
     Stanley   |  99      |  A
     Annie     |  100     |  A+
   """
gradetotest = int(input("Enter your grade: "))
if gradetotest == 100:
    print("A+")
elif gradetotest >= 80:
    print("B")
elif gradetotest >= 70:
    print("C")
elif gradetotest >= 60:
    print("D")
else:
    print("F")
