import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_ylim((0,1))

size = 100
scale = 2
samples = 0
arr = {}

def generate_samples(samples):
    arr = {}
    for i in range(samples):
        arr[i] = np.random.exponential(scale=scale, size=size)
    return arr

def calculate_means(arrays):
    means = []
    for i in range(len(arrays)):
        mean = np.mean(arrays[i])
        means.append(mean)
    return means

n = 0
def animate(i):
    global n
    n += 1
    arrays = generate_samples(n)
    print(n)
    means = calculate_means(arrays)
    ax1.clear()
    ax1.hist(means)

    
anim = animation.FuncAnimation(fig, animate, interval=100)
plt.show()