
def write_to_file(sql_script):
    print('SQL SCRIPT: ', sql_script)
    f = open('expenses.sql', 'a')
    f.write('\n')
    
    if sql_script[0][0] is not None:
        for line in sql_script[0][0]:
            if "'NULL'" in line:
                line = line.replace("'NULL'", "NULL")                
            f.write(line + '\n')
        
        f.write('\n\n')
    
    if sql_script[0][1] is not None:
        for line in sql_script[0][1]:
            if "'NULL'" in line:
                line = line.replace("'NULL'", "NULL")     
            f.write(line + '\n')
        
        f.write('\n\n')

    if sql_script[0][2] is not None:
        for line in sql_script[0][2]:
            if "'NULL'" in line:
                line = line.replace("'NULL'", "NULL")     
            f.write(line + '\n')
        
        f.write('\n\n')

    if sql_script[0][3] is not None:
        for line in sql_script[0][3]:
            if "'NULL'" in line:
                line = line.replace("'NULL'", "NULL")     
            f.write(line + '\n')
        
        f.write('\n\n')

    f.write('-----------------------------------------------')

    f.close()
