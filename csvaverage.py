import numpy as np

import numpy as np

path = 'data.csv'
all= np.genfromtxt(path, delimiter=",")

all.mean(axis=0)

average=[]

for i in range(all.shape[1]):
    average.append((all[0,i]+all[1,i])/2)
    
 
file = open("results.txt","w+")
file.write("average")
file.close