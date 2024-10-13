# Summary
This Python script interacts with the Cambridge Dictionary and Notion to fetch word definitions and examples, and then stores this information in a Notion database.

## Key Components:
1. Libraries Used:
    - **requests** : For making HTTP requests to fetch word data.
    - **BeautifulSoup** (from bs4): For parsing HTML and extracting definitions and examples.
    - **notion_client** : For interacting with the Notion API to add data.
2. Initialization:
    - A Notion client is initialized with an authentication token.
3. Functionality:
    - **fetch_definition_and_example(word):**
      - Takes a word as input, fetches its definition and example from the Cambridge Dictionary, and returns them.
      - Handles potential request errors gracefully.
    - **add_to_notion(word, definition, example, tag):**
      - Adds the fetched word, its definition, example, and a user-defined tag to a specified Notion database.
      - Catches exceptions during the database operation and reports any failures.
4. Main Loop:
    - Prompts the user to enter a word.
    - Calls the fetching function and, if successful, asks for a tag to categorize the word.
    - Continues until the user types 'exit'.
### Usage:
Run the script, input a word to retrieve its definition and example, and store it in Notion with a tag for easy reference.
