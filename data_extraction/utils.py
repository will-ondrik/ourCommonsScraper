chars_to_remove = [
    '$',
    ','
]
def format_dollar_values(value):
    for char in chars_to_remove:
        value = value.replace(char, '')
    
    return value


def format_single_quotes_for_sql(word):
    word = word.replace("'", "''")
    return word