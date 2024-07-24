from web_driver.selenium_setup import get_driver
from constants.constants import MP_EXPENSES_PAGE_URL, NO_TBODY_FOUND, EXPENSES_MAIN_INFO, EMPTY_STRING, NOT_LISTED
from bs4 import BeautifulSoup
import time

def split_date_range(date_range):
    date_range.replace('From ', '')
    return date_range.split(' to ')

def extract_travel_expenses(href_value):
    
    try:
        travel_data = []
        driver = get_driver()
        PAGE_URL = MP_EXPENSES_PAGE_URL + href_value
        
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
            if EXPENSES_MAIN_INFO in row.get('class', []):
                row_data = row.find_all('td')
                claim_id = row_data[0].text.strip()
                date_range = split_date_range(row_data[1].text.strip())
                transportation_cost = row_data[2].text.strip().replace('$', '')
                accomodation_cost = row_data[3].text.strip().replace('$', '')
                meals_and_incidentals_cost = row_data[4].text.strip().replace('$', '')
                regular_points = row_data[5].text.strip()
                special_points = row_data[6].text.strip()
                USA_points = row_data[7].text.strip()
                total_cost = row_data[8].text.strip()

                # Rows are grouped in 2's
                # Get the second row (contains nested table rows ('tr'))
                nested_rows = rows[i + 1].find_all('tr')
                nested_travel_data = []

                # Iterate through nested rows
                # Skip the table header row ([1:])
                for row in nested_rows[1:]:
                    nested_row_data = row.find_all('td')

                    if len(nested_row_data) == 6:
                        traveller_name = nested_row_data[0].text.strip().split(',')
                        traveller_type = nested_row_data[1].text.strip()
                        purpose_of_travel = nested_row_data[2].text.strip()
                        travel_date = nested_row_data[3].text.strip()
                        departure_city = nested_row_data[4].text.strip()
                        destination_city = nested_row_data[5].text.strip()

                        nested_travel_data.append({
                            'traveller_first_name': traveller_name[1],
                            'traveller_last_name': traveller_name[0],
                            'traveller_type': traveller_type,
                            'purpose_of_travel': purpose_of_travel,
                            'travel_date': travel_date,
                            'departure_city': departure_city,
                            'destination_city': destination_city
                        })

                    elif len(row_data) == 4:
                        traveller_type = nested_row_data[1].text.strip()
                        purpose_of_travel = nested_row_data[2].text.strip()
                        destination_city = nested_row_data[3].text.strip()


                        # Some of these names aren't given (empty strings)
                        # Check and insert 'not listed' if empty
                        traveller_name = nested_row_data[0].text.strip().split(',')
                        if traveller_name[0] == EMPTY_STRING:
                            traveller_name[0] = NOT_LISTED
                            traveller_name[1] = NOT_LISTED

                            nested_travel_data.append({
                                'traveller_first_name': traveller_name[1],
                                'traveller_last_name': traveller_name[0],
                                'purpose_of_travel': purpose_of_travel,
                                'destination_city': destination_city
                            })

                   
                        travel_data.append({
                            'claim_id': claim_id,
                            'start_date': date_range[0],
                            'end_date' : date_range[1],
                            'transportation_cost': transportation_cost,
                            'accommodation_cost': accomodation_cost,
                            'meals_and_incidentals_cost': meals_and_incidentals_cost,
                            'regular_points_used': regular_points,
                            'special_points_used': special_points,
                            'USA_points_used': USA_points,
                            'total_cost': total_cost,
                            'details': nested_travel_data
                        })            

                        # Move i to the next main row
                        i += 2
                    else:
                        # If no nested row, move to the next available row
                        i += 1

                return travel_data
    finally:
        driver.quit()