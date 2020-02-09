#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 14:58:18 2020

@author: alejandro
"""
import random 
health = 50
difficult = [1,2,3]
potion_health = int(random.randint(25,50)/difficult[0])
health += potion_health
print(health)
