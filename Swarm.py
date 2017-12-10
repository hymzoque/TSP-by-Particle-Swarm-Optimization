# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:54:53 2017

@author: hymzoque
"""
import random
import Particle
import Updator

class Swarm:
    
    __SWARM_SIZE = 1000
    __NEIGHBOR_NUM = 3
    __LOOP_TIME = 500
    BY_NEIGHBOR = 1
    BY_BEST = 2
    # init the swarm by random
    def __init__(self, distances, 
                 swarm_size=__SWARM_SIZE, neighbor_num=__NEIGHBOR_NUM, loop_time=__LOOP_TIME,
                 update_mode=BY_NEIGHBOR):
        self.__distances = distances
        self.__swarm_size = swarm_size
        self.__neighbor_num = neighbor_num
        self.__loop_time = loop_time
        self.__update_mode = update_mode
        self.updator = Updator.Updator(distances)
        
        self.__create_swarm()
    
    
    def __create_swarm(self):
        # generate initial particles by random
        self.particles = []
        marks = list(range(self.__swarm_size - 1))
        for i in range(self.__swarm_size):
            # randomly choose neighbors
            neighbors = random.sample(marks, self.__neighbor_num)
            p = Particle.random_particle(self.__distances, neighbors)
            self.particles.append(p)
        self.best = max(self.particles)
    
    def evolution(self):
        for i in range(self.__loop_time):
            # generate new group
            new_group = []
            for par in self.particles:
                newone = self.__update(par)
                if (newone == None or par.distance < newone.distance):
                    new_group.append(par)
                else:
                    new_group.append(newone)
            self.particles = new_group
            self.best = max(self.particles)
#            print("- " + str(i) + " - : " + str(self.best.distance))
# =============================================================================
#             file.write("- " + str(i) + " - " + str(len(set(new_group))) + " : " + str(self.best.distance))
#             file.write("\n")
# =============================================================================
        return self.best
    
    # perform good
    def __update_by_neighbors(self, particle):
        neighbors = particle.neighbors
        # find the best neighbor
        neighbor_best = None
        for index in neighbors:
            par = self.particles[index]
            if (neighbor_best == None or par.distance < neighbor_best.distance):
                neighbor_best = par
        return self.updator.update(particle, neighbor_best)
    
    # perform not good
    def __update_by_best(self, particle):
        return self.updator.update(particle, self.best)
    
    def __update(self, particle):
        if (self.__update_mode == Swarm.BY_NEIGHBOR):
            return self.__update_by_neighbors(particle)
        else:
            return self.__update_by_best(particle)
        
    