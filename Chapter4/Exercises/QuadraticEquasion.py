import math

def PrintRoots(a,b,c):
    if Determinant(a,b,c) > 0:
        root1, root2 = Roots(a,b,c)
        print("r1 = ", root1, "r2 = ", root2)
    elif Determinant(a,b,c) == 0:
        root = Roots(a,b,c)
        print("r= ", root)
    else:
        print("The equation has no real roots.")

def Roots(a,b,c):
    root1 = (-b+math.sqrt(Determinant(a,b,c)))/(2*a)
    root2 = (-b-math.sqrt(Determinant(a,b,c)))/(2*a)

    return root1, root2


def Determinant(a,b,c):
    result= b**2 -4*a*c
    return result


