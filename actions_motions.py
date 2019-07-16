#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.ontology import *
import serial

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=57600, timeout=1)


class Motions(object):
    """Class used to define which command to send to robot

    """
# --> Sub callback function, one per intent


def move_forward(hermes, intent_message):
    # terminate the session first if not continue
    hermes.publish_end_session(intent_message.session_id, "")

    # action code goes here...
    print('[Received] intent: {}'.format(intent_message.intent.intent_name))

    # send command to bot
    ser.write(b'\xFF\x55\x01\xFE\x00\xFF')
    ser.write(b'\xFF\x55\x00\xFF\x00\xFF')

    # if need to speak the execution result by tts
    hermes.publish_start_session_notification(intent_message.site_id, "Going forward, Papa", "")
