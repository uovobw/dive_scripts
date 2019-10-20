#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from lib import *

def test_ead():
    eads = {
        (21, 10): 10,
        (21, 20): 20,
        (21, 30): 30,
        (21, 75): 75,
        (28, 20): 18,
        (28, 30): 26,
        (28, 40): 36,
        (28, 50): 45
    }
    for (fo2, depth), expected in eads.items():
        assert ead(fo2, depth) == expected
