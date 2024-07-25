import data_processing.utils as utils
from constants.constants import EMPTY_STRING

def travel_claim_insert(start_date, end_date, transportation_cost, acccomodation_cost, meals_and_incidentals_cost, regular_points_used, special_points_used, usa_points_used, total_cost):
    return f"INSERT INTO TravelClaim (expenseId, memberId, startDate, endDate, totalCost) VALUES (@expenseId, @mpId, '{start_date}', '{end_date}', {transportation_cost}, {acccomodation_cost}, {meals_and_incidentals_cost}, {regular_points_used}, {special_points_used}, {usa_points_used}, {total_cost});"


def traveller_insert(first_name, last_name, traveller_type):
    return f"INSERT INTO Traveller (firstName, lastName, type) VALUES ('{first_name}', '{last_name}', '{traveller_type}');"

def travel_insert(purpose, city='NULL', departure='NULL', destination='NULL', date='NULL'):
    return f"INSERT INTO Travel (travellerId, claimId, date, departure, destination, purpose) VALUES (@travellerId, @claimId, '{date}', '{departure}', '{destination}', '{purpose}', '{city}');"

def sequelize(travel_data, startPeriod, endPeriod, year, quarter):
    script = []
    if not travel_data:
        return
    for data in travel_data:
        script.append(utils.expense_insert('travel', data['total_cost'], startPeriod, endPeriod, year, quarter))
        script.append(utils.set_var_expense_id())
        script.append(travel_claim_insert(data['start_date'], data['end_date'], data['transportation_cost'], data['accommodation_cost'], data['meals_and_incidentals_cost'], data['regular_points_used'], data['special_points_used'], data['USA_points_used'], data['total_cost']))
        script.append(utils.set_var_claim_id())

        if not data['details']:
            return
        else:
            for nested_data in data['details']:
                if nested_data.get('traveller_name')[0] == EMPTY_STRING:
                    script.append(traveller_insert(nested_data['traveller_name'][0].strip(), nested_data['traveller_name'][0], nested_data['traveller_type']))
                else:
                    script.append(traveller_insert(nested_data['traveller_name'][1].strip(), nested_data['traveller_name'][0], nested_data['traveller_type']))
                script.append(utils.set_var_traveller_id())
                if nested_data.get('travel_date') is None and nested_data.get('departure') is None:
                    script.append(travel_insert(nested_data['purpose_of_travel'], nested_data['destination'], departure='NULL', destination='NULL', date='NULL'))
                else:
                    script.append(travel_insert(nested_data['travel_date'], nested_data['departure'], nested_data['destination'], nested_data['purpose_of_travel']))

    return script     