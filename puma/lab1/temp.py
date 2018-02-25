import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import MultipleLocator
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_ylim((0,1))

low = 1 #inclusive
high = 7 #exclusive

def rollDice():
    return np.random.randint(low, high)

    
def gen():
    yield np.random.randint(low, high)
    
def calcProbability():
    for k, v in rollsDict.items():
        rollProbabilities[k] = v/numOfRolls
    
    
rollsDict = {}
bins = [i for i in range(high)]
rollProbabilities = {}
numOfRolls = 0

def animate(i):
    roll = next(gen())
    rollsDict[roll] = rollsDict.get(roll, 0) + 1
    global numOfRolls
    numOfRolls += 1
    print('Rolls:', rollsDict)
    calcProbability()
    print('Probabilities:', rollProbabilities)
    ax1.clear()
    ax1.bar(rollProbabilities.keys(), rollProbabilities.values())

    
anim = animation.FuncAnimation(fig, animate, interval=100)
plt.show()