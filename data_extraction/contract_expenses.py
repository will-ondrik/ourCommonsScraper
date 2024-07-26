from bs4 import BeautifulSoup
from constants.constants import BASE_URL, NO_TBODY_FOUND, EXPENSES_MAIN_INFO
from data_extraction.utils import format_dollar_values, format_single_quotes_for_sql
import time


def extract_contract_expenses(driver, href_value):
    time.sleep(1)
    contract_data = []
    PAGE_URL = BASE_URL + href_value
    driver.get(PAGE_URL)
    time.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    tbody = soup.find('tbody')
    if not tbody:
        print(NO_TBODY_FOUND)
        return
    

    rows = tbody.find_all('tr')
    i = 0
    while i < len(rows):
        row = rows[i]
        if EXPENSES_MAIN_INFO in row.get('class', []):
            row_data = row.find_all('td')
            supplier = format_single_quotes_for_sql(row_data[0].text.strip())
            description = format_single_quotes_for_sql(row_data[1].text.strip())
            date = row_data[2].text.strip()
            total_cost = format_dollar_values(row_data[3].text.strip())

            contract_data.append({
                'supplier': supplier,
                'description': description,
                'date': date,
                'total_cost': total_cost
            })
        i += 1

    return contract_data
        
    