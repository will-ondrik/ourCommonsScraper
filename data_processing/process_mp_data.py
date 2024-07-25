import data_processing.utils as utils

def mp_insert(first_name, last_name, constituency, caucus, salary):
    return f"INSERT INTO MembersOfParliament (firstName, lastName, constituency, caucus, salary) VALUES ('{first_name}', '{last_name}', '{constituency}', '{caucus}', {salary});"

def sequelize(mp_data):
    script = []
    for row in mp_data:
        script.append(mp_insert(row['first_name'], row['last_name'], row['constituency'], row['caucus'], row['salary']))        
        script.append(utils.set_var_mp_id())
    return script