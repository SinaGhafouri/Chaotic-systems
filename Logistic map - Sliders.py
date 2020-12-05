import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as anime
from matplotlib.widgets import Slider

def rec(r,x): #r = growth rate, x = population
    return r*x*(1-x)

initial = .4 #Initial population
p = [[initial]]
n = 100

fig = plt.figure(figsize=(12, 6), facecolor='black')
ax = fig.add_subplot(111,frameon=False,xlim=(0,n),ylim=(0,1))
ax.set_xticks(range(0,n+1,int(n/10)))
ax.set_yticks(np.arange(0,1,.1))
ax.tick_params(axis='x', colors='red')
ax.tick_params(axis='y', colors='red')
plt.style.use('dark_background')
line, = ax.plot([],[],'r-')

r_slider_ax = fig.add_axes([0.13, .035, .7, .02])
r_slider_ax.tick_params(axis='y', colors='red')
r_slider = Slider(r_slider_ax, 'Growth Ratio', valmin = 0, valmax = 4, valinit = 3.759816)
r_slider.label.set_size(10)

def animate(j): #for changing growth rate
    r = r_slider.val
    p.append([initial])
    for i in range(n): #for changing the population
        p[j].append(rec(r, p[j][-1]))
    
    y = p[j]
    x = range(n+1)
    line.set_data([x, y])
    return line,

anim = anime.FuncAnimation(fig, animate, frames=None, interval=100)
plt.show()
