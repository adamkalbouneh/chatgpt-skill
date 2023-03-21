from mycroft import MycroftSkill, intent_file_handler
import openai
import os

class Chatgpt(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        openai.api_key = os.environ[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]  # Set the API key

    @intent_file_handler('chatgpt.intent')
    def handle_chatgpt(self, message):
        prompt = "Hello, how are you?"  # Example prompt
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=60
        )
        text = response.choices[0].text.strip()  # Get the generated text
        self.speak(text)  # Speak the generated text

def create_skill():
    return Chatgpt()
