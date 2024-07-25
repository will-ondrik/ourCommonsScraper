import data_processing.utils as utils

def contract_claim_insert(supplier, date, purpose, total_cost):
    return f"INSERT INTO ContractClaim (expenseId, memberId, supplier, date, purpose, totalCost) VALUES (@expenseId, @mpId, '{supplier}', '{date}', '{purpose}', {total_cost});"

def sequelize(contracts_data, startPeriod, endPeriod, year, quarter):
    script = []

    if not contracts_data:
        return
    else:
        for data in contracts_data:
            script.append(utils.expense_insert('contract', data['total_cost'], startPeriod, endPeriod, year, quarter))
            script.append(utils.set_var_expense_id())
            script.append(contract_claim_insert(data['supplier'], data['date'], data['description'], data['total_cost']))

    return script
