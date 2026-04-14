# Task 1: this program collects trending stories/news/tech/sports/sci/ent and categorizes them

import time
top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"   # API URLs
headers = {"User-Agent": "TrendPulse/1.0"}  # Header (IMPORTANT)

categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "show", "award", "streaming"]
}                                                                                                           # Categories with keywords


def detect_category(title):                                                                         # Function to detect category
    title = title.lower()
    for category, words in categories.items():
        for word in words:
            if word in title:
                return category
    return "others"


try:
    
    response = requests.get(top_stories_url, headers=headers)  # Fetch top story IDs

    if response.status_code != 200:
        print("Failed to fetch story IDs")
    else:
        story_ids = response.json()

        print("Fetching stories.........\n")
      
        for story_id in story_ids[:50]:    # Fetch first 50

            story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"

            try:
                story_res = requests.get(story_url, headers=headers)

                if story_res.status_code != 200:
                    print(f"Skipping story {story_id} (failed request)")
                    continue

                story = story_res.json()

                if story and "title" in story:
                    title = story["title"]
                    category = detect_category(title)

                    print("Title:", title)
                    print("Category:", category)
                    print("-" * 50)

            except Exception as e:
                print(f"Error fetching story {story_id}:", e)

        time.sleep(2)

except Exception as e:
    print("Error occurred:", e)
