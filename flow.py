import numpy as np
import fcsparser
import csv
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

path='/home/lucy/test.fcs'
##print(path)
meta,data=fcsparser.parse(path,reformat_meta=True)
##print(data)
#plt.scatter(data['SSC-A'],data['SSC-H'], alpha=0.8,color='gray')
#plt.show()

#print(data['SSC-A'])
#print(data['SSC-H'])
SSC = np.vstack([data['SSC-A'],data['SSC-H']])
##print(SSC)
SSC_z = gaussian_kde(SSC)(SSC)
idx = SSC_z.argsort()
x,y,z = data['SSC-A'][idx],data['SSC-H'][idx],SSC_z[idx]

N = round(len(x)/2.5)
fig,ax=plt.subplots()
#ax.scatter(data['SSC-A'],data['SSC-H'],c=SSC_z,s=100, edgecolor='')
#ax.scatter(x,y, c=z,s=50, edgecolor='')
ax.scatter(x[N:],y[N:], c=z[N:],s=50, edgecolor='')
ax.scatter(x[:N],y[:N], c='r',s=50, edgecolor='')
plt.show()

