#!/usr/bin/env python3
import sys
import math

BOTTLES = {
    "m18": {"max_pressure": 232, "fill_pressure": 210, "volume": 18.0, "bottom": True},
    "m15": {"max_pressure": 232, "fill_pressure": 210, "volume": 15.0, "bottom": True},
    "m12": {"max_pressure": 232, "fill_pressure": 210, "volume": 12.0, "bottom": True},
    "m10": {"max_pressure": 232, "fill_pressure": 210, "volume": 10.0, "bottom": True},
    "d20": {"max_pressure": 232, "fill_pressure": 210, "volume": 40.0, "bottom": True},
    "d18": {"max_pressure": 232, "fill_pressure": 210, "volume": 36.0, "bottom": True},
    "d16": {"max_pressure": 232, "fill_pressure": 210, "volume": 32.0, "bottom": True},
    "d15": {"max_pressure": 232, "fill_pressure": 210, "volume": 30.0, "bottom": True},
    "d12": {"max_pressure": 232, "fill_pressure": 210, "volume": 24.0, "bottom": True},
    "d10": {"max_pressure": 232, "fill_pressure": 210, "volume": 20.0, "bottom": True},
    "d8.5": {"max_pressure": 232, "fill_pressure": 210, "volume": 17.0, "bottom": True},
    "7l": {"max_pressure": 200, "fill_pressure": 190, "volume": 7.0, "bottom": False},
    "s80": {"max_pressure": 200, "fill_pressure": 190, "volume": 11.1, "bottom": False},
    "s40": {"max_pressure": 200, "fill_pressure": 180, "volume": 5.7, "bottom": False},
}

MIN_MIN_GAS = 40

NX_50_DEPTH = 21
OXYGEN_DEPTH = 6

DEC0_PO2 = 1.6
WORK_PO2 = 1.4
GUE_PO2 = 1.2
MIN_PO2 = 0.16

WORK_ASCENT_SPEED = 9
DECO_ASCENT_SPEED = 3

DEFAULT_BOTTLE_PRESSURE = 220

DEFAULT_DYNAMIC_SAC = 30
DEFAULT_BOTTOM_SAC = 20
DEFAULT_DECO_SAC = 15


def ead(o2, depth):
    """returns the equivalent air depth for a given nitrox mix"""
    fraction_o2 = percentage_to_fraction(o2)
    fraction_n2 = 1.0 - fraction_o2
    return math.ceil(((depth + 10.0) * (fraction_n2 / 0.79)) - 10.0)


def end(o2, he, depth):
    """returns the END of a gas given in standard form (like 18/45)"""
    fraction_he = percentage_to_fraction(he)
    return math.ceil(((depth + 10.0) * (1.0 - fraction_he)) - 10.0)


def mod(o2, po2=GUE_PO2):
    """returns the mod of a given percentage of o2 with a given maximum po2"""
    pctg = o2 / 100
    return math.floor(((po2 / pctg) * 10) - 10)


def narcotic_fraction(o2, he):
    """returns the narcotic fraction of a given trimix gas in standard form (like 18/45)"""
    fraction_o2 = percentage_to_fraction(o2)
    fraction_he = percentage_to_fraction(he)
    narcotic = 1.0 - fraction_o2
    return narcotic


def partial_pressure(percentage, depth):
    """returns the partial pressure of a given percentage of a gas
    at a given depth"""
    ata = depth_to_ata(depth)
    fraction = percentage_to_fraction(percentage)
    return round(ata * fraction, 2)


def percentage_to_fraction(percentage):
    """returns the fraction (0.0-1.0) given a percentage of gas (0-100)"""
    return float(percentage / 100.0)


def fraction_to_percentage(fraction):
    """returns the percentage (0-100) given a fraction of gas (0.0-1.0)"""
    return fraction * 100.0


def avg_pressure(start, end):
    """returns average pressure from ATAstart to ATAend"""
    return round((start + end) / 2, 2)


def depth_to_ata(depth):
    """returns the pressure in ATA given a depth in meters"""
    return (depth / 10.0) + 1.0


def ascent_time(depth, change=NX_50_DEPTH, ascent_speed=DECO_ASCENT_SPEED):
    """returns the time in minutes necessary to get to the first gas change.
    change is in meters, ascent_speed in m/minute
    """
    return math.ceil((depth - change) / ascent_speed)


def total_volume(bottle_size, pressure=DEFAULT_BOTTLE_PRESSURE):
    """returns the volume in liters of a tank of given size in liters and pressure in bar"""
    return bottle_size * pressure


def minutes_to_gas_change(depth, change=NX_50_DEPTH, ascent_speed=DECO_ASCENT_SPEED):
    """returns the total minutes necessary to calculate minimum gas between two depths"""
    total_time = 1 + ascent_time(depth, change=change, ascent_speed=ascent_speed)
    return total_time


def bottle_duration(consumption, pressure, empty_pressure=0):
    """returns the duration in minutes of bottle when used with a consumption rate in
    bars/minute, starting at a given pressure (bars) and being considered empty at a
    given pressure (bars)"""
    available = pressure - empty_pressure
    return math.floor(available / consumption)


def liters_to_bars(liters, bottle_size, round=False):
    """returns the bars corresponding to a given volume in a given bottle_size in liters"""
    if round:
        return math.ceil(liters / bottle_size)
    else:
        return liters / bottle_size


def consumption_per_minute(depth, bottle_size, sac=DEFAULT_BOTTOM_SAC, silent=True):
    """returns the consumption in bars/minute of a bottle of a given size for
    a given SAC"""
    sac = float(sac)
    ata = depth_to_ata(depth)
    liters_per_minute = ata * sac
    bars = liters_to_bars(liters_per_minute, bottle_size)
    if not silent:
        print(
            "Depth: {}\nATA@Depth: {}\nLiters per minute @{}l/m {}\nBars/minute of bottle {}: {:.1f}".format(
                depth, ata, sac, liters_per_minute, bottle_size, bars
            )
        )
    return bars


def get_bottles(available):
    bottles = []
    more = True
    while more:
        bottle_type = input("Bottle type? {}: ".format([x for x in available.keys()]))
        if bottle_type not in available.keys():
            print(
                "Invalid or unknown bottle. Available ones are: {}".format(
                    [x for x in available.keys()]
                )
            )
            continue
        bottle_pressure = int(input("Bottle pressure for {}: ".format(bottle_type)))
        reserve = float(input("Reserve in bars: "))
        bottles.append(
            {"type": bottle_type, "pressure": bottle_pressure, "reserve": reserve}
        )
        cont = input("Add another bottle? (only 'y' will continue)")
        if cont != "y":
            more = False
    return bottles
