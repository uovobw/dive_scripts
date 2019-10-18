#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
from pprint import pprint

from lib import *

bottles = []

def get_bottles():
    more = True
    while more:
        bottle_type = input("Bottle type? {}: ".format([x for x in BOTTLES.keys()]))
        if bottle_type not in BOTTLES.keys():
            print("Invalid or unknown bottle. Available ones are: {}".format([x for x in BOTTLES.keys()]))
            continue
        bottle_pressure = int(input("Bottle pressure for {}: ".format(bottle_type)))
        reserve = float(input("Reserve in bars: "))
        bottles.append({
            "type": bottle_type,
            "pressure": bottle_pressure,
            "reserve": reserve
        })
        cont = input("Add another bottle? (only 'y' will continue)")
        if cont != "y":
            more = False

if __name__ == "__main__":
    print("Calculating Maximum time ad depth for bottles")
    get_bottles()
    pprint(bottles)
    depth = int(input("Depth of bottom segment (meters): "))
    ata = depth_to_ata(depth)
    sac = int(input("SAC of diver at surface in l/minute: "))
    total_time = []
    for bottle_data in bottles:
        bottle_type = bottle_data["type"]
        stats = BOTTLES[bottle_type]
        consumption_min = consumption_per_minute(depth, stats["volume"])
        available_bars = bottle_data["pressure"] - bottle_data["reserve"]
        minutes = available_bars / consumption_min
        total_time.append({
            "bottle": bottle_type,
            "consumption_per_minute": consumption_min,
            "minutes": minutes
        })
    print("Maximum time at depth: {}".format(math.floor(sum([x["minutes"] for x in total_time]))))
