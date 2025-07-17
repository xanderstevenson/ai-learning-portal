import requests
from bs4 import BeautifulSoup

def fetch_cisco_learning_material(url):
    # Placeholder for scraping or API calls to get learning material
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example parsing logic - adjust based on actual page structure
    titles = soup.find_all('h2', class_='title')
    return [{'title': title.text.strip(), 'url': url} for title in titles]

