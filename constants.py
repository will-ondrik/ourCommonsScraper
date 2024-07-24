# Inserted into the MAIN_PAGE_URL in 'main.py' for specific data collection
YEAR = 2024
Q1 = 1
Q2 = 2
Q3 = 3
Q4 = 4

# Reporting Period Dates
reporting_periods = {
    'Q1': ['04-01', '06-30'],
    'Q2': ['07-01', '09-30'],
    'Q3': ['10-01', '12-31'],
    'Q4': ['01-01', '03-31']
}


# URL Information
 # MP_EXPENSES_PAGE_URL needs to have /YEAR/QUARTER appended to it
BASE_URL = 'https://www.ourcommons.ca'
MP_EXPENSES_PAGE_URL = f"{BASE_URL}/proactivedisclosure/en/members"


# Firefox/Selenium Constants
FIREFOX_BINARY = '/opt/firefox/firefox'
GECKO_DRIVER_EXECUTABLE = '/usr/local/bin/geckodriver'
