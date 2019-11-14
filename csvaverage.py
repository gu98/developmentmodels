import numpy as np

path = 'data.csv'
all= np.genfromtxt(path, delimiter=",")

results=all.mean(axis=0)

#print(results)

file = open("results.csv","w+")
file.write(",".join(str(value) for value in results))
file.close()