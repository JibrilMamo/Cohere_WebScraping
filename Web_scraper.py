import cohere
import requests
from bs4 import BeautifulSoup

# Initialize the Cohere client
api_key = 'YOUR_API_KEY'
co = cohere.Client(api_key)


def summarize_text(text):
    response = co.summarize(
        text=text,
        length='short'  # Options: 'short', 'medium', 'long'
    )
    return response.summary


def fetch_webpage_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract all text from paragraph tags
    paragraphs = soup.find_all('p')
    text = ' '.join([para.get_text() for para in paragraphs])

    return text


# Example URL to scrape and summarize
url = 'https://en.wikipedia.org/wiki/Frog'
webpage_text = fetch_webpage_text(url)

summary = summarize_text(webpage_text)
print("Summary:", summary)
