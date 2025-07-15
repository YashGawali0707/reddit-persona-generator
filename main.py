import os
import requests
from dotenv import load_dotenv
import praw

# ✅ Load credentials from .env
load_dotenv(dotenv_path="user.env")

# 🔐 Reddit API credentials
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
USER_AGENT = os.getenv("USER_AGENT")

# 🔧 Initialize Reddit API
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)

# 🔍 Extract Reddit username from URL
def extract_username(url):
    return url.strip("/").split("/")[-1]

# 🧹 Scrape posts and comments
def scrape_reddit_user(username):
    user = reddit.redditor(username)
    posts = []
    comments = []

    try:
        for submission in user.submissions.new(limit=20):
            post_text = f"[POST] Title: {submission.title}\n{submission.selftext}"
            posts.append(post_text)

        for comment in user.comments.new(limit=30):
            comment_text = f"[COMMENT] {comment.body}"
            comments.append(comment_text)

    except Exception as e:
        print(f"❌ Error scraping Reddit user: {e}")

    return posts, comments

# 🤖 Generate persona using Ollama local LLM
def generate_persona(posts, comments, model="llama2"):
    content = "\n\n".join(posts + comments)

    if not content.strip():
        print("⚠️ No content found to generate persona.")
        return "No content available."

    prompt = f"""
    Based on the following Reddit content, generate a detailed user persona including:

    - Interests
    - Personality traits
    - Tone of writing
    - Values or beliefs

    For each trait, cite 2-3 short post or comment excerpts that support it.

    Reddit content:
    {content}
    """

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json().get("response", "")
        print("\n🧠 Ollama Output (First 500 characters):\n", result[:500])
        return result

    except Exception as e:
        print(f"❌ Error generating persona with Ollama: {e}")
        return ""

# 💾 Save output to file
def save_to_file(username, content):
    filename = f"persona_{username}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\n✅ Persona saved to {filename}")

# ▶️ Main runner
if __name__ == "__main__":
    reddit_url = input("🔗 Enter Reddit profile URL: ")
    username = extract_username(reddit_url)

    print(f"\n🔍 Scraping Reddit user: {username}...")
    posts, comments = scrape_reddit_user(username)

    print(f"🤖 Generating persona using Ollama...")
    persona = generate_persona(posts, comments, model="llama2")  # You can change model to mistral, gemma etc.

    print(f"💾 Saving output to file...")
    save_to_file(username, persona)
