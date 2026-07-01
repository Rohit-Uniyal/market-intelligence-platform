from src.scraper.browser import get_browser
from src.scraper.twitter_scraper import build_search_url


driver = get_browser()

url = build_search_url("#nifty50")

print(f"Generated URL: {url}")

driver.get(url)

input("Press Enter to close the browser...")

driver.quit()