#Number 1
def doublePrecision():
  s = 0
  exponent = 10000000111
  c, i = 0, 0
  while(exponent != 0):
    exp = exponent % 10
    c = c + exp * pow(2, i)
    exponent = exponent//10
    i += 1
  fraction = str(1110101110010000000000000000000000000000000000000000)
  f = 0
  i = 1
  for item in fraction:
    f = f + int(item) * (0.5**i)
    i += 1
  n = ((-1)**s)*(2**(c - 1023)) * ((1+f))
  print(n)
  return

doublePrecision()
print("\n")
#Number 2
def Chopping():
  s = 0
  
  exponent = 10000000111
  c, i = 0, 0
  while(exponent != 0):
    exp = exponent % 10
    c= c + exp * pow(2,i)
    exponent = exponent//10
    i+=1
    
  fraction = str(1110101110010000000000000000000000000000000000000000)
  f = 0
  i = 1
  for item in fraction:
    f = f+int(item) * (0.5**i)
    i+=1
  nc = ((-1)**s)*(2**(c-1023)) * ((1+f))
  print(int(nc))

  return
Chopping()
print("\n")

#Number 3
def Rounding():
  s = 0
  exponent = 10000000111
  c, i = 0, 0
  while(exponent != 0):
    exp = exponent % 10
    c = c + exp *pow(2, i)
    exponent = exponent//10
    i+= 1
  fraction = str(1110101110010000000000000000000000000000000000000000)
  f = 0
  i = 1
  for item in fraction:
    f = f + int(item)*(0.5**i)
    i += 1
  nr = ((-1)**s)*(2**(c-1023)*(1+f))
  print(round(nr))
  return
Rounding()
print("\n")

#Number 4
def absolute_error(precise:float, approximate: float):
    sub_operation = precise - approximate
    return abs(sub_operation)

def relative_error(precise:float, approximate: float):
    sub_operation = absolute_error(precise, approximate)
    div_operation = sub_operation / precise
    return div_operation

print(absolute_error(491.5625, 492))
print(relative_error(491.5625, 492))
print("\n")

#Number 5
def infinite_series(x, k:int):
  return((-1)**k) * ((x**k)/(k**3))
min_error = 1e-4
current_itteration = 1
while(abs(infinite_series(1, current_itteration)) > min_error):
  current_itteration += 1 

print(current_itteration - 1)
print("\n")

#Number 6
import numpy as np
def func(x):
    return ((x**3) + (4*(x**2)) - 10)
def my_bisection(f, a, b, tol): 
    if np.sign(f(a)) == np.sign(f(b)):
      raise Exception(
         "The scalars a and b do not bound a root")
    m = (a + b)/2
    if np.abs(a -b) <= tol:
        # stopping condition, report m as root
        return 0
    elif np.sign(f(a)) == np.sign(f(m)):
        # case where m is an improvement on a. 
        # Make recursive call with a = m
        return my_bisection(f, m, b, tol) + 1
    elif np.sign(f(b)) == np.sign(f(m)):
        # case where m is an improvement on b. 
        # Make recursive call with b = m
        return my_bisection(f, a, m, tol) + 1
def my_newton(f, df, x0, tol):
  result = f(x0) / df(x0)
  x = x0
  count = 1
  while(abs(result) >= tol):
    x -= result
    count += 1
    result = f(x)/ df(x)
  return count
f_x = lambda x: (x**3) + (4* (x**2)) - 10
f_prime = lambda x: 3 * (x**2) + (8 * x)

print(my_bisection(f_x, -4, 7, .0001))
print(my_newton(f_x, f_prime, 7, .0001))
