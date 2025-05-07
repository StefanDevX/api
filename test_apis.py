import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API keys
omdb_key = os.getenv("OMDB_API_KEY")
google_books_key = os.getenv("GOOGLE_BOOKS_API_KEY")

# Test OMDb API
def test_omdb():
    url = f"http://www.omdbapi.com/?apikey={omdb_key}&s=Sherlock+Holmes&type=movie"
    response = requests.get(url)
    data = response.json()
    print("OMDb API Test:")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {data.get('Response')}")
    if data.get('Search'):
        print(f"Found {len(data['Search'])} movies")
        print(f"First movie: {data['Search'][0]['Title']}")
    print("\n")

# Test Google Books API
def test_google_books():
    url = f"https://www.googleapis.com/books/v1/volumes?q=Sherlock+Holmes&key={google_books_key}"
    response = requests.get(url)
    data = response.json()
    print("Google Books API Test:")
    print(f"Status Code: {response.status_code}")
    if data.get('items'):
        print(f"Found {len(data['items'])} books")
        print(f"First book: {data['items'][0]['volumeInfo'].get('title')}")
    print("\n")

if __name__ == "__main__":
    test_omdb()
    test_google_books()
