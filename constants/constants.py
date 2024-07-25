# Inserted into the MAIN_PAGE_URL in 'main.py' for specific data collection
YEAR = 2024
PREVIOUS_YEAR = 2023
Q1 = 1
Q2 = 2
Q3 = 3
Q4 = 4

# Reporting Period Dates
reporting_periods = {
    'Q1': [f'{PREVIOUS_YEAR}-04-01', f'{PREVIOUS_YEAR}-06-30'],
    'Q2': [f'{PREVIOUS_YEAR}-07-01', f'{PREVIOUS_YEAR}-09-30'],
    'Q3': [f'{PREVIOUS_YEAR}-10-01', f'{PREVIOUS_YEAR}-12-31'],
    'Q4': [f'{YEAR}-01-01', f'{YEAR}-03-31']
}

REPORTING_TIME_PERIOD = reporting_periods['Q3']
FISCAL_QUARTER = Q3



# URL Information
 # MP_EXPENSES_PAGE_URL needs to have /YEAR/QUARTER/ + unique href value appended to it
BASE_URL = 'https://www.ourcommons.ca'
MP_EXPENSES_PAGE_URL = f"{BASE_URL}/proactivedisclosure/en/members/{YEAR}/{Q3}/"


# Firefox/Selenium Constants
FIREFOX_BINARY = '/opt/firefox/firefox'
GECKO_DRIVER_EXECUTABLE = '/usr/local/bin/geckodriver'



# Error Messages
NO_TBODY_FOUND = 'No <tbody> element found in the HTML'


# Tbody classes
EXPENSES_MAIN_INFO = 'expenses-main-info'


# General Strings
EMPTY_STRING = ''
NOT_LISTED = 'Not Listed'