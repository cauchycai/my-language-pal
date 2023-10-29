import os
import openai
from openai.api_resources.abstract.engine_api_resource import EngineAPIResource

def main():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response: EngineAPIResource = openai.ChatCompletion.create(
        # model="gpt-3.5-turbo",
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You will be provided with sentences, and your task is to help them sound natural in English."
            },
            {
                "role": "user",
                "content": "The system will fetch the tracking information of orders and return the trackings to the Amazon stores by Amazon API."
            }
        ],
        temperature=0,
        max_tokens=256
    )
    print(response)


if __name__ == '__main__':
    main()
