#!/usr/bin/env python3
import sys
import math

# TODO: add check for python 3 to avoid numbers HORRENDOUS ERRORS

from lib import *


def minimum_gas(
    depth,
    bottle_size,
    change=NX_50_DEPTH,
    sac=DEFAULT_BOTTOM_SAC,
    ascent_speed=DECO_ASCENT_SPEED,
):
    """returns the amount in bar for a given bottle size for two divers ascending at a given ascent speed
    from a given depth in meters, using a given bottle_size in liters to a given gas change depth using a 
    given SAC
    """
    c = sac * 2
    a = avg_pressure(depth_to_ata(depth), depth_to_ata(change))
    t = minutes_to_gas_change(depth, change=change, ascent_speed=ascent_speed)
    total_liters = c * a * t
    bars_for_bottle = liters_to_bars(total_liters, bottle_size, round=True)
    print(
        "Consuption: {}\nATA avg: {}\nTime of ascent: {}\nTotal liters: {}\nBars in bottle (size: {}): {}".format(
            c, a, t, total_liters, bottle_size, bars_for_bottle
        )
    )
    return bars_for_bottle


if __name__ == "__main__":
    print("Calculating Minimum Gas")
    if len(sys.argv) != 1:
        bottle_size = int(sys.argv[1])
        start_depth = int(sys.argv[2])
        end_depth = int(sys.argv[3])
        ascent_speed = int(sys.argv[4])
        sac = int(sys.argv[5])
    else:
        bottle_size = int(input("Bottle size in liters (total volume liters):  "))
        start_depth = int(input("Starting depth of ascent (meters):  "))
        end_depth = int(input("First viable gas source depth (meters):  "))
        ascent_speed = int(
            input("Ascent speed from start depth to final depth (meters/minute):  ")
        )
        sac = int(input("Single diver Surface Air Consumption (SAC in literls):  "))
    min_gas = minimum_gas(
        start_depth, bottle_size, change=end_depth, sac=sac, ascent_speed=ascent_speed
    )
    if min_gas < MIN_MIN_GAS:
        print(
            "WARNING: minimum gas of {} is less than recommended {} bars. Rounding to {}".format(
                min_gas, MIN_MIN_GAS, MIN_MIN_GAS
            )
        )
        min_gas = MIN_MIN_GAS
    print("Minimum gas: {}".format(min_gas))
    print("Adjusted Minimum gas: {}".format(5 * math.ceil(min_gas / 5)))
