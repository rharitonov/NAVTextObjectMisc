common_tables = []
skip_line = False
obj_id = ''

with open('c:/temp/t51.txt', 'r', encoding='cp866') as fi:
    for line in fi:
        if line.startswith('OBJECT '):
            words = line.split(' ', 3)
            obj_id = words[2]
        elif line.startswith('    DataPerCompany=No;'):
            common_tables.append(obj_id)



with open('c:/temp/tables_mapping3.csv', 'w', encoding='cp866') as fo:
    with open('c:/Temp/tables_mapping2.csv', 'r', encoding='cp866') as fi:
        for line in fi:
            words = line.strip().split(';')
            if words[0] in common_tables:
                csv_line = f'{words[0]};{words[1]};0' 
            else:
                csv_line = f'{words[0]};{words[1]};1'
            fo.write(f'{csv_line}\n')
               