#!/usr/bin/env python3
import sys
import math

from lib import *

def ratio_for_bottle(bottle_size, sac=DEFAULT_BOTTOM_SAC, range_start=10, range_end=100):
    '''this function receives a bottle size in liters, a SAC in liters/minute and a start/end range
    depth in meters. for each 10 meters increment in that depth range it then calculates
    the bars consumed per minute (for the bottle size and SAC) and collects the value for the
    1 and 5 minutes intervals.'''
    cons = {}
    for depth in range(range_start, range_end, 10):
        this_bar_min = consumption_per_minute(depth, bottle_size, sac=sac)
        this_bar_5min = this_bar_min * 5
        cons[depth] = {
            1: this_bar_min,
            5: this_bar_5min
        }
    return cons

if __name__ == "__main__":
    '''this code uses the information provided by the ratio_for_bottle code to generate a viable
    "bottle factor" in bars per 5 minutes per ata of depth. for example: a double 12, of total volume
    24 liters, with a SAC of 20 liters per minute, is shown being consumed at the rate of 25 bars
    per 5 minutes at the depth of 50 meters. this info can be used to tailor the bottle factor to 
    a useful number when diving.'''
    print("Calculating Bottle Ratio at depths")
    bottle_size = float(input("Bottle size in liters (total volume liters):  "))
    sac = int(input("Single diver Surface Air Consumption (SAC in literls):  "))
    cons = ratio_for_bottle(bottle_size, sac=sac)
    for depth, data in cons.items():
        ata = depth_to_ata(depth)
        print("Depth: {} bars/5' {:.2f} / ata {}:  {:.2f}".format(depth,
                                                          data[5],
                                                          ata,
                                                          data[5] / ata))
