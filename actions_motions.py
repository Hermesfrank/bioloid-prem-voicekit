#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.ontology import *
import actions_leds
import serial
import time

# open serial port
ser = serial.Serial(port='/dev/ttyUSB0', baudrate=57600, timeout=1)


class Motions(object):
    """Class used to define which command(s) to send to robot
    """

# --> Sub callback function, one per intent
def move_forward(hermes, intent_message):
    # terminate the session first if not continue
    hermes.publish_end_session(intent_message.session_id, "")

    # action code goes here...
    print('[Received] intent: {}'.format(intent_message.intent.intent_name))

#    actions_leds.initialize_pi_hat_leds()

    # send command to bot
    ser.write(b'\xFF\x55\x01\xFE\x00\xFF')
    # terminates action at one step
    ser.write(b'\xFF\x55\x00\xFF\x00\xFF')

    # if need to speak the execution result by tts
    hermes.publish_start_session_notification(intent_message.site_id, "Going forward", "")


def move_back(hermes, intent_message):
    # terminate the session first if not continue
    hermes.publish_end_session(intent_message.session_id, "")

    # action code goes here...
    print('[Received] intent: {}'.format(intent_message.intent.intent_name))

#    actions_leds.initialize_pi_hat_leds()

    # send command to bot
    ser.write(b'\xFF\x55\x02\xFD\x00\xFF')
    ser.write(b'\xFF\x55\x00\xFF\x00\xFF')

    # if need to speak the execution result by tts
    hermes.publish_start_session_notification(intent_message.site_id, "Backing up", "")


def turn_right(hermes, intent_message):
    # terminate the session first if not continue
    hermes.publish_end_session(intent_message.session_id, "")

    # action code goes here...
    print('[Received] intent: {}'.format(intent_message.intent.intent_name))

#    actions_leds.initialize_pi_hat_leds()

    # send command to bot
    ser.write(b'\xFF\x55\x08\xF7\x00\xFF')
    ser.write(b'\xFF\x55\x00\xFF\x00\xFF')

    # if need to speak the execution result by tts
    hermes.publish_start_session_notification(intent_message.site_id, "Turning right", "")


def turn_left(hermes, intent_message):
    # terminate the session first if not continue
    hermes.publish_end_session(intent_message.session_id, "")

    # action code goes here...
    print('[Received] intent: {}'.format(intent_message.intent.intent_name))

#    actions_leds.initialize_pi_hat_leds()

    # send command to bot
    ser.write(b'\xFF\x55\x04\xFB\x00\xFF')
    ser.write(b'\xFF\x55\x04\xFB\x00\xFF')
    ser.write(b'\xFF\x55\x04\xFB\x00\xFF')
    time.sleep(1)
    ser.write(b'\xFF\x55\x00\xFF\x00\xFF')

    # if need to speak the execution result by tts
    hermes.publish_start_session_notification(intent_message.site_id, "Turning left", "")


def do_handstand(hermes, intent_message):
    # terminate the session first if not continue
    hermes.publish_end_session(intent_message.session_id, "")

    # action code goes here...
    print('[Received] intent: {}'.format(intent_message.intent.intent_name))

    actions_leds.initialize_pi_hat_leds()

    # send command to bot
    ser.write(b'\xFF\x55\x18\xE7\x00\xFF')

    # if need to speak the execution result by tts
    hermes.publish_start_session_notification(intent_message.site_id, "I can do a handstand", "")


def do_pushup(hermes, intent_message):
    # terminate the session first if not continue
    hermes.publish_end_session(intent_message.session_id, "")

    # action code goes here...
    print('[Received] intent: {}'.format(intent_message.intent.intent_name))

    actions_leds.initialize_pi_hat_leds()

    # send command to bot
    ser.write(b'\xFF\x55\x14\xEB\x00\xFF')

    # if need to speak the execution result by tts
    hermes.publish_start_session_notification(intent_message.site_id, "I will do three pushups", "")


def pound_chest(hermes, intent_message):
    # terminate the session first if not continue
    hermes.publish_end_session(intent_message.session_id, "")

    # action code goes here...
    print('[Received] intent: {}'.format(intent_message.intent.intent_name))

    # Smile and glitter
    actions_leds.smile()
    actions_leds.initialize_pi_hat_leds()

    # send command to bot
    ser.write(b'\xFF\x55\x21\xDE\x00\xFF')

    # if need to speak the execution result by tts
    hermes.publish_start_session_notification(intent_message.site_id, "I am a proud robot", "")

    time.sleep(2)
    # Return to neutral face
    actions_leds.straight_face()
