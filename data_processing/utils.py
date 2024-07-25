def start_transaction():
    return "START TRANSACTION;"

def commit_transaction():
    return "COMMIT;"

def set_var_mp_id():
    return f"SET @mpId = LAST_INSERT_ID();"
    
def set_var_expense_id():
    return f"SET @expenseId = LAST_INSERT_ID();"

def set_var_claim_id():
    return f"SET @claimId = LAST_INSERT_ID();"

def set_var_traveller_id():
    return f"SET @travellerId = LAST_INSERT_ID();"


def expense_insert(claim_type, cost, reporting_start_period, reporting_end_period, year, fiscalQuarter):
    return f"INSERT INTO Expense (memberId, claimType, cost, reportingPeriodStart, reportingPeriodEnd, year, fiscalQuarter) VALUES (@mpId, '{claim_type}', {cost}, '{reporting_start_period}', '{reporting_end_period}', {year}, {fiscalQuarter});"
