#!/usr/bin/env python3
import sys
import math

from lib import *

def consumption_per_minute(depth, bottle_size, sac=DEFAULT_BOTTOM_SAC):
    sac = float(sac)
    ata = depth_to_ata(depth)
    liters_per_minute = ata * sac
    bars = liters_to_bars(liters_per_minute, bottle_size)
    print("Depth: {}\nATA@Depth: {}\nLiters per minute @{}l/m {}\nBars of bottle {}: {:.1f}".format(depth, ata, sac, liters_per_minute, bottle_size, bars))
    return bars

if __name__ == "__main__":
    print("Calculating Gas Consumption")
    if len(sys.argv) != 1:
        bottle_size = float(sys.argv[1])
        depth = float(sys.argv[2])
        sac = float(sys.argv[3])
        pressure = int(sys.argv[4])
    else:
        bottle_size = float(input("Bottle size in liters (total volume liters):  "))
        depth = float(input("Depth (meters):  "))
        sac = float(input("Diver Surface Air Consumption (SAC in literls):  "))
        pressure = int(input("Enter pressure (bars):   "))
    cpm = consumption_per_minute(depth, bottle_size, sac=sac)
    cpm_5 = cpm * 5.0
    print("Consumption bar per 1 minute:  {:.1f} (rounded: {})".format(cpm, round(cpm)))
    print("Consumption bar per 5 minute:  {:.1f} (rounded {})".format(cpm_5, round(cpm_5)))
    print("Duration of bottle (to 30 bars):   {}".format(bottle_duration(cpm, pressure, empty_pressure=30))) 
    print("Duration of bottle (to empty):   {}".format(bottle_duration(cpm, pressure)))
