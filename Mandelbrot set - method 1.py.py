import matplotlib.pyplot as plt
import numpy as np
import time

grid = []
resolution = 500 #***Don't asign a large number! because it will fill the whole memory and freezes the system. :(***

iteration = 30


x, y = np.meshgrid(np.linspace(-2,1,resolution), np.linspace(-1.5,1.5,resolution))

def zn(a,b):
    global g, z, new_z, c
    z = np.zeros((1,resolution,resolution))
    for i in range(iteration):
        try: new_z = [z[-1]**2 + x+y*1j]
        except: break
        z=np.concatenate((z,new_z))
        #g = abs(z) > 10
    g = abs(z)>10
    return g

t1 = time.time()

grid = zn(x,y)

   
t2 = time.time()
print('Duration = {:.4} Sec'.format(t2-t1))


plt.figure(figsize=(10,10))

plt.imshow(grid[-1], cmap=plt.get_cmap('winter'))
#plt.savefig('funcfrac5.png')
plt.show()

