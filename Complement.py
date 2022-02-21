"""
Complementing a Strand of DNA
@author: Maia Kelly
"""
import re

data = open("DNA.txt")
data = data.read()
base_pairs = {"A":"T", "T":"A", "C":"G", "G":"C"}
def complementstrand(dict, data):
    complement = re.sub('.', lambda bp: dict.get(bp.group(), bp.group()), data)
    return complement[::-1]
complement = complementstrand(base_pairs, data)
print(complement)
