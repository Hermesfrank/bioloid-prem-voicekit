#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from snipsTools import SnipsConfigParser
# from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import grove.grove_temperature_humidity_sensor_sht3x
'''
CONFIG_INI = "config.ini"

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))
'''
class Sensors(object):
    """Class used to wrap action code with mqtt connection

       Please change the name referring to your application
    """
'''    
    def __init__(self):
        # get the configuration if needed
        try:
            self.config = SnipsConfigParser.read_configuration_file(CONFIG_INI)
            self.mqtt_address = self.config.get("secret").get("mqtt")
        except:
            self.config = None
            self.mqtt_address = MQTT_ADDR

        # start listening to MQTT
        self.start_blocking()
    # --> Sub callback function, one per intent
'''
def answer_temperature(hermes, intent_message):
    # terminate the session first if not continue
    hermes.publish_end_session(intent_message.session_id, "")

    # action code goes here...
    print('[Received] intent: {}'.format(intent_message.intent.intent_name))

    # In Fahrenheit - note that this is a dual sensor, so this picks off the first output
    temperature_humidity_sensor = grove.grove_temperature_humidity_sensor_sht3x.Grove()
    temperature, _ = temperature_humidity_sensor.read()
    temperature = ((temperature * 9) / 5) + 32

    # if need to speak the execution result by tts
    hermes.publish_start_session_notification(intent_message.site_id,
                                              "The temperature in Fahrenheit is {} degrees".format(int(temperature)), "")
'''        
    # --> Register callback function and start MQTT
    def start_blocking(self):
        with Hermes(self.mqtt_address) as h:
            h.subscribe_intents(self.master_intent_callback).start()
'''
'''
if __name__ == "__main__":
    Sensors()
'''