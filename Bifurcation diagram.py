import matplotlib.pyplot as plt
import numpy as np
import time

def rec(r, x): #r = growth rate, x = population
    return r*x*(1-x)

t1 = time.time()

initial = .4 #Initial population
p = [[initial]] 
m = 5000
r = np.linspace(-3, 4, m)
n = 500
y_final = []
for j in range(m): #for changing growth rate
    p.append([initial])
    for i in range(n): #for changing the population
        p[j].append(rec(r[j], p[j][-1]))
        #if n-i<20:
    y_final.append(p[j][-200::])

t2 = time.time()
print("Duration = ", t2-t1)

plt.style.use('dark_background')
fig = plt.figure(figsize=(6,6), facecolor='black')
ax = plt.axes(frameon=False)

plt.plot(r,y_final,'w.',markersize=.05)
plt.show()
