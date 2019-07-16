#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from snipsTools import SnipsConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *

import actions_sensors
import actions_leds
import actions_motions
import actions_chat

# Using a DotStar 8x8 LED Matrix connected to digital pins 12 and 13 to make faces - see actions_leds module
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
       connection
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
        self.ser = serial.Serial(port='/dev/ttyUSB0', baudrate=57600, timeout=1)

        # start listening to MQTT
        self.start_blocking()
        
    # --> Sub callback function, one per intent

    # See actions_* for these callbacks

    # --> Master callback function, triggered every time an intent is recognized
    def master_intent_callback(self, hermes, intent_message):
        coming_intent = intent_message.intent.intent_name

        # chat
        if coming_intent == 'Hermesf:when_born':
            actions_chat.when_born(hermes, intent_message)
        elif coming_intent == 'Hermesf:creator':
            actions_chat.creator(hermes, intent_message)
        elif coming_intent == 'Hermesf:belong_to':
            actions_chat.belong_to(hermes, intent_message)
        elif coming_intent == 'Hermesf:wink':
            actions_chat.wink(hermes, intent_message)
        elif coming_intent == 'Hermesf:smile':
            actions_chat.smile(hermes, intent_message)
        elif coming_intent == 'Hermesf:frown':
            actions_chat.frown(hermes, intent_message)

        # motions
        elif coming_intent == 'Hermesf:move_forward':
            actions_motions.move_forward(hermes, intent_message)
        elif coming_intent == 'Hermesf:move_back':
            actions_motions.move_back(hermes, intent_message)
        elif coming_intent == 'Hermesf:turn_left':
            actions_motions.turn_left(hermes, intent_message)
        elif coming_intent == 'Hermesf:turn_right':
            actions_motions.turn_right(hermes, intent_message)
        elif coming_intent == 'Hermesf:do_pushup':
            actions_motions.do_pushup(hermes, intent_message)
        elif coming_intent == 'Hermesf:do_handstand':
            actions_motions.do_handstand(hermes, intent_message)
        elif coming_intent == 'Hermesf:pound_chest':
            actions_motions.pound_chest(hermes, intent_message)

        # sensor reports
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
