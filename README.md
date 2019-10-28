# BIG FAT DISCLAIMER

ONLY AN ABSOLUTE MADMAN WOULD USE *ANYTHING* IN THIS REPO AS INDICATION TO CONDUCT ANY REAL WORLD DIVE.

ALL THAT IS IN THIS CODE IS JUST FOR *FUN* AND DOES NOT SUBSTITUTE PROPER DIVER TRAINING, PLANNING AND EXECUTION.

THE AUTHOR DECLINE ALL AND ANY RESPONSABILITY FOR ANY DEATH OR INJURY THAT MIGHT RESULT FROM EVEN READING
THIS CODE, LET ALONE USE IT IN ANY REAL WORLD SCENARIO.

PLEASE MAKE SURE YOU KNOW WHAT YOU ARE DOING WHEN DIVING AND NEVER EVER RELY ONLY ON BUGGY, INCOMPLETE AND
BAD CODE WRITTEN BY SOME UNKNOWN PERSON ON THE INTERNET. *YOU* *HAVE* *BEEN* *WARNED*.

**ALL OF THIS CODE IS ABSOLUTELY NOT LICENSED NOR ENDORSEB BY GUE OR ANY OF ITS REPRESENTATIVES, HAS NOTHING
TO DO WITH GUE AND ALL OF ITS ERRORS AND MISINTERPRETATIONS ARE SOLELY RESPONSABILITY OF THE AUTHOR** 

# Scuba diving planning scripts

These are some "utility scripts" that i wrote during and after the GUE Tech 1 course. I use them to get an idea
of the various gas pressures, dive lenghts, consumptions and so on when planning a dive. Due to the delicate nature 
of the matter at hand, my very limited and partial experience and my extremely poor programming skills the software
does not even _consider_ doing decompression calculations.

## Requirements

You need to have python installed on the machine, then install the requirements with the
```
pip install -r requirements.txt
```
command and then run the various script with 
```
python <script_name>.py
```

## Structure

The main code, barring some horrendous python floating point operation errors, lives in the `lib.py` file that is
imported from all other scripts. They usually run with a prompt and are pretty self explanatory. When not otherwise
specified the units are in meters, bars, minutes and liters.

## Tests

Tests use the `pytest` suite and cover a little of the code, with more and more coming as time passes. I have checked
most of the values with the `VPlanner` and `DecoPlanner` softwares.

