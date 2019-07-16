#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.ontology import *
import grove.grove_temperature_humidity_sensor_sht3x

temperature_humidity_sensor = grove.grove_temperature_humidity_sensor_sht3x.Grove()

class Sensors(object):
    """Class used to wrap action code with mqtt connection

       Please change the name referring to your application
    """
def answer_temperature(hermes, intent_message):
    # terminate the session first if not continue
    hermes.publish_end_session(intent_message.session_id, "")

    # action code goes here...
    print('[Received] intent: {}'.format(intent_message.intent.intent_name))

    # In Fahrenheit - note that this is a dual sensor, so this picks off the first output

    temperature, _ = temperature_humidity_sensor.read()
    temperature = ((temperature * 9) / 5) + 32

    # if need to speak the execution result by tts
    hermes.publish_start_session_notification(intent_message.site_id,
                                              "The temperature in Fahrenheit is {} degrees".format(int(temperature)), "")

def answer_humidity(hermes, intent_message):
    # terminate the session first if not continue
    hermes.publish_end_session(intent_message.session_id, "")

    # action code goes here...
    print('[Received] intent: {}'.format(intent_message.intent.intent_name))

    # Note, this is a dual sensor so picking off the second output
    _, humidity = temperature_humidity_sensor.read()

    # if need to speak the execution result by tts
    hermes.publish_start_session_notification(intent_message.site_id, "The current inside humidity is {} percent".format(int(humidity)), "")
