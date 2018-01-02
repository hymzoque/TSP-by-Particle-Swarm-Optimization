# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:55:12 2017

@author: hymzoque
"""

import random

import Particle

class Updator:
    def __init__(self, distances):
        self.__distances = distances
        self.count = 0
    
    # benchline
    # from order1 crossover method
    def update_benchline(self, reciever, insertor):
        p_re = reciever.path
        p_in = insertor.path
        length = len(p_re)
        # segmant length
        seg_len = random.randint(1, length / 2)
#        seg_len = 5
        p1 = random.randint(0, length - 1)
        p2 = p1 + seg_len
        if (p2 >= length):
            p2 -= length
        
        insection = [p_in[p1]]
        insection.extend(self.__sub(p_in, p1, p2))
        insection.append(p_in[p2])
        temp_reci = self.__minus(p_re, insection)
        if (p1 > p2):
            temp_reci.extend(insection)
            return Particle.Particle(temp_reci, reciever.neighbors, self.__distances)
        else:
            newone = temp_reci[:p1]
            newone.extend(insection)
            newone.extend(temp_reci[p1:])
            return Particle.Particle(newone, reciever.neighbors, self.__distances)
    
    
    # put the segment of insertor into the reciever
    def update(self, reciever, insertor):
        r_re = reciever.path
        r_in = insertor.path
        length = len(r_re)
        p1 = random.randint(0, length - 1)
        p2 = p1 + 1 if p1 != length - 1 else 0
        
        # p3 front p4 latter
        p3 = r_in.index(r_re[p1])
        p4 = r_in.index(r_re[p2])
        delta = p4 - p3
        if (delta < 0):
            delta = -delta
            p3, p4 = p4, p3
        # delta is num of point between p3 and p4
        delta -= 1
        # no addition
        if (delta == 0):
            return None
        else:
            self.count += 1
        # seek the shorter 
        if (delta > length / 2 - 1):
            delta = length - 2 - delta
            p3, p4 = p4, p3
        insection = self.__sub(r_in, p3, p4)
        newone = [r_re[p2]]
        newone.extend(self.__minus(self.__sub(r_re, p2, p1), insection))
        newone.append(r_re[p1])
        newone.extend(insection)
        
        return Particle.Particle(newone, reciever.neighbors, self.__distances)
    
    
    # @l list, @a begin, @b end
    # result sublist of l, not include a and b
    # b can < a
    # a != b
    def __sub(self, l, a, b):
        length = len(l)
        if (a >= length | b >= length):
            return
        sub = []
        count = a + 1 if a != length - 1 else 0
        while (count != b):
            sub.append(l[count])
            count += 1
            if (count >= length):
                count -= length
        return sub
    
    # list a minus list b(with order)
    # [1,5,6,7] - [4,9,5] = [1,6,7]
    # a and b are unique list
    def __minus(self, la, lb):
        newlist = []
        for item in la:
            if item not in lb:
                newlist.append(item)
        return newlist
