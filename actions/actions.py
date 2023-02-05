# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import pandas as pd
import numpy as np
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.types import DomainDict
from rasa_sdk.executor import CollectingDispatcher



class ActionForPersonName(Action):

    def name(self) -> Text:
        return "action_for_person_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> List[EventType]:
        for data in tracker.latest_message['entities']:

            name = data['value']
            dispatcher.utter_message(text=f"Hi {name}, May I know What kind of body type? Thin or medium or heavy?")

            return [SlotSet("person_name",name)]
    

class ActionForBodyFrame(Action):

    def name(self) -> Text:
        return "action_for_body_frame"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> List[EventType]:
        for data in tracker.latest_message['entities']:
            body_frame = data['value']
            dispatcher.utter_message(response="utter_ask_for_appetite")
            return [SlotSet("body_frame",body_frame)]



class ActionForAppetite(Action):

    def name(self) -> Text:
        return "action_for_appetite"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> List[EventType]:
        for data in tracker.latest_message['entities']:
            appetite = data['value']
            dispatcher.utter_message(response="utter_ask_for_mind")
            return [SlotSet("appetite_type",appetite)]


class ActionForMind(Action):

    def name(self) -> Text:
        return "action_for_mind"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> List[EventType]:
        for data in tracker.latest_message['entities']:
            mind = data['value']
            dispatcher.utter_message(response="utter_ask_for_sleep")
            return [SlotSet("mind_type",mind)]


class ActionForSleep(Action):

    def name(self) -> Text:
        return "action_for_sleep"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> List[EventType]:
        for data in tracker.latest_message['entities']:
            sleep = data['value']
            dispatcher.utter_message(response="utter_ask_for_speech")
            return [SlotSet("sleep_type",sleep)]


   

class ActionForSpeech(Action):

    def name(self) -> Text:
        return "action_for_speech"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> List[EventType]:
        for data in tracker.latest_message['entities']:
            speech = data['value']
            dispatcher.utter_message(response="utter_ending_results")
            return [SlotSet("speech_type",speech)]
        

class ActionForResults(Action):

    def name(self) -> Text:
        return "action_for_results"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> List[EventType]:
        kapa = 0
        vata = 0
        pita = 0
        body_frame = tracker.get_slot('body_frame')
        if body_frame.lower() == "thin":
            vata+=10
        elif body_frame.lower() == "medium":
            pita+=10
        elif body_frame.lower() == "heavy":
            kapa+=10
        else:
            vata=kapa=pita=0
        
        appetite_type = tracker.get_slot('appetite_type')
        if appetite_type.lower() == "variable":
            vata+=10
        elif appetite_type.lower() == "good":
            pita+=10
        elif appetite_type.lower() == "slow":
            kapa+=10
        else:
            vata=kapa=pita=0

        mind_type = tracker.get_slot('mind_type')
        if mind_type.lower() == "restless":
            vata+=10
        elif mind_type.lower() == "analytical":
            pita+=10
        elif mind_type.lower() == "calm":
            kapa+=10
        else:
            vata=kapa=pita=0

        sleep_type = tracker.get_slot('sleep_type')
        if sleep_type.lower() == "interrupted":
            vata+=10
        elif sleep_type.lower() == "little interrupted":
            pita+=10
        elif sleep_type.lower() == "prolonged":
            kapa+=10
        else:
            vata=kapa=pita=0

        speech_type = tracker.get_slot('speech_type')
        if speech_type.lower() == "fast":
            vata+=10
        elif speech_type.lower() == "sharp":
            pita+=10
        elif speech_type.lower() == "monotonous":
            kapa+=10
        else:
            vata=kapa=pita=0

        final_results_dict = {"Vata": vata, "Kapha": kapa, "Pitta":pita}
        predicted_dosha = max(final_results_dict)

        dispatcher.utter_message(text=f"Given your characterstics, you are a {predicted_dosha}!")
        return []

