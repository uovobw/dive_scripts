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

def avg_pressure(start, end):
    '''returns average pressure from ATAstart to ATAend'''
    return round((start + end) / 2, 1)

def depth_to_ata(depth):
    '''returns the pressure in ATA given a depth in meters'''
    return (depth / 10) + 1

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

def liters_to_bars(liters, bottle_size):
    '''returns the bars corresponding to a given volume in a given bottle_size in liters'''
    return math.ceil(liters / bottle_size)
