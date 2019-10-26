import sys


def hello(who):
    print('hello{}'.format(who))

hello(" world!")

#hello(sys.argv[0])
import math
math.factorial(5)
print(math.factorial(5))

from math import factorial as fac

n = 5
k = 3

print(fac(n) / (fac(k))*fac(n-k))
print(fac(n) // (fac(k))*fac(n-k))

print(2**31)

n=100
k=2
print(fac(n) // (fac(k))*fac(n-k))

print(fac(n))
x = len(str(fac(n)))
print(x)