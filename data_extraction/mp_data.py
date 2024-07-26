from data_extraction.utils import format_dollar_values

def extract_mp_data(row_data):
    mp_data = []
    name = row_data[0].text.strip().split(', ')
    
    if name[0] == 'Vacant':
        first_name = name[0].strip()
        last_name = name[0]
    else:
        first_name = name[1].strip().replace('Hon. ', '')
        last_name = name[0]
    
    constituency = row_data[1].text.strip()
    caucus = row_data[2].text.strip()
    salary = format_dollar_values(row_data[3].text.strip())
    mp_data.append({
        'first_name': first_name,
        'last_name': last_name,
        'constituency': constituency,
        'caucus': caucus,
        'salary': salary
    })

    return mp_data
