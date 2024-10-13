import requests
from bs4 import BeautifulSoup
from notion_client import Client

# Initialize Notion client
notion = Client(auth='NOTION_INTEGRATION_KEY')

def fetch_definition_and_example(word):
    url = f"https://dictionary.cambridge.org/dictionary/english/{word}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract definition and example
        definition = soup.find('div', class_='def ddef_d db').get_text()[:-2].capitalize()
        example = soup.find('div', class_='examp dexamp').get_text().capitalize()
        return definition, example
        
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
        return None, None  # Return None if there’s an error

def add_to_notion(word, definition, example, tag):
    try:
        notion.pages.create(
            parent={"database_id": "NOTION_DATABASE_ID"},
            properties={
                "Word": {"title": [{"text": {"content": word}}]},
                "Definition": {"rich_text": [{"text": {"content": definition}}]},
                "Example Sentence": {"rich_text": [{"text": {"content": example}}]},
                "Tags": {
                    "multi_select": [{"name": tag}]
                }
            },
        )
        print(f"Added '{word}' to Notion.")
    except Exception as e:
        print(f"Failed to add to Notion: {e}")

def main():
    while True:
        word = input("Enter a word (or type 'exit' to quit): ")
        if word.lower() == 'exit':
            break
        
        definition, example = fetch_definition_and_example(word)

        # Check if fetch was successful
        if definition is None or example is None:
            print("Failed to retrieve data. Please check your connection or the word entered.")
            continue  # Continue to the next iteration of the loop

        tag = input("Enter 1 tag: ")
        add_to_notion(word, definition, example, tag)

if __name__ == "__main__":
    main()
