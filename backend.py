from openai import OpenAI
import os


class Chatbot:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("chatbox_api"))

    def get_response(self, user_input):
        response = self.client.chat.completions.create(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "user",
                 "content": [
                     {"type": "text",
                         "text": user_input},],}],
            temperature=0.5
        ).choices[0].message.content
        return response


if __name__ == "__main__":
    chatbot = Chatbox()
    response = chatbot.get_response("Write a Joke about birds.")
    print(response)


