import data_processing.utils as utils

def hospitality_claim_insert(date, location, attendance, purpose, total_cost):
    return f"INSERT INTO HospitalityClaim (expenseId, memberId, date, location, attendance, purpose, totalCost) VALUES (@expenseId, @mpId, '{date}', '{location}', {attendance}, '{purpose}', {total_cost});"

def event_insert(claim_number, event_type, supplier, cost):
    return f"INSERT INTO event (claimId, claimNumber, type, purpose, supplier, totalCost) VALUES (@claimId, '{claim_number}', '{event_type}', '{supplier}', {cost});"

def sequelize(hospitality_data, startPeriod, endPeriod, year, quarter):
    print('sqlized hospitality', hospitality_data)
    script = []
    if not hospitality_data:
        return
    else:
        for data in hospitality_data:
            script.append(utils.expense_insert('hospitality', data['total_cost'], startPeriod, endPeriod, year, quarter))
            script.append(hospitality_claim_insert(data['date'], data['location'], data['attendance'], data['purpose'], data['total_cost']))
            script.append(utils.set_var_claim_id())

            if not data['details']:
                continue
            else:
                for nested_data in data['details']:
                    print('nested data: ', nested_data)
                    script.append(event_insert(nested_data['claim_number'], data['event_type'], nested_data['supplier'], nested_data['cost']))

    return script