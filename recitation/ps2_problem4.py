'''
In this problem, you are going to implement a Quadratic Equation solver.
A quadratic equation is of the form  𝑎𝑥2+𝑏𝑥+𝑐=0.
 

Roots of this equation are  −𝑏±(√𝑏2−4𝑎𝑐)2𝑎
 .

What you need to do:

Take a, b, c as inputs to the quadratic solver function.
Calculate -b,  (⎯⎯√𝑏2−4𝑎𝑐)
  and 2a.
Now, we can have two cases:
a)  𝑏2−4𝑎𝑐
  >= 0
b)  𝑏2−4𝑎𝑐
  < 0
The first case is pretty simple where the roots are as decribed above. But in the second case where the term inside the square root is < 0, the roots become  −𝑏±𝑖(√4𝑎𝑐−𝑏2)2𝑎
 , where "i" is an imaginary number.

Note: the  ±
  sign means one root is  −𝑏+(√𝑏2−4𝑎𝑐)2𝑎
  and other is  −𝑏−(√𝑏2−4𝑎𝑐)2𝑎
 
Print the roots in a string format, with proper placement of "i" in the imaginary roots.
'''

def quadraticSolver(a, b, c):
    disc= (b**2)-(4*a*c)
    pos_instance = (-b + (disc**(1/2)))/2*a
    neg_instance = (-b - (disc**(1/2)))/2*a
    return pos_instance, neg_instance

quadraticSolver(1,-8,12)
        