
# Dark Web Scraper with TOR Anonymity

## Description

This project is a Python-based web scraper designed to extract data from dark web (.onion) sites while maintaining anonymity through the TOR network. It leverages the requests library with TOR proxy configurations and rotates IP addresses using the stem library to enhance privacy.


## Features

* Scrapes .onion websites anonymously via TOR.

* Rotates IP addresses to maintain anonymity.

* Extracts headlines (<h2> elements) from target sites.

* Uses BeautifulSoup for HTML parsing.

* Handles request exceptions gracefully.



## Requirements

Make sure you have the following dependencies installed:

* Python 3.x
* TOR installed and running
* Required Python libraries: 


```bash
pip install requests beautifulsoup4 stem
```


## TOR Configuration

1. Ensure the TOR service is running.

2. Modify the TOR configuration file ```bash(torrc)``` to enable control port:

``` ControlPort 9051 HashedControlPassword your_hashed_password ```

3. Restart TOR service after changes: ```bash service tor restart```

4. Replace ```bash'your_tor_password'``` in ```bash change_ip() ``` function with your actual password.


## Usage 

1. Replace ``` .onion``` URLs in ```bash dark_web_urls ```list with actual target sites.

2. Run the script:``` python scraper.py```


## Important Notes

* Ensure TOR is running before executing the script.

* Accessing certain dark web sites may be illegal in some jurisdictions. Use responsibly.

* Modify the scrape_dark_web() function based on the structure of the target website.


## Disclaimer
This project is for educational purposes only. The author is not responsible for any misuse of this tool. Always comply with legal and ethical guidelines when accessing online content.

