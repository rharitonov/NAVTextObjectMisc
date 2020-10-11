found = []
skip_line = False
obj_id = ''

with open('c:/temp/t50.txt', 'r', encoding='cp866') as fi:
    for line in fi:
        if line.startswith('OBJECT '):
            words = line.split(' ', 3)
            obj_id = words[2]
        elif line.startswith('    TableType='):
            found.append(obj_id)


#print(', '.join(found))


with open('c:/temp/tables_mapping4-1.csv', 'w', encoding='cp866') as fo:
    with open('c:/Temp/tables_mapping4.csv', 'r', encoding='cp866') as fi:
        for line in fi:
            words = line.strip().split(';')
            if words[0] in found:
                csv_line = f'{words[0]};{words[1]};{words[2]};1' 
            else:
                csv_line = f'{words[0]};{words[1]};{words[2]};0'
            fo.write(f'{csv_line}\n')
               