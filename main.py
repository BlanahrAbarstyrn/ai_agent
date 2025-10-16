import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', action='store_true')
    #args = parser.parse_args()
    args, _ = parser.parse_known_args()

    if len(sys.argv) < 2:
        print("Usage: uv run main.py <ai prompt>")
        sys.exit(1)
    user_prompt = sys.argv[1]

    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
    )
    print(response.text)

    usage = response.usage_metadata

    prompt_tokens = usage.prompt_token_count
    response_tokens = usage.candidates_token_count

    if args.verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")





if __name__ == "__main__":
    main()
