import data_processing.utils as utils
from constants.constants import MP_LOOKUP, PREVIOUS_YEAR

def mp_insert(first_name, last_name, constituency, caucus):
    return f"INSERT INTO MembersOfParliament (firstName, lastName, constituency, caucus) VALUES ('{first_name}', '{last_name}', '{constituency}', '{caucus}');"

def existing_mp_insert(mpId):
    return f"SET @mpId = {mpId};"

def salary_insert(full_name, year, salary, travelSpending, hospitalitySpending, contractSpending):
    return f"INSERT INTO SalaryAndSpending (memberId, memberName, year, salary, travelExpenses, hospitalityExpenses, contractExpenses) VALUES (@mpId, '{full_name}', {year}, {salary}, {travelSpending}, {hospitalitySpending}, {contractSpending});"

def sequelize(mp_data):
    script = []
    for row in mp_data:
        print('Mp Data:', mp_data)
        full_name = f"{row['first_name']} {row['last_name']}".replace('Hon. ', '')
        
        if full_name in MP_LOOKUP and full_name is not 'Vacant Vacant':
            mpId = MP_LOOKUP[full_name]
            script.append(existing_mp_insert(mpId))                

        else:
            MP_LOOKUP[full_name] = len(MP_LOOKUP) + 1
            
            script.append(mp_insert(row['first_name'], row['last_name'], row['constituency'], row['caucus']))        
            script.append(utils.set_var_mp_id())

        script.append(salary_insert(full_name, PREVIOUS_YEAR, row['salary'], row['travel_expenses'], row['hospitality_expenses'], row['contract_expenses']))
    return script