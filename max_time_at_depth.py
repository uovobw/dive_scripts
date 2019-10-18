#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
from pprint import pprint

from lib import *

if __name__ == "__main__":
    print("Calculating Maximum time ad depth for bottles")
    bottles = get_bottles(BOTTLES)
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
