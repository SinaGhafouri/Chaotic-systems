import matplotlib.pyplot as plt
import numpy as np
import time

grid = []
resolution = 200
iteration = 30
t1 = time.time()
for i in np.arange(-1.5,1.5,1/resolution):
    grid.append([])
    for j in np.arange(-1.5,1.5,1/resolution):
        grid[-1].append(1)
        z = [0]
        g = 1
        for k in range(iteration):
            new_z = z[-1]**2 + complex(j,i)
            z.append(new_z)
            if abs(z[-1]) > 3:
                g = 0
                break            
        if g==0:
            grid[-1][-1]=abs(z[-2]) #k/iteration
            
t2 = time.time()
print('Duration = {:.4} Sec'.format(t2-t1))

clrmp = plt.cm.winter
plt.figure(figsize=(50,50))
plt.imshow(grid, cmap=clrmp)
#plt.savefig('frac9.png')
plt.show()


