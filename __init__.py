from mycroft import MycroftSkill, intent_file_handler


class Chatgpt(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('chatgpt.intent')
    def handle_chatgpt(self, message):
        self.speak_dialog('chatgpt')


def create_skill():
    return Chatgpt()

