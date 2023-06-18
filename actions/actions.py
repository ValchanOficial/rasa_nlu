# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk.events import AllSlotsReset
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import aiohttp

class ActionGetGithubRepositoriesForm(Action):

    def name(self) -> Text:
        return "action_get_github_repositories"

    async def run(
        self, 
        dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: Dict[Text, Any]
        ) -> List[Dict[Text, Any]]:

        github_username = tracker.get_slot('github_username')
        
        if not github_username:
            dispatcher.utter_message(text="Invalid Github username, please try again.")
            return [AllSlotsReset()]
        else:
            github_repositories = await get_github_repositories(github_username)
            dispatcher.utter_message(response = 'utter_github_response', repositories = github_repositories)
            return [AllSlotsReset()]

async def get_github_repositories(github_username: Text) -> Text:
    async with aiohttp.ClientSession() as session:
        url = f"https://api.github.com/users/{github_username}/repos"
        async with session.get(url) as response:
            if response.status == 200:
                github_repositories = await response.json()
                github_repositories_names = [repository["name"] for repository in github_repositories]
                if len(github_repositories_names) == 0:
                    return f"Sorry, I couldn't find any repositories for {github_username} on GitHub."
                github_repositories_message = "\n".join(github_repositories_names)
                return github_repositories_message
            else:
                return f"Sorry, I couldn't find any repositories for {github_username} on GitHub."
