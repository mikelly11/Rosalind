"""
Counting DNA Strings
@author: Maia Kelly
"""
import re
data = open("DNA.txt")
data = data.read()
print("A =", len(re.findall("A", data)), "C =", len(re.findall("C", data)), "G =", len(re.findall("G", data)), "T =", len(re.findall("T", data)))


# Using Numpy
#import numpy as np
#data = np.genfromtxt("DNA.txt", dtype="str")
#astring = np.char.count(data, "A")
#cstring = np.char.count(data, "C")
#gstring = np.char.count(data, "G")
#tstring = np.char.count(data, "T")
#print("A = ", astring, "C = ", cstring, "G = ", gstring, "T = ", tstring)
