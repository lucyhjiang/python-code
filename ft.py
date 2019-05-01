# Discrete Fourier transform demonstration (python v3)

# Initialize the since wave time series to be transformed
# Pesudo code
# 1. Input: get user input of original vector
# 1a: Input vector manually
# 1b: Input vector by a function: size of vector, frequency and phase of function
# 2. Fourier transform the vector into another vector into frequency space
# 3. Plot out original vector, and transformed vector

import cmath

# get user-input vector
v = [complex(x) for x in input().split()]
# count size of vector
N = len(v)


# initialize transformed vector
vft = list(range(N))


# calculate transformed vector using for loop
for y in range(N):
	sum = 0
	for x in range(N):
		psum =v[x]*cmath.exp(complex(0, -2*cmath.pi*x*y/N))
		psum = complex(round(psum.real),round(psum.imag))
		sum = sum + psum
		# print (psum)
	vft[y] = 1/N*sum
	
# Print calculated loop
print(vft)
