# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:55:57 2017

@author: hymzoque
"""

import timeit

import Swarm
import Initer

def PSO(dataset):
    initer = Initer.Initer(dataset)
    distances = initer.distances
    # about 10 seconds
    if (dataset == 52):
        s = Swarm.Swarm(distances, swarm_size=1000, loop_time=600, neighbor_num=3)
    # about 3-4 mins
    elif (dataset == 130):
        s = Swarm.Swarm(distances, swarm_size=1800, loop_time=3000, neighbor_num=3)

    with open("log_pso_" + str(dataset), "a") as f:
        best = s.evolution(doprint=1, file=f)
        best.writein(f)
        f.write("\n")
        best.printout()
    
def PSO_benchline_1(dataset):
    initer = Initer.Initer(dataset)
    distances = initer.distances
    # about 40 seconds
    if (dataset == 52):
        s = Swarm.Swarm(distances, swarm_size=1200, loop_time=800, neighbor_num=3)
    # about 16-17 mins
    elif (dataset == 130):
        s = Swarm.Swarm(distances, swarm_size=2000, loop_time=4000, neighbor_num=3)

    with open("log_benchline_1_" + str(dataset), "a") as f:
        best = s.evolution_benchline_1(doprint=1, file=f)
        best.writein(f)
        f.write("\n")
        best.printout()

def PSO_benchline_2(dataset):
    initer = Initer.Initer(dataset)
    distances = initer.distances
    # about 9-12 seconds
    if (dataset == 52):
        s = Swarm.Swarm(distances, swarm_size=1000, loop_time=600, neighbor_num=3)
    # about 2-3 mins
    elif (dataset == 130):
        s = Swarm.Swarm(distances, swarm_size=1800, loop_time=3000, neighbor_num=3)

    with open("log_benchline_2_" + str(dataset), "a") as f:
        best = s.evolution_benchline_2(doprint=1, file=f, by_neighbor_probability=0.95)
        best.writein(f)
        f.write("\n")
        best.printout()
#    
def test_PSO(dataset):
    open("log_pso_" + str(dataset), "w").close()
    
    t1 = timeit.Timer("PSO(" + str(dataset) + ")", "from main import PSO")
    for i in range(5):
        time = t1.timeit(number=1)
        with open("log_pso_" + str(dataset), "a") as f:
            f.write("use time : ")
            f.write(str(time))
            f.write("\n\n")

def test_PSO_benchline_1(dataset):
    open("log_benchline_1_" + str(dataset), "w").close()
    
    t1 = timeit.Timer("PSO_benchline_1(" + str(dataset) + ")", "from main import PSO_benchline_1")
    for i in range(5):
        time = t1.timeit(number=1)
        with open("log_benchline_1_" + str(dataset), "a") as f:
            f.write("use time : ")
            f.write(str(time))
            f.write("\n\n")

def test_PSO_benchline_2(dataset):
    open("log_benchline_2_" + str(dataset), "w").close()
    
    t1 = timeit.Timer("PSO_benchline_2(" + str(dataset) + ")", "from main import PSO_benchline_2")
    for i in range(5):
        time = t1.timeit(number=1)
        with open("log_benchline_2_" + str(dataset), "a") as f:
            f.write("use time : ")
            f.write(str(time))
            f.write("\n\n")
    
# 130tsp global best distance 6110.86094968039

#PSO_benchline_2(52)
#PSO_benchline_1(130)
#PSO(130)
#test_PSO(130)
#test_PSO_benchline_1(130)
#test_PSO_benchline_2(130)

