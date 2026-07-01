from src.scraper.browser import get_browser

driver = get_browser()

driver.get("https://www.google.com")

input("Press Enter to close the browser...")

driver.quit()
