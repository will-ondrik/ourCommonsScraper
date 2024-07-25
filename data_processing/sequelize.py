from data_processing import process_contract_expenses
from data_processing import process_hospitality_expenses
from data_processing import process_travel_expenses
from data_processing import process_mp_data


def sequelize_data(extracted_mp_expense_data, startPeriod, endPeriod, year, quarter):
    
    sql_script = []
    sequelized_mp_data = process_mp_data.sequelize(extracted_mp_expense_data[0][0])
    sequelized_travel_data = process_travel_expenses.sequelize(extracted_mp_expense_data[0][1], startPeriod, endPeriod, year, quarter)
    sequelized_hospitality_data = process_hospitality_expenses.sequelize(extracted_mp_expense_data[0][2], startPeriod, endPeriod, year, quarter)
    sequelized_contract_data = process_contract_expenses.sequelize(extracted_mp_expense_data[0][3], startPeriod, endPeriod, year, quarter)

    sql_script.append({
        0: sequelized_mp_data,
        1: sequelized_travel_data,
        2: sequelized_hospitality_data,
        3: sequelized_contract_data
    })

    return sql_script