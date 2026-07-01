from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from src.scraper.constants import CHROME_DRIVER_VERSION


def get_browser():

    options = Options()

    options.debugger_address = "127.0.0.1:9222"

    service = Service(
        ChromeDriverManager(
            driver_version=CHROME_DRIVER_VERSION
        ).install()
    )

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    return driver