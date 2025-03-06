import requests
from bs4 import BeautifulSoup
from stem.control import Controller
from stem import Signal
import time

# TOR Proxy Configuration
PROXIES = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# Function to refresh Tor identity
def change_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password='your_tor_password')  # Set your Tor control password
            controller.signal(Signal.NEWNYM)
        time.sleep(5)  # Wait for IP change
    except Exception as e:
        print(f"Error changing IP: {e}")

# Function to scrape a dark web site
def scrape_dark_web(url):
    try:
        response = requests.get(url, proxies=PROXIES, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('h2')  # Modify based on the website structure
        for headline in headlines:
            print(headline.text.strip())
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    dark_web_urls = [
        "http://exampledarkwebsite.onion",  # Replace with actual .onion sites
        "http://anotherdarkweb.onion"
    ]
    
    for url in dark_web_urls:
        print(f"Scraping {url}...")
        scrape_dark_web(url)
        change_ip()  # Change IP after each request for anonymity
