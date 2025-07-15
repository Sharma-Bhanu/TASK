import argparse
import os
from reddit_scraper import get_reddit_instance, extract_username_from_url, get_user_data
from persona_generator import generate_persona

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_persona_to_file(username, persona_text):
    file_path = os.path.join(OUTPUT_DIR, f"{username}_persona.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(persona_text)
    print(f"✅ Persona saved to {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Reddit User Persona Generator")
    parser.add_argument("--url", type=str, required=True, help="Reddit profile URL")
    args = parser.parse_args()

    reddit = get_reddit_instance()
    try:
        username = extract_username_from_url(args.url)
        print(f"🔍 Fetching data for: {username}")
        posts, comments = get_user_data(reddit, username)

        print("🤖 Generating persona using LLM...")
        persona_text = generate_persona(posts, comments)

        save_persona_to_file(username, persona_text)

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
