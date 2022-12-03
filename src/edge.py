class Edge(object):
    def __init__(self, u, v, weight=0):
        self.u = u
        self.v = v
        self.weight = weight

    def getWeight(self):
        return self.weight

    def getVertices(self):
        return self.u, self.v

    def getOtherVertex(self, vertex):
        if vertex == self.u:
            return self.v
        elif vertex == self.v:
            return self.u
        else:
            raise ValueError("Vertex not incident to edge.")

    def __str__(self):
        return str(self.u) + '->' + str(self.v) + ' ' + str(self.weight)
