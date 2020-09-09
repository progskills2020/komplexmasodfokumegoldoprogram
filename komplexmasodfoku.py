import math
import cmath

"""
ax^2+bx+c=0
a!=0


"""

a = float(input("Adja meg az 'a'-t:"))
b = float(input("Adja meg az 'b'-t:"))
c = float(input("Adja meg az 'c'-t:"))

diszkriminans = b*b-4*a*c

if diszkriminans>0:
    x1 = (-b+math.sqrt(diszkriminans))/(2*a)
    x2 = (-b-math.sqrt(diszkriminans))/(2*a)
    print("A másodfokú egyenletnek két valós megoldása van:%.2f, %.2f" % (x1,x2))
elif diszkriminans == 0:
    x = -b/(2*a)
    print("A másodfokú egyenletnek egy valós megoldása van:%.2f" % x)
else:
    x1 = (-b+cmath.sqrt(diszkriminans))/(2*a)
    x2 = (-b-cmath.sqrt(diszkriminans))/(2*a)
    print("A másodfokú egyenletnek két komplex megoldása van:",(x1,x2))






