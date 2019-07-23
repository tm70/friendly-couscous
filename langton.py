# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:08:05 2019

@author: s4432989
"""

import numpy as np

class langton:
    def __init__(self, N = 256, startpos = [100,100], startdirn = 3, colours = 2, rule = "LR"):
        self.grid = np.zeros((N,N), np.uint)
        self.position = startpos
        self.direction = startdirn
        self.colours = colours
        self.rule = rule
        
    def getStates(self):
        return self.grid
    
    def getColours(self):
        return self.colours
    
    def evolve(self):
        if self.rule[self.grid[self.position[0], self.position[1]]] == 'L':
            self.direction = (self.direction - 1) % 4
        elif self.rule[self.grid[self.position[0], self.position[1]]] == 'R':
            self.direction = (self.direction + 1) % 4
        
        self.grid[self.position[0], self.position[1]] = (self.grid[self.position[0], self.position[1]] + 1) % self.colours
        
        try:
            if self.direction == 0:
                self.position[0] -= 1
            elif self.direction == 1:
                self.position[1] += 1
            elif self.direction == 2:
                self.position[0] += 1
            elif self.direction == 3:
                self.position[1] -= 1
        except:
            pass
        