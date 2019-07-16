#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import board
import adafruit_dotstar as dotstar

# Using a DotStar Digital LED Matrix with 64 LEDs connected to digital pins
dots = dotstar.DotStar(board.D13, board.D12, 64, brightness=0.1)


class LEDs(object):
    """Class used to set up
       face LED-matrix animations
    """


def initialize_matrix():
    dots.fill((0, 0, 0))


def initialize_face():
    # Left eye
    dots[49] = (255, 255, 255)
    dots[50] = (255, 255, 255)
    dots[57] = (255, 255, 255)
    dots[58] = (255, 255, 255)
    # Right eye
    dots[53] = (255, 255, 255)
    dots[54] = (255, 255, 255)
    dots[61] = (255, 255, 255)
    dots[62] = (255, 255, 255)
    # Main part of mouth
    dots[18] = (255, 255, 255)
    dots[19] = (255, 255, 255)
    dots[20] = (255, 255, 255)
    dots[21] = (255, 255, 255)
    dots[10] = (255, 255, 255)
    dots[11] = (255, 255, 255)
    dots[12] = (255, 255, 255)
    dots[13] = (255, 255, 255)
    # Neutral expression
    dots[16] = (255, 255, 255)
    dots[17] = (255, 255, 255)
    dots[22] = (255, 255, 255)
    dots[23] = (255, 255, 255)
