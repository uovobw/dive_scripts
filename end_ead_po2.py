#!/usr/bin/env python3
import sys
import math

# TODO: add check for python 3 to avoid numbers HORRENDOUS ERRORS

from lib import *

if __name__ == "__main__":
    print("Calculating END and Po2 for given O2 and He fractions")
    if len(sys.argv) != 1:
        o2 = int(sys.argv[1])
        he = int(sys.argv[2])
        depth = int(sys.argv[3])
    else:
        o2 = int(input("Oxygen gas fraction (x/100):  "))
        he = int(input("Helium gas fraction (x/100):  "))
        depth = int(input("Depth (meters):  "))
    if he == 0:
        ead = ead(o2, depth)
    end = end(o2, he, depth)
    partial_pressure_o2 = partial_pressure(o2, depth)
    print("Gas: {}/{} at {} meters:".format(o2, he, depth))
    if he == 0:
        print("EAD: {}".format(ead))
    print("END: {}".format(end))
    print("Po2: {}".format(partial_pressure_o2))


