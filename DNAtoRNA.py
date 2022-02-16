"""
DNA to RNA
@author: Maia Kelly
"""

data = open("DNA.txt")
data = data.read()
print(data.replace("T", "U"))
