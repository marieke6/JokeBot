# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import secrets
import wikipedia


class ActionTellJoke(Action):

    def name(self) -> Text:
        return "action_tell_joke"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        jokeCat = ["good", "bad", "ok"]

        # Tell a random joke and ask for feedback
        dispatcher.utter_message(response="utter_" + secrets.choice(jokeCat) + "_joke")
        dispatcher.utter_message(response="utter_ask_for_feedback")

        return []


class ActionHandleFeedback(Action):

    def name(self) -> Text:
        return "action_handle_feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        recentSentiment = next(tracker.get_latest_entity_values("sentiment"),
                               None)  # Extracts the most recent sentiment
        if recentSentiment == "pos":
            dispatcher.utter_message(response="utter_feedback_good")  # Utter good feedback response, only if feedback
            # is good
        elif recentSentiment is None:
            dispatcher.utter_message(response="utter_default")  # Handle case where there is no intent/sentiment
            # extracted
        else:
            dispatcher.utter_message(response="utter_feedback_bad")  # If feedback is neutral or negative utter bad
            # feedback

        return []
#wikipedia api implemmentation
class ActionWikipedia(Action): 
    def name(self) -> Text:
        return "action_wiki_subject"
    
    def run(self, dispatcher : CollectingDispatcher, 
    tracker: Tracker, 
    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    recentSearch = 
    next(tracker.get_latest_entity_values("wikipediasubject"), None) 

    try:  #wikipedia.summary prints summary from page
        print(wikipedia.page(wikipedia.search(recentSearch))
        dispatcher.utter_message(text= "Here are the subjects results from wikipedia") + wikipedia.summary(wikipedia.search(recentSearch)

   
    except wikipedia.exceptions.WikipediaException as e:
        dispatcher.utter_message(text= "Could not find this subject on wikipedia! :(, try an new subject,or check for spelling errors!")    
print(e)


    return[]


