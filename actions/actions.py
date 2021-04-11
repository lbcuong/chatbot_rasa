import json
from typing import Any, Text, Dict, List


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase


class ActionCheckExistence(Action):
    with open("data/knowledge_base.json") as f:
        knowledge_base = json.load(f)

    def name(self) -> Text:
        return "action_check_existence"

    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for objs in tracker.latest_message['entities']:
            if objs['entity'] == 'name':
                obj = objs['value']
                for each in self.knowledge_base['restaurant']:
                    if each['name'] == obj:
                        dispatcher.utter_message(text=f"{each['name']} have cuisine of {each['cuisine']}")
                break
        else:
            dispatcher.utter_message(text=f"What information do you need?")
        return []
        
"""class ActionShowList(ActionQueryKnowledgeBase):
    def __init__(self):
        # load knowledge base with data from the given file
        knowledge_base = InMemoryKnowledgeBase("data/knowledge_base.json")

        # overwrite the representation function of the restaurant object
        # by default the representation function is just the name of the object
        knowledge_base.set_representation_function_of_object(
            "restaurant", lambda obj: obj["name"] + " (" + obj["cuisine"] + ")" + " (" + obj["price-range"] + ")."
        )

        super().__init__(knowledge_base)"""