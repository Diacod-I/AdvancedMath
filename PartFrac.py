from sympy import *
from sympy.integrals.transforms import inverse_laplace_transform
from sympy import exp, Symbol
from sympy.abc import s
s,t = symbols('s t')
try :
    value = apart(input("Apply the function in terms of s and t (use brackets wherever necessary):"))
    svalue=inverse_laplace_transform(value,s,t)
except EOFError:
        print("Oii, write it properly..")
except KeyboardInterrupt: 
    print("Oof.. Okay fine I guess..")
print("Partial fraction:",value)
print("Inverse Laplace:",svalue)