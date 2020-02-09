#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 16:00:43 2020

@author: alejandro
"""

# Ask user for name

name = input("What's your name? ")
print(name)
#Ask user for age
age = input("How old are you ")
print(age)
#Ask user for city
city = input("what city do you live in ")
print(city)

#Ask user what they enjoy
love = input("what do you love doing")
#Create output text
string = 'Your name is "{}", you are "{}" years old. Your live in "{}" and you love "{}"'
output = string.format(name,age,city,love)
#Print output to screen
print(output)