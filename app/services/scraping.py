import requests
from bs4 import BeautifulSoup

def scrape_competitor_price(url: str) -> float:
    """
    Scrapes the current selling price from a competitor's product page.
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # NOTE: You must update the selector (e.g., 'span.price') 
        # based on the specific website you are scraping.
        price_element = soup.select_one('.price-tag, #price, .a-price-whole')
        
        if price_element:
            price_str = price_element.get_text().replace('$', '').replace(',', '').strip()
            return float(price_str)
    except Exception as e:
        print(f"Scraping error: {e}")
    
    return 0.0
import requests
from bs4 import BeautifulSoup

def get_competitor_price(url: str) -> float:
    """
    Scrapes a product page to find the current selling price.
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Example selector: this needs to match the site's HTML
        price_text = soup.find("span", class_="price-tag").get_text()
        
        # Strip currency symbols and convert to float
        return float(price_text.replace("$", "").replace(",", "").strip())
    except Exception as e:
        print(f"Scraping failed: {e}")
        return 0.0