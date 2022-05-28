from re import search
from sympy import *
from sympy.integrals.transforms import inverse_laplace_transform,laplace_transform
from sympy import exp
from sympy.abc import s,t
s,t = symbols('s t')
def eLAPorINV(value):
    if (search("s",str(value))):
        tvalue=inverse_laplace_transform(value,s,t)
        print("Inverse Laplace:",tvalue)
    elif (search("t",str(value))):
        svalue=laplace_transform(value,t,s)
        print("Laplace:",svalue)    
try :
    value = (input("Apply the function in terms of s or t (use brackets wherever necessary):"))
    print("Partial fraction:",apart(value))
    eLAPorINV(value)
except KeyboardInterrupt: 
    print("\n\n\nOof.. Okay fine I guess..")
except:
    print("An exception occured while trying to find apart()")
