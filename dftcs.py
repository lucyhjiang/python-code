#Program to solve heat equations using Forwarrd time centered space scje,e

import numpy
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages('finite_difference.pdf')

#Initialize parameters
tau = float(input ('Enter time step size: '))
N = int(input ("Enter the number of grid points: "))

#Analyze if the solution is stable with the current gridsize
ukappa = 1. #diffusion coefficient for u
vkappa = 10. #diffusion coefficient for v

L = 10. #total size 
h = L/(N) #grid size
coeff = vkappa * tau/h**2
print(coeff)

if coeff <= 0.5:
	print("Solution is stable with currect gridsize")
else:
	print("Solution is not stable with the current gridsize")


nstep = int(input ("Enter the number of steps: ")) 
plotstep = int(input("Enter the plotstep: "))
gamma = float(input("Enter the scaling parameter: "))

#gamma = 70. #scaling parameter



a = 92.
b = 64.
K = 0.1
alpha = 1.5
rho = 18.5


#Define X/Y grid
X = numpy.arange(0, 10, h)
##print("Size of X: ", len(X))




#Set initial condition
##uu = numpy.zeros((N,N))
##uu[round((N-1)/2),round((N-1)/2)] = 1/h #delta function
uu = numpy.random.rand(N,N)
##vv = numpy.zeros((N,N));
##vv[round((N-1)/2),round((N-1)/2)] = 1/h #delta function
vv = numpy.random.rand(N,N)

##print(uu)
##print(vv)
##print("Size of uu: ", len(uu))



