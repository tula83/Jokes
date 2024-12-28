import openai
import requests

def get_joke():
    # Using OpenAI's GPT-4 to generate a joke
    response = openai.Completion.create(
        model="gpt-4o-mini",
        prompt="Tell me a funny joke.",


        response_format={
            "type": "text"
        },
        temperature=1,
        max_completion_tokens=10000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    joke = response.choices[0].text.strip()
    return joke


def get_joke_rapid():
    url = "https://humor-jokes-and-memes.p.rapidapi.com/jokes/search"

    querystring = {"exclude-tags": "nsfw", "keywords": "rocket", "min-rating": "7", "include-tags": "one_liner",
                   "number": "3", "max-length": "200"}

    headers = {
        "x-rapidapi-key": "Sign Up for Key",
        "x-rapidapi-host": "humor-jokes-and-memes.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())

    return response.json()

