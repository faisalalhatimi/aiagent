import os
from dotenv import load_dotenv
from openai import OpenAI, responses
import argparse

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key == None:
    raise RuntimeError("api key is not setup")


parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)


response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": f"{args.user_prompt}",
        }
    ],
)


def main():
    if response.usage != None:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    elif response.usage == None:
        raise RuntimeError("no prompts detected")

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
