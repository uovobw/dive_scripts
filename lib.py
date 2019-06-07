#!/usr/bin/env python3
import sys
import math

MIN_MIN_GAS = 40

NX_50_DEPTH = 21

WORK_ASCENT_SPEED = 9
DECO_ASCENT_SPEED = 3

DEFAULT_BOTTLE_PRESSURE = 240

DEFAULT_DYNAMIC_SAC = 30
DEFAULT_BOTTOM_SAC = 20
DEFAULT_DECO_SAC = 15

def ead(o2, depth):
    '''returns the equivalent air depth for a given nitrox mix'''
    fraction_o2 = percentage_to_fraction(o2)
    fraction_n2 = 1.0 - fraction_o2
    return math.ceil(((depth + 10.0) * (fraction_n2 / 0.79)) - 10.0)

def end(o2, he, depth):
    '''returns the END of a gas given in standard form (like 18/45)'''
    fraction_he = percentage_to_fraction(he)
    return math.ceil(((depth + 10.0) * (1.0 - fraction_he)) - 10.0) 
    
def narcotic_fraction(o2, he):
    '''returns the narcotic fraction of a given trimix gas in standard form (like 18/45)'''
    fraction_o2 = percentage_to_fraction(o2)
    fraction_he = percentage_to_fraction(he)
    narcotic = 1.0 - fraction_o2
    return narcotic

def partial_pressure(percentage, depth):
    '''returns the partial pressure of a given percentage of a gas
    at a given depth'''
    ata = depth_to_ata(depth)
    fraction = percentage_to_fraction(percentage)
    return round(ata * fraction, 2)

def percentage_to_fraction(percentage):
    '''returns the fraction (0.0-1.0) given a percentage of gas (0-100)'''
    return float(percentage / 100.0)

def fraction_to_percentage(fraction):
    '''returns the percentage (0-100) given a fraction of gas (0.0-1.0)'''
    return fraction * 100.0
    
def avg_pressure(start, end):
    '''returns average pressure from ATAstart to ATAend'''
    return round((start + end) / 2, 1)

def depth_to_ata(depth):
    '''returns the pressure in ATA given a depth in meters'''
    return (depth / 10.0) + 1.0

def ascent_time(depth, change=NX_50_DEPTH, ascent_speed=DECO_ASCENT_SPEED):
    '''returns the time in minutes necessary to get to the first gas change.
    change is in meters, ascent_speed in m/minute
    '''
    return math.ceil((depth - change) / ascent_speed)

def total_volume(bottle_size, pressure=DEFAULT_BOTTLE_PRESSURE):
    '''returns the volume in liters of a tank of given size in liters and pressure in bar'''
    return bottle_size * pressure

def minutes_to_gas_change(depth, change=NX_50_DEPTH):
    '''returns the total minutes necessary to calculate minimum gas between two depths'''
    total_time = 1 + ascent_time(depth, change=change) + 1
    return total_time

def bottle_duration(consumption, pressure, empty_pressure=0):
    '''returns the duration in minutes of bottle when used with a consumption rate in
    bars/minute, starting at a given pressure (bars) and being considered empty at a
    given pressure (bars)'''
    available = pressure - empty_pressure
    return math.floor(available / consumption)

def liters_to_bars(liters, bottle_size, round=False):
    '''returns the bars corresponding to a given volume in a given bottle_size in liters'''
    if round:
        return math.ceil(liters / bottle_size)
    else:
        return liters / bottle_size

