import os
import sys
import argparse
from dotenv import load_dotenv
from utils.prompts import system_prompt
from openai import OpenAI
from utils.call_function import available_functions, call_function


load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key == None:
    raise RuntimeError("api key is not setup")


parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)


messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]


def agent_logic(client, messages, args):

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
        temperature=0,
    )

    if not response.usage:
        raise RuntimeError("no prompts detected")


    if response.usage != None and args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    message = response.choices[0].message
    messages.append(message)

    if message.tool_calls:
        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, args.verbose)
            messages.append(result_message)

            if result_message["content"] == "":
                raise Exception("no content passed")

            if args.verbose == True:
                print(f"-> {result_message['content']}")

        return False
    else:
        print(message.content)
        return True

def main():
    for _ in range(20):
        done = agent_logic(client, messages, args)

        if done:
            break

    else:
        sys.exit("Couldn't produce a final result")


if __name__ == "__main__":
    main()
