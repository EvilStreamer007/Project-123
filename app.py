import numpy as np
import random

rewards = np.array([
    [-1, -1, -1, -1, 0, -1],
    [-1,-1,-1,0,-1,100],
    [-1, -1, -1, 0, -1, -1],
    [-1, 0, 0, -1, -1, -1],
    [0, -1, -1, -1, -1, 100],
    [-1, -1, -1, -1, 0, 100]
])

def setInitialState():
    return np.random.randint(0,6) #provides a random number from 0 - 6

def getAction(currentstate, rewardMatrix):
    availableAction = []
    print("Reward Matrix \n", rewardMatrix)
    for action in enumerate(rewardMatrix[currentstate]): #enumerate - function that gives index and the element present at that index
        if action[1] != -1:
            availableAction.append(action[0])
        
    chooseAction = random.choice(availableAction)
    print("Random Choice of Action from",availableAction,"is",chooseAction)
    return chooseAction

currentstate = np.random.randint(0, 6)
action = getAction(currentstate, rewards)
print(action)