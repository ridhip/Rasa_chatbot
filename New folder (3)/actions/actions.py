from __future__ import absolute_import, division, unicode_literals
from typing import Text, List, Dict, Any
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet

import glob
import os
import requests


class ActionWeather(Action):
	def name(self):
		return 'action_weather'
	def run(self,
        	dispatcher,tracker,
       		domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		path = 'D:/Repository'
		files =[]
		TempList=[]
		loc = tracker.get_slot('location')
		for r, d, f in os.walk(path):
			for file in f:
				files.append(os.path.join(r, file))
		for f in files:
			filename = open(f, "r")
			text = filename.read().strip().split()
			if loc in text:
				dispatcher.utter_message(text=f)
				TempList.append(f)
		return [SlotSet('location',loc)]
