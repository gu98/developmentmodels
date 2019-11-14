import numpy as np

path = 'data.csv'
all= np.genfromtxt(path, delimiter=",")

results=all.mean(axis=0)


    
print(results)
file = open("results.txt","w+")
file.write("average")
file.close