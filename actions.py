# actions/actions.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideAssignmentDeadline(Action):
    def name(self) -> Text:
        return "action_provide_assignment_deadline"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course = next(tracker.get_latest_entity_values("course"), None)
        if course:
            # Fetch deadline from your database or API
            deadline = "2025-03-15"  # Example static deadline
            dispatcher.utter_message(text=f"The deadline for {course} is {deadline}.")
        else:
            dispatcher.utter_message(text="Please specify the course name.")
        return []

class ActionShareClassSchedule(Action):
    def name(self) -> Text:
        return "action_share_class_schedule"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        day = next(tracker.get_latest_entity_values("day"), None)
        if day:
            # Fetch schedule from your database or API
            schedule = "Math at 10 AM, Physics at 2 PM"  # Example static schedule
            dispatcher.utter_message(text=f"Your schedule for {day} is: {schedule}.")
        else:
            dispatcher.utter_message(text="Please specify the day.")
        return []
