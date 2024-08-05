from constants.constants import BASE_URL, NO_TBODY_FOUND, EXPENSES_MAIN_INFO, EMPTY_STRING, NOT_LISTED
from data_extraction.utils import format_dollar_values, format_single_quotes_for_sql
from bs4 import BeautifulSoup
import time

def split_date_range(date_range):
    date_range = date_range.replace('From ', '')
    date_range = date_range.replace(' to ', ',')
    return date_range.split(',')

def extract_travel_expenses(driver, href_value):
    time.sleep(1)
    travel_data = []
    PAGE_URL = BASE_URL + href_value
        
    # Navigate to Page
    driver.get(PAGE_URL)
    time.sleep(1)

    # Extract HTML Content and Parse with BS4
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Find the TBody element that contains desired data
    tbody = soup.find('tbody')
    if not tbody:
        print(NO_TBODY_FOUND)
        return travel_data
        
    # Find and iterate through all table rows
    rows = tbody.find_all('tr')
    i = 0
    while i < len(rows):
        row = rows[i]
        if 'expenses-main-info' in row.get('class', []):
            claimId = row.find('td', class_='text-nowrap').text.strip()
            date_text = row.find_all('td', class_='text-nowrap')[1].text.strip()
            dateRange = split_date_range(date_text) if date_text else ['NULL', 'NULL']
            transportation_cost = format_dollar_values(row.find_all('td', class_='text-nowrap text-right')[0].text.strip())
            accommodation_cost = format_dollar_values(row.find_all('td', class_='text-nowrap text-right')[1].text.strip())
            meals_and_incidentals_cost = format_dollar_values(row.find_all('td', class_='text-nowrap text-right')[2].text.strip())
            regular_points = row.find_all('td', class_='text-nowrap text-right')[3].text.strip()
            special_points = row.find_all('td', class_='text-nowrap text-right')[4].text.strip()
            USA_points = row.find_all('td', class_='text-nowrap text-right')[5].text.strip()
            total_cost = format_dollar_values(row.find_all('td', class_='text-nowrap text-right')[6].text.strip())

            

            nested_row = rows[i + 1].find_all('tr')
            nested_data = []
            for row in nested_row[1:]:
                row_data = row.find_all('td')
                if len(row_data) == 6:
                    traveller = row_data[0].text.strip().replace('Hon. ', '')
                    traveller_name = None

                    if 'brandon aboultaif'.lower() == traveller.lower():
                        traveller_name = ['Aboultaif', 'Brandon']
                    elif 'test'.lower() == traveller.lower():
                        continue
                    elif not traveller:
                        traveller_name = ['Not listed', 'Not listed']
                    else:
                        traveller_name = traveller.split(',')
                        traveller_name[0] = format_single_quotes_for_sql(traveller_name[0])
                        
                    traveller_type = row_data[1].text.strip()
                    purpose_of_travel = format_single_quotes_for_sql(row_data[2].text.strip())
                    travel_date = row_data[3].text.strip()
                    departure = format_single_quotes_for_sql(row_data[4].text.strip())
                    destination = format_single_quotes_for_sql(row_data[5].text.strip())
                    nested_data.append({
                        'traveller_name': traveller_name,
                        'traveller_type': traveller_type,
                        'purpose_of_travel': purpose_of_travel,
                        'travel_date': travel_date,
                        'departure': departure,
                        'destination': destination,
                    })

                elif len(row_data) == 4:
                    traveller = row_data[0].text.strip().replace('Hon. ', '')
                    if not traveller:
                        traveller_name = ['Not Listed', 'Not Listed']
                    else:
                        traveller_name = traveller.split(',')
                        traveller_name[0] = format_single_quotes_for_sql(traveller_name[0])
                        traveller_name[1] = format_single_quotes_for_sql(traveller_name[1])

                    traveller_type = row_data[1].text.strip()
                    purpose_of_travel = format_single_quotes_for_sql(row_data[2].text.strip())
                    city = format_single_quotes_for_sql(row_data[3].text.strip())
                    nested_data.append({
                        'traveller_name': traveller_name,
                        'traveller_type': traveller_type,
                        'purpose_of_travel': purpose_of_travel,
                        'travel_date': 'NULL',
                        'departure': 'NULL',
                        'destination': city
                    })

            travel_data.append({
                'claim_id': claimId,
                'start_date': dateRange[0],
                'end_date': dateRange[1],
                'transportation_cost': transportation_cost,
                'accommodation_cost': accommodation_cost,
                'meals_and_incidentals_cost': meals_and_incidentals_cost,
                'regular_points_used': regular_points,
                'special_points_used': special_points,
                'USA_points_used': USA_points,
                'total_cost': total_cost,
                'details': nested_data
            })
            i += 2
        else:
            i += 1
    print('travel data', travel_data)
    return travel_data