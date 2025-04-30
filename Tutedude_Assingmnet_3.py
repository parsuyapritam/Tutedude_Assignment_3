#Task_1
n=int(input('Enter a number: '))
def Factorial(n):
    if n <= 1:
        return 1
    else:
        return n * (Factorial(n-1))

F=Factorial(n)
print('Factorial of',n,'is:',F)



#Task_2

import math
a=int(input('\nEnter a number: '))

print("Square root: ",math.sqrt(a))
print("Logarithm: ",math.log(a) )
print("Sine: ",math.sin(a))

