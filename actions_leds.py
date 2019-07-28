#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time
import board
import adafruit_dotstar as dotstar

# Using a DotStar Digital LED Matrix with 64 LEDs connected to digital pins
dots = dotstar.DotStar(board.D13, board.D12, 64, brightness=0.1)
# Using a Respeaker 2-Mics Pi Hat with its 3 APA102 LEDs connected to hardware SPI
chest = dotstar.DotStar(board.SCK, board.MOSI, 3, brightness=0.1)


class LEDs(object):
    """Class used to set up
       face LED-matrix animations
    """


def initialize_pi_hat_leds():
    # a random color 0 -> 224
    def random_color():
        return random.randrange(0, 7) * 32

    # MAIN LOOP
    num = 1
    n_chest = len(chest)
    while num < 50:
        # Fill each dot with a random color
        for dot in range(n_chest):
            chest[dot] = (0, 0, random_color())
        num = num + 1
        time.sleep(.1)


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


def smile():
    dots[16] = (0, 0, 0)
    dots[24] = (255, 255, 255)
    dots[31] = (255, 255, 255)
    dots[23] = (0, 0, 0)


def straight_face():
    dots[16] = (255, 255, 255)
    dots[24] = (0, 0, 0)
    dots[31] = (0, 0, 0)
    dots[8] = (0, 0, 0)
    dots[15] = (0, 0, 0)
    dots[23] = (255, 255, 255)


def frown():
    dots[8] = (255, 255, 255)
    dots[16] = (0, 0, 0)
    dots[23] = (0, 0, 0)
    dots[15] = (255, 255, 255)


def wink():
    dots[61] = (0, 0, 0)
    dots[62] = (0, 0, 0)
    time.sleep(.05)
    dots[53] = (0, 0, 0)
    dots[54] = (0, 0, 0)
    time.sleep(.05)
    dots[53] = (255, 255, 255)
    dots[54] = (255, 255, 255)
    time.sleep(.05)
    dots[61] = (255, 255, 255)
    dots[62] = (255, 255, 255)
