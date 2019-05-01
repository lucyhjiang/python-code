# This code convert number from decimal form into binary (python v3)

# Input number (integer or fraction part)
# Output converted binary number

import math 
import sys

# Getting user input
# n = eval(input (" Please enter your number: "))
n = eval(sys.argv[1])
print (n)


# Separate into integer and fraction part
a = math.trunc(n)
b = n - a


# initialize variable
c = 10000
v = []


# Calculate binary conversion for integer part
while c != 0:
	c = math.floor (a/2)
	d = a - c * 2
	v.extend([str(d)])
	a = c
v.reverse()

# Calculate binary conversion for fraction part

if b == 0:
	print (''.join(v))
else:
	v.extend(".")
	while c <= 20 and b != 0: 
		e = b * 2
		f = math.trunc(e)
		v.extend([str(f)])
		b = e - f
	print (''.join(v))



