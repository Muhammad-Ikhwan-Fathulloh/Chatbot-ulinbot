# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from pyowm import OWM

class ActionNama(Action):

    def name(self) -> Text:
        return "action_nama_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        nama = tracker.get_slot("nama")
        dispatcher.utter_message(text= "Halo {} !".format(nama))
        return []

key = "9eda082491667401cd76dde164af3199"

class ActionCuaca(Action):

    def name(self) -> Text:
        return "action_cuaca"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        loc = tracker.get_slot("loc")
        owm = OWM(key)
        mgr = owm.weather_manager()

        observation = mgr.weather_at_place(loc)
        w = observation.weather

        mess1 = f"Laporan Cuaca di {loc}"
        mess2 = f"Suhu (celsius) : {w.temperature('celsius')['temp']}"
        mess3 = f"Kecepatan Angin : {w.wind()['speed']}Km/h"
        mess4 = f"Kelembaban : {w.humidity}%"
        mess5 = f"Status Cuaca : {w.detailed_status}."

        message = mess1 + '\n' + mess2 + '\n' + mess3 + '\n' + mess4 + '\n' + mess5
        dispatcher.utter_message(text=message)

        return []
