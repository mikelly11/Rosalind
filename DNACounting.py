"""
Counting DNA Strings
@author: Maia
"""
import numpy as np

data = np.genfromtxt("DNA.txt", dtype="str")

astring = np.char.count(data, "A")
cstring = np.char.count(data, "C")
gstring = np.char.count(data, "G")
tstring = np.char.count(data, "T")

print("A = ", astring, "C = ", cstring, "G = ", gstring, "T = ", tstring)