#Loop through time
for istep in range(nstep):
	#initiate temp storage matrix
	uu_new = numpy.zeros((N,N));
	vv_new = numpy.zeros((N,N));
	#Loop through x
	for ix in range(N):
		for iy in range(N):
			if ix == 0 and iy ==0:
				uu_new[ix,iy] = uu[ix,iy] + tau * ( ukappa/h**2 * ( uu[ix+1,iy] + uu[ix,iy+1] - 2*uu[ix,iy]) + gamma * (a - uu[ix,iy] - (rho*uu[ix,iy]*vv[ix,iy])/(1 + uu[ix,iy] + K * uu[ix,iy]**2 )))
				vv_new[ix,iy] = vv[ix,iy] + tau * ( ukappa/h**2 * ( vv[ix+1,iy] + vv[ix,iy+1] - 2*vv[ix,iy]) + gamma * (alpha * (b-vv[ix,iy]) - (rho*uu[ix,iy]*vv[ix,iy])/(1 + uu[ix,iy] + K * uu[ix,iy]**2 )))
			elif ix == 0 and iy == N-1:
				uu_new[ix,iy] = uu[ix,iy] + tau * ( ukappa/h**2 * ( uu[ix+1,iy] + uu[ix,iy-1] - 2*uu[ix,iy]) + gamma * (a - uu[ix,iy] - (rho*uu[ix,iy]*vv[ix,iy])/(1 + uu[ix,iy] + K * uu[ix,iy]**2 )))
				vv_new[ix,iy] = vv[ix,iy] + tau * ( ukappa/h**2 * ( vv[ix+1,iy] + vv[ix,iy-1] - 2*vv[ix,iy]) + gamma * (alpha * (b-vv[ix,iy]) - (rho*uu[ix,iy]*vv[ix,iy])/(1 + uu[ix,iy] + K * uu[ix,iy]**2 )))
			elif ix == N-1 and iy == 0:
				uu_new[ix,iy] = uu[ix,iy] + tau * ( ukappa/h**2 * ( uu[ix-1,iy] + uu[ix,iy+1] - 2*uu[ix,iy]) + gamma * (a - uu[ix,iy] - (rho*uu[ix,iy]*vv[ix,iy])/(1 + uu[ix,iy] + K * uu[ix,iy]**2 )))
				vv_new[ix,iy] = vv[ix,iy] + tau * ( ukappa/h**2 * ( vv[ix-1,iy] + vv[ix,iy+1] - 2*vv[ix,iy]) + gamma * (alpha * (b-vv[ix,iy]) - (rho*uu[ix,iy]*vv[ix,iy])/(1 + uu[ix,iy] + K * uu[ix,iy]**2 )))
			elif ix == N-1 and iy == N-1:
				uu_new[ix,iy] = uu[ix,iy] + tau * ( ukappa/h**2 * ( uu[ix-1,iy] + uu[ix,iy-1] - 2*uu[ix,iy]) + gamma * (a - uu[ix,iy] - (rho*uu[ix,iy]*vv[ix,iy])/(1 + uu[ix,iy] + K * uu[ix,iy]**2 )))
				vv_new[ix,iy] = vv[ix,iy] + tau * ( ukappa/h**2 * ( vv[ix-1,iy] + vv[ix,iy-1] - 2*vv[ix,iy]) + gamma * (alpha * (b-vv[ix,iy]) - (rho*uu[ix,iy]*vv[ix,iy])/(1 + uu[ix,iy] + K * uu[ix,iy]**2 )))
			elif ix == 0:
				uu_new[ix,iy] = uu[ix,iy] + tau * ( ukappa/h**2 * ( uu[ix+1,iy] + uu[ix,iy+1] + uu[ix,iy-1] - 3*uu[ix,iy]) + gamma * (a - uu[ix,iy] - (rho*uu[ix,iy]*vv[ix,iy])/(1 + uu[ix,iy] + K * uu[ix,iy]**2 )))
				vv_new[ix,iy] = vv[ix,iy] + tau * ( ukappa/h**2 * ( vv[ix+1,iy] + vv[ix,iy+1] + vv[ix,iy-1] - 3*vv[ix,iy]) + gamma * (alpha * (b-vv[ix,iy]) - (rho*uu[ix,iy]*vv[ix,iy])/(1 + uu[ix,iy] + K * uu[ix,iy]**2 )))
			elif iy == 0:
				uu_new[ix,iy] = uu[ix,iy] + tau * ( ukappa/h**2 * ( uu[ix+1,iy] + uu[ix-1,iy] + uu[ix,iy+1] - 3*uu[ix,iy]) + gamma * (a - uu[ix,iy] - (rho*uu[ix,iy]*vv[ix,iy])/(1 + uu[ix,iy] + K * uu[ix,iy]**2 )))
				vv_new[ix,iy] = vv[ix,iy] + tau * ( ukappa/h**2 * ( vv[ix+1,iy] + vv[ix-1,iy] + vv[ix,iy+1] - 3*vv[ix,iy]) + gamma * (alpha * (b-vv[ix,iy]) - (rho*uu[ix,iy]*vv[ix,iy])/(1 + uu[ix,iy] + K * uu[ix,iy]**2 )))
			elif ix == N-1:
				uu_new[ix,iy] = uu[ix,iy] + tau * ( ukappa/h**2 * ( uu[ix-1,iy] + uu[ix,iy+1] + uu[ix,iy-1] - 3*uu[ix,iy]) + gamma * (a - uu[ix,iy] - (rho*uu[ix,iy]*vv[ix,iy])/(1 + uu[ix,iy] + K * uu[ix,iy]**2 )))
				vv_new[ix,iy] = vv[ix,iy] + tau * ( ukappa/h**2 * ( vv[ix-1,iy] + vv[ix,iy+1] + vv[ix,iy-1] - 3*vv[ix,iy]) + gamma * (alpha * (b-vv[ix,iy]) - (rho*uu[ix,iy]*vv[ix,iy])/(1 + uu[ix,iy] + K * uu[ix,iy]**2 )))
			elif iy == N-1:
				uu_new[ix,iy] = uu[ix,iy] + tau * ( ukappa/h**2 * ( uu[ix+1,iy] + uu[ix-1,iy] + uu[ix,iy-1] - 3*uu[ix,iy]) + gamma * (a - uu[ix,iy] - (rho*uu[ix,iy]*vv[ix,iy])/(1 + uu[ix,iy] + K * uu[ix,iy]**2 )))
				vv_new[ix,iy] = vv[ix,iy] + tau * ( ukappa/h**2 * ( vv[ix+1,iy] + vv[ix-1,iy] + vv[ix,iy-1] - 3*vv[ix,iy]) + gamma * (alpha * (b-vv[ix,iy]) - (rho*uu[ix,iy]*vv[ix,iy])/(1 + uu[ix,iy] + K * uu[ix,iy]**2 )))
				##uu_new[ix,iy] = 6
			else:
				##uu_new[ix,iy] = 8
				uu_new[ix,iy] = uu[ix,iy] + tau * ( ukappa/h**2 * ( uu[ix+1,iy] + uu[ix-1,iy] + uu[ix,iy+1] + uu[ix,iy-1] - 4*uu[ix,iy]) + gamma * (a - uu[ix,iy] - (rho*uu[ix,iy]*vv[ix,iy])/(1 + uu[ix,iy] + K * uu[ix,iy]**2 )))
				vv_new[ix,iy] = vv[ix,iy] + tau * ( ukappa/h**2 * ( vv[ix+1,iy] + vv[ix-1,iy] + vv[ix,iy+1] + vv[ix,iy-1] - 4*vv[ix,iy]) + gamma * (alpha * (b-vv[ix,iy]) - (rho*uu[ix,iy]*vv[ix,iy])/(1 + uu[ix,iy] + K * uu[ix,iy]**2 )))
				
	##print(uu_new)
	##print(vv_new)

	uu = uu_new
	vv = vv_new
	print("Now is at step: ", istep)
	if (istep+1)%plotstep == 0:
		fig = plt.figure()
		plt.clf()
		time = (istep+1) * tau
		plt.contourf(X,X,uu)
		plt.title('Time = %i' %time)
		pp.savefig()
		

print(uu)
print(vv)

pp.close()




	

	 
