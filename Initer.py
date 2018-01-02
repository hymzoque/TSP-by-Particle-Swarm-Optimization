# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:56:58 2017

@author: hymzoque
"""

import re
import math

class Initer:
    def __init__(self, dataset=52):
        self.__read_points(dataset)
        self.__calculate_distances()
    
    # read points
    def __read_points(self, dataset):
        self.points = []
        if (dataset == 52):
            data_file = open("berlin52.tsp", "r")
        elif (dataset == 130):
            data_file = open("ch130.tsp", "r")
        elif (dataset == 150):
            data_file = open("ch150.tsp", "r")
        else:
            data_file = open("a280.tsp", "r")
            
        for line in data_file.readlines():
            matchobj = re.match(" *\d+ +(\d+\.?\d*) +(\d+\.?\d*)",line)
            if matchobj:
                self.points.append([float(matchobj.group(1)), float(matchobj.group(2))])
        data_file.close()
        return self.points
    
    # calculate all point-to-point distances
    def __calculate_distances(self):
        self.distances = []
        for index_1 in range(len(self.points)):
            point_1 = self.points[index_1]
            distance_temp = []
            for index_2 in range(len(self.points)):
                point_2 = self.points[index_2]
                distance_temp.append(math.sqrt(
                        (point_1[0] - point_2[0])*(point_1[0] - point_2[0]) +
                        (point_1[1] - point_2[1])*(point_1[1] - point_2[1])))
            self.distances.append(distance_temp)
        return self.distances

