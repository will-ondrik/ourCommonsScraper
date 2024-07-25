from web_driver.selenium_setup import get_driver
from constants.constants import MP_EXPENSES_PAGE_URL, REPORTING_TIME_PERIOD, YEAR, FISCAL_QUARTER
from bs4 import BeautifulSoup
from data_extraction.mp_data import extract_mp_data
from data_extraction.travel_expenses import extract_travel_expenses
from data_extraction.hospitality_expenses import extract_hospitality_expenses
from data_extraction.contract_expenses import extract_contract_expenses
from data_processing.sequelize import sequelize_data
from fileIO.sql_script import write_to_file
import time

def main():
    driver = get_driver()
    extract_data(driver, MP_EXPENSES_PAGE_URL)


def extract_data(driver, url):
    start_time = time.time()
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')


    rows = soup.find_all('tr', class_='expenses-main-info')
    for row in rows:
        # Variables to hold lists
        extracted_mp_data = []
        mp_data = None
        travel_expense_data = None
        hospitality_expense_data = None
        contract_expense_data = None

        # Extract row data
        row_data = row.find_all('td')

        # access columns to find elements with page hrefs
        travel_col = row_data[4]
        hospitality_col = row_data[5]
        contract_col = row_data[6]

        # Find the anchor elements in each column (if exists)
        travel_col_anchor = travel_col.find('a')
        hospitality_col_anchor = hospitality_col.find('a')
        contract_col_anchor = contract_col.find('a')

        # pass row data to mp_data func
        mp_data = extract_mp_data(row_data)
        print('MP: ', mp_data)

        if travel_col_anchor:
            print('extracting travel expenses...')
            travel_expense_data = extract_travel_expenses(driver, travel_col_anchor['href'])
            print('extraction complete.')
        else:
            print('No href found: Member has no travel expenses for this quarter.')


        if hospitality_col_anchor:
            print('extracting hospitality expenses...')
            hospitality_expense_data = extract_hospitality_expenses(driver, hospitality_col_anchor['href'])
            print('extraction complete.')
        else:
            print('No href found - Member has no hospitality expenses for this quarter')

        if contract_col_anchor:
            print('extracting contract expenses...')
            contract_expense_data = extract_contract_expenses(driver, contract_col_anchor['href'])
            print('extraction complete.')
        else:
            print('No href found - Member has no contract expenses for this quarter.')

        extracted_mp_data.append({
            0: mp_data,
            1: travel_expense_data,
            2: hospitality_expense_data,
            3: contract_expense_data
        })
        
        print('sequelizing...')
        sequelized_expense_data = sequelize_data(extracted_mp_data, REPORTING_TIME_PERIOD[0], REPORTING_TIME_PERIOD[1], YEAR, FISCAL_QUARTER)
        print('sequelizing complete.')
        print('writing to file...')
        write_to_file(sequelized_expense_data)
        print('sequelizing complete.')
    end_time = time.time()

    print('Program duration: ', end_time - start_time)



main()
