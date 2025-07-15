import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# Compose prompt to generate persona
def build_prompt(posts, comments):
    examples = ""
    for post in posts:
        examples += f"\n[POST]\nTitle: {post['title']}\nText: {post['selftext']}\nURL: {post['url']}\n"
    for comment in comments:
        examples += f"\n[COMMENT]\nText: {comment['body']}\nURL: {comment['url']}\n"

    return f"""
You are an AI persona builder. Based on the Reddit posts and comments below, generate a detailed user persona.
For each characteristic (e.g. Interests, Personality Traits, Profession, Writing Style), cite the specific post/comment URL used to infer that.

Reddit Activity:
{examples}

Output format:
Persona:
- Interests: ... (Cited from: ...)
- Personality: ... (Cited from: ...)
- Profession: ... (Cited from: ...)
- Writing Style: ... (Cited from: ...)
- Values or Beliefs: ... (Cited from: ...)
"""

def generate_persona(posts, comments):
    prompt = build_prompt(posts, comments)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000
    )

    return response.choices[0].message['content']
