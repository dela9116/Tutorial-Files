import numpy as np

class Node:
    def __init__(self):
        self.name = None
        self.x = None
        self.y = None

class Truss:
    def __init__(self, ):
        self.nodes = [] # an empty list of nodes
        self.nNodes = 0
        self.xAverage = 0
        self.yAverage = 0


    def ReadTrussData(self, data):
        #data is an array of strings, read from a Truss data file
        for line in data:  # loop over all the lines
            cells = line.strip().split(',')
            keyword = cells[0].lower()

            if keyword == 'node':
                thisnode=Node()
                thisnode.name = cells[1].strip()
                thisnode.x=float(cells[2].strip())
                thisnode.y=float(cells[3].strip())
                self.nodes.append(thisnode)
        self.UpdateTruss()


    def UpdateTruss(self):
        self.nNodes = len(self.nodes)
        xAverage = 0
        yAverage = 0
        for node in self.nodes:
            xAverage+= node.x
            yAverage+= node.y
        self.xAverage = xAverage/self.nNodes
        self.yAverage = yAverage/self.nNodes


