from drawShape import drawEdges 

def interpolate(V, E, depth, detail):
    if depth < 1 or detail < 2:
        return 
    for _ in range(depth):
        newEdges = []
        for e in E:
            p0 = e[0]
            p1 = e[1]
            interim = [(V[p0][0]+V[p1][0])/2, (V[p0][1]+V[p1][1])/2, (V[p0][2]+V[p1][2])/2]
            V.append(interim)
            interimIndex = V.length()-1
            newEdges.append([p0, interimIndex])
            newEdges.append([interimIndex, p1])


        


V = [[1, 1, 0], [2, 1, 0], [1, 2, 0]]
E = [[0, 1], [1, 2], [0, 2]]
F = [[0, 1, 2]]

interpolate(V, E, 1, 2)
drawEdges(E, V)