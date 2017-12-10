# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:55:57 2017

@author: hymzoque
"""

import timeit

import Swarm
import Initer

def PSO():
    initer = Initer.Initer()
    distances = initer.distances
    
    s = Swarm.Swarm(distances, swarm_size=1000, loop_time=600, neighbor_num=3, update_mode=1)
#    with open("log1", "w") as f:
#        best = s.evolution(f)
#        best.printout()
#    
    with open("log2", "a") as f:
        best = s.evolution()
        best.writein(f)
        f.write("update times : ")
        f.write(str(s.updator.count))
        f.write("\n")
#    
def runPSO():
    t1 = timeit.Timer("PSO()", "from main import PSO")
    for i in range(25):
        time = t1.timeit(number=1)
        with open("log2", "a") as f:
            f.write("use time : ")
            f.write(str(time))
            f.write("\n\n")
        
    
runPSO()