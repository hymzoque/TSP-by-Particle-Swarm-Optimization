# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:55:40 2017

@author: hymzoque
"""

import random
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt

class Particle:
    
    # init
    def __init__(self, path, neighbors, distances):
        self.path = path
        self.neighbors = neighbors
        self.__distances = distances
        self.__calculate_distance()
        
    # calculate path distance of gene
    def __calculate_distance(self):
        self.distance = 0.0
        for index in range(len(self.path) - 1):
            p1 = self.path[index]
            p2 = self.path[index + 1]
            self.distance += self.__distances[p1][p2]
        self.distance += self.__distances[self.path[len(self.path) - 1]][self.path[0]]
        return self.distance
    
    # print out infomation of this gene
    def printout(self):
        print(self.path)
        print("distance : " + str(self.distance))
        
    # draw out this gene
    def drawout(self, points, dataset=52):
        ax = plt.subplot()
        if (dataset == 52):
            x = 1800
            y = 1400
        elif (dataset == 130):
            x = 800
            y = 800
        ax.set_xlim(left=0, right=x)
        ax.set_ylim(bottom=0, top=y)
        for i in range(len(self.path)):
            p1 = self.path[i]
            p2 = self.path[i + 1] if i != len(self.path) - 1 else self.path[0]
            (x, y) = zip(*[points[p1], points[p2]])
            ax.add_line(Line2D(x, y, lineWidth=1, color='black'))
        plt.plot()
        plt.show()
        self.printout()
    
    def writein(self, file):
        file.write(str(self.path))
        file.write("\ndistance : ")
        file.write(str(self.distance))
        file.write("\n")
    
    def __eq__(self, other):
        return other != None and self.distance == other.distance
    def __gt__(self, other):
        return self.distance < other.distance
    def __hash__(self):
        return hash(self.distance)
    
# generate path by random
def random_particle(distances, neighbors):
    l = list(range(len(distances)))
    random.shuffle(l)
    return Particle(l, neighbors, distances)



