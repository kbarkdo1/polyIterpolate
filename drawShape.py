import matplotlib.pyplot as plt

def drawLine(point1, point2):
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    plt.plot(x_values, y_values, 'k', linestyle="-")

def drawEdges(E, V):
    for p in E:
        drawLine(V[p[0]], V[p[1]])
    plt.show()



