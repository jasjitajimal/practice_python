
# Equation is ax^2+bx+c
# Type the value of constants a,b and c
# Quadratic eqn has 2 solution

a = int(input("Enter Value of a: "))
b = int(input("Enter Value of b: "))
c = int(input("Enter Value of c: "))

Sol1 = (-b + ((b**2) - (4*a*c))**.5)/(2*a)
Sol2 = (-b + ((b**2) + (4*a*c))**.5)/(2*a)

Ans = "Solution 1 is: {0} and Solution 2 is: {1}"
print(Ans.format(Sol1, Sol2))
