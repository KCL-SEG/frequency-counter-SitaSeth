"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    for x in items:
      
        x=str(x)
        if x in frequencies.keys():
            frequencies[x] = frequencies[x] + 1
        else:
            frequencies[x] = 1
    return frequencies
