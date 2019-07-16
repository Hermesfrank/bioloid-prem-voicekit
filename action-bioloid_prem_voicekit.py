#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from snipsTools import SnipsConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *

import actions_sensors
import actions_leds

import grove.grove_relay
import grove.grove_temperature_humidity_sensor_sht3x
import serial
import time
import board
import adafruit_dotstar as dotstar

# Using a DotStar Digital LED Matrix with 64 LEDs connected to digital pins
dots = dotstar.DotStar(board.D13, board.D12, 64, brightness=0.1)

# Initialize face LED-matrix to all off
actions_leds.initialize_matrix()

# Initialize basic neutral face
actions_leds.initialize_face()

CONFIG_INI = "config.ini"

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


class VoiceKit(object):
    """Class used to wrap action code with mqtt connection
       Please change the name referring to your application
    """

    def __init__(self):
        # get the configuration if needed
        try:
            self.config = SnipsConfigParser.read_configuration_file(CONFIG_INI)
            self.mqtt_address = self.config.get("secret").get("mqtt")
        except :
            self.config = None
            self.mqtt_address = MQTT_ADDR

        self.relay = grove.grove_relay.Grove(12)
        self.temperature_humidity_sensor = grove.grove_temperature_humidity_sensor_sht3x.Grove()
        self.ser = serial.Serial(port='/dev/ttyUSB0', baudrate=57600, timeout=1)

        # start listening to MQTT
        self.start_blocking()
        
    # --> Sub callback function, one per intent
    def move_forward(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print('[Received] intent: {}'.format(intent_message.intent.intent_name))

        # send command to bot
        self.ser.write(b'\xFF\x55\x01\xFE\x00\xFF')
        self.ser.write(b'\xFF\x55\x00\xFF\x00\xFF')

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, "Going forward", "")

    def move_back(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print('[Received] intent: {}'.format(intent_message.intent.intent_name))

        # send command to bot
        self.ser.write(b'\xFF\x55\x02\xFD\x00\xFF')
        self.ser.write(b'\xFF\x55\x00\xFF\x00\xFF')

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, "Backing up", "")

    def turn_right(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print('[Received] intent: {}'.format(intent_message.intent.intent_name))

        # send command to bot
        self.ser.write(b'\xFF\x55\x08\xF7\x00\xFF')
        self.ser.write(b'\xFF\x55\x00\xFF\x00\xFF')

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, "Turning right", "")

    def turn_left(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print('[Received] intent: {}'.format(intent_message.intent.intent_name))

        # send command to bot
        self.ser.write(b'\xFF\x55\x04\xFB\x00\xFF')
        self.ser.write(b'\xFF\x55\x00\xFF\x00\xFF')

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, "Turning left", "")

    def do_handstand(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print('[Received] intent: {}'.format(intent_message.intent.intent_name))

        # send command to bot
        self.ser.write(b'\xFF\x55\x18\xE7\x00\xFF')

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, "I can do a handstand", "")

    def do_pushup(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print('[Received] intent: {}'.format(intent_message.intent.intent_name))

        # send command to bot
        self.ser.write(b'\xFF\x55\x14\xEB\x00\xFF')

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, "I can do a pushup", "")

    def pound_chest(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print('[Received] intent: {}'.format(intent_message.intent.intent_name))

        # Smile
        actions_leds.smile()

        # send command to bot
        self.ser.write(b'\xFF\x55\x21\xDE\x00\xFF')

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, "I am a proud robot", "")

        time.sleep(2)
        # Return to neutral face
        actions_leds.straight_face()

    def relay_on(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")
        
        # action code goes here...
        print('[Received] intent: {}'.format(intent_message.intent.intent_name))

        # First smile
        actions_leds.smile()
        # Then pound chest
        self.ser.write(b'\xFF\x55\x21\xDE\x00\xFF')

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, "I am a proud robot", "")
        time.sleep(1)

        # Return to neutral face
        actions_leds.straight_face()

    def relay_off(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print('[Received] intent: {}'.format(intent_message.intent.intent_name))

        # Wink
        # Return to neutral face
        actions_leds.wink()

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, "I've turned the relay off", "")

    # --> Master callback function, triggered every time an intent is recognized
    def master_intent_callback(self, hermes, intent_message):
        coming_intent = intent_message.intent.intent_name
        if coming_intent == 'Hermesf:relay_on':
            self.relay_on(hermes, intent_message)
        elif coming_intent == 'Hermesf:relay_off':
            self.relay_off(hermes, intent_message)
        elif coming_intent == 'Hermesf:move_forward':
            self.move_forward(hermes, intent_message)
        elif coming_intent == 'Hermesf:move_back':
            self.move_back(hermes, intent_message)
        elif coming_intent == 'Hermesf:turn_left':
            self.turn_left(hermes, intent_message)
        elif coming_intent == 'Hermesf:turn_right':
            self.turn_right(hermes, intent_message)
        elif coming_intent == 'Hermesf:do_pushup':
            self.do_pushup(hermes, intent_message)
        elif coming_intent == 'Hermesf:do_handstand':
            self.do_handstand(hermes, intent_message)
        elif coming_intent == 'Hermesf:pound_chest':
            self.pound_chest(hermes, intent_message)
        elif coming_intent == 'Hermesf:ask_temperature':
            actions_sensors.answer_temperature(hermes, intent_message)
        elif coming_intent == 'Hermesf:ask_humidity':
            actions_sensors.answer_humidity(hermes, intent_message)

    # --> Register callback function and start MQTT
    def start_blocking(self):
        with Hermes(self.mqtt_address) as h:
            h.subscribe_intents(self.master_intent_callback).start()


if __name__ == "__main__":
    VoiceKit()
