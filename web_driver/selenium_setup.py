from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.service import Options
from selenium.webdriver.common.by import By
from ourCommonsScraper.constants.constants import FIREFOX_BINARY, GECKO_DRIVER_EXECUTABLE 

def get_driver():
    # Configure Selenium WebDriver Options
    # Specify the path to the Firefox binary
    # Enable headless mode for background execution
    options = Options()
    options.binary_location = FIREFOX_BINARY 
    options.headless = True 

    # Initialize the Firefox WebDriver
    # Specify the path to the geckodriver executable
    # Create a Firefox WebDriver instance with the specified options
    service = Service(GECKO_DRIVER_EXECUTABLE)
    driver = webdriver.Firefox(service=service, options=options) 

    return driver
