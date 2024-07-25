from constants.constants import REPORTING_TIME_PERIOD, YEAR, FISCAL_QUARTER
def write_to_file(sql_script):
    f = open(f'{REPORTING_TIME_PERIOD[0]}-to-{REPORTING_TIME_PERIOD[1]}-Year:{YEAR}-Quarter:{FISCAL_QUARTER}.sql', 'a')
    f.write('\n')
    
    if sql_script[0][0] is not None:
        for line in sql_script[0][0]:
            if "'NULL'" in line:
                line = line.replace("'NULL'", "NULL")                
            f.write(line + '\n')
        
        f.write('\n')
    
    if sql_script[0][1] is not None:
        for line in sql_script[0][1]:
            if "'NULL'" in line:
                line = line.replace("'NULL'", "NULL")     
            f.write(line + '\n')
        
        f.write('\n')

    if sql_script[0][2] is not None:
        for line in sql_script[0][2]:
            if "'NULL'" in line:
                line = line.replace("'NULL'", "NULL")     
            f.write(line + '\n')
        
        f.write('\n')

    if sql_script[0][3] is not None:
        for line in sql_script[0][3]:
            if "'NULL'" in line:
                line = line.replace("'NULL'", "NULL")     
            f.write(line + '\n')
        
        f.write('\n')


    f.close()
