# Reddit User Persona Generator

This tool generates a user persona from any public Reddit profile using scraped comments and posts. It uses OpenAI's GPT model to infer personality, interests, profession, writing style, and values — with citations.

---

## 🚀 Features
- Scrapes Reddit posts & comments using PRAW
- Uses GPT (via OpenAI API) to generate a user persona
- Cites posts/comments for each inferred trait
- Outputs persona to a text file

---

## 🛠 Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/reddit-user-persona.git
cd reddit-user-persona
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Add API Keys to `.env`
Create a `.env` file in the root directory:
```dotenv
REDDIT_CLIENT_ID=your_client_id
REDDIT_SECRET=your_secret
REDDIT_USER_AGENT=your_user_agent
OPENAI_API_KEY=your_openai_key
```
You can get Reddit credentials from https://www.reddit.com/prefs/apps

---

## ▶️ Usage
Run the script using:
```bash
python main.py --url https://www.reddit.com/user/kojied/
```

This will generate an output file like:
```
output/kojied_persona.txt
```

---

## 📁 File Structure
```
reddit-user-persona/
├── main.py
├── reddit_scraper.py
├── persona_generator.py
├── requirements.txt
├── .env
├── README.md
└── output/
    └── kojied_persona.txt
```

---

## 📌 Notes
- This script only works for **public** Reddit users.
- Make sure to respect Reddit's API rate limits.
- You can increase `post_limit` or `comment_limit` in `reddit_scraper.py` for more thorough analysis.

---

## ✅ Example Users
Tested on:
- https://www.reddit.com/user/kojied/
- https://www.reddit.com/user/Hungry-Move-6603/

---
