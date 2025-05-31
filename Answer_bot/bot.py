import json
import requests
from bs4 import BeautifulSoup

# Load local JSON data
with open('knowledge_base.json') as f:
    knowledge = json.load(f)

def fetch_from_web(query):
    try:
        print("Fetching answer from the web...")
        # Modify query to target college
        search_query = f"{query} site:drait.edu.in"
        search_url = f"https://www.google.com/search?q={search_query}"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(search_url, headers=headers)

        if response.status_code != 200:
            return "Sorry, couldn't fetch from the web right now."

        soup = BeautifulSoup(response.text, "html.parser")
        snippets = soup.select('div.BNeawe.s3v9rd.AP7Wnd')

        for snippet in snippets:
            text = snippet.get_text().strip()
            if len(text) > 50:
                return text

        return "Couldn't find relevant information online."

    except Exception as e:
        return f"Error fetching from web: {str(e)}"

def chatbot():
    print("Welcome to DrAIT Chatbot! Ask about fees, courses, fests, or any other info.")
    while True:
        user_input = input("You: ").strip().lower()

        if "fee" in user_input:
            print("Bot:", knowledge.get("fees", "Information not available."))
        elif "course" in user_input or "program" in user_input:
            print("Bot:", knowledge.get("courses", "Information not available."))
        elif "fest" in user_input or "event" in user_input:
            print("Bot:", knowledge.get("fests", "Information not available."))
        elif user_input in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot:", fetch_from_web(user_input))

if __name__ == "__main__":
    chatbot()
