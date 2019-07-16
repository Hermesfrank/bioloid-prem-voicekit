#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import board
import adafruit_dotstar as dotstar

# Using a DotStar Digital LED Matrix with 64 LEDs connected to digital pins
dots = dotstar.DotStar(board.D13, board.D12, 64, brightness=0.1)

class LEDs(object):
    """Class used to wrap action code with mqtt connection

       Please change the name referring to your application
    """
def initialize_matrix():
    dots.fill((0, 0, 0))
