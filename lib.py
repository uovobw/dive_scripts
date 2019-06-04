#!/usr/bin/env python3
import sys
import math

MIN_MIN_GAS = 40

def avg_pressure(start, end):
    '''returns average pressure from ATAstart to ATAend'''
    return round((start + end) / 2, 1)

def depth_to_ata(depth):
    '''returns the pressure in ATA given a depth in meters'''
    return (depth / 10) + 1

def ascent_time(depth, change=21, ascent_speed=3):
    '''returns the time in minutes necessary to get to the first gas change.
    change is in meters, ascent_speed in m/minute
    '''
    return math.ceil((depth - change) / ascent_speed)

def total_volume(bottle_size, pressure=240):
    '''returns the volume in liters of a tank of given size in liters and pressure in bar'''
    return bottle_size * pressure

def minutes_to_gas_change(depth, change=21):
    '''returns the total minutes necessary to calculate minimum gas between two depths'''
    total_time = 1 + ascent_time(depth, change=change) + 1
    return total_time

def liters_to_bars(liters, bottle_size):
    '''returns the bars corresponding to a given volume in a given bottle_size in liters'''
    return math.ceil(liters / bottle_size)
