import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

<<<<<<< HEAD
file = open("/Users/vidalattias/Desktop/projet1/hanoi_extension.csv")
=======
file = open("./hanoi2D.csv")
>>>>>>> 2534bee1344f789b9517fe2e2c39995f6dfbb962

discs = []
picks = []
totalMoves = []

#Used to skip the first iteration
boolHeader = True
for line in file:
    if boolHeader:
        boolHeader = False
    else:
        tabs = line.split(';')

        #We want to remove the ending newline
        tabs[2] = tabs[2].replace('\n', '')

        #Since there will be the same number of discs and picks multiple time,
        #we keep only one of each
        if int(tabs[0]) not in discs:
            discs.append(int(tabs[0]))
        if int(tabs[1]) not in picks:
            picks.append(int(tabs[1]))

        totalMoves.append(int(tabs[2]))
        
moves = [[0 for i in range(len(picks))] for j in range(len(discs))]

for i in range(len(discs)):
    for j in range(len(picks)):
        #We use logarithm to have a logarithmic scale
        moves[i][j] = np.log2(totalMoves[i*(len(picks))+j])


d, p = np.meshgrid(discs, picks)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#We do a transpose because the data has not the right dimension
ax.plot_wireframe(d, p, np.transpose(moves), rstride=1, cstride=1)

