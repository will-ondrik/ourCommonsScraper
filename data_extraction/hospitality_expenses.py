from bs4 import BeautifulSoup
from constants.constants import BASE_URL, NO_TBODY_FOUND, EXPENSES_MAIN_INFO
from data_extraction.utils import format_dollar_values, format_single_quotes_for_sql
import time

def extract_event_type(event_row):
    event_data = event_row.text.strip()
    return event_data.replace('Type of Event', '').strip()

def extract_hospitality_expenses(driver, href_value):
    time.sleep(1)
    hospitality_data = []
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
            date = row_data[0].text.strip()
            location = format_single_quotes_for_sql(row_data[1].text.strip())
            attendance = row_data[2].text.strip()
            purpose = format_single_quotes_for_sql(row_data[3].text.strip())
            total = format_dollar_values(row_data[4].text.strip())

            nested_row_data = []
            nested_rows = rows[i + 1].find_all('tr')
            event_row = rows[i + 1].find(class_='col-md-4')
            event_type = extract_event_type(event_row)

            for row in nested_rows[1:len(nested_rows)-1]:
                row_data = row.find_all('td')
                claim_number = row_data[0].text.strip()
                supplier = format_single_quotes_for_sql(row_data[1].text.strip())
                cost = format_dollar_values(row_data[2].text.strip())

                nested_row_data.append({
                    'claim_number': claim_number,
                    'supplier': supplier,
                    'cost': cost
                })

            hospitality_data.append({
                'event_type': event_type,
                'date': date,
                'location': location,
                'attendance': attendance,
                'purpose': purpose,
                'total_cost': total,
                'details': nested_row_data
            })

            i += 2
        else:
            i += 1

    return hospitality_data