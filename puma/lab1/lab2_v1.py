import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_ylim((0,1))

low = 0 #inclusive
high = 10 #exclusive
    
def gen():
    yield np.random.randint(low, high)
    
def calcProbability():
    for k, v in rollsDict.items():
        rollProbabilities[k] = v/numOfRolls

def calcMatrixProbability():
    for i in range(high):
        for j in range(high):
            probabilityMatrix[i][j] = rollProbabilities.get(i, 0) * rollProbabilities.get(j, 0)

rollsDict = {}
bins = [i for i in range(high)]
rollProbabilities = {}
numOfRolls = 0
probabilityMatrix = np.zeros((high,high))

def animate(i):
    currentRoll = next(gen())
    rollsDict[currentRoll] = rollsDict.get(currentRoll, 0) + 1
    global numOfRolls
    numOfRolls += 1
    print('Rolls:', rollsDict)
    calcProbability()
    print('Probabilities:', rollProbabilities)
    calcMatrixProbability()
    ax1.clear()
    ax1.imshow(probabilityMatrix, cmap='hot', interpolation='nearest')
    
anim = animation.FuncAnimation(fig, animate, interval=100)
plt.show()