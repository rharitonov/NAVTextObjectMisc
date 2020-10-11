found = []
skip_line = False
obj_id = ''

with open('c:/temp/t50.txt', 'r', encoding='cp866') as fi:
    for line in fi:
        if line.startswith('OBJECT '):
            words = line.split(' ', 3)
            obj_id = words[2]
            found.append(obj_id)


#print(', '.join(found))


with open('c:/temp/sql-2.csv', 'w', encoding='cp866') as fo:
    with open('c:/Temp/sql.csv', 'r', encoding='cp866') as fi:
        for line in fi:
            words = line.strip().split(';')
            if words[1] in found:
                csv_line = f'{words[0]};{words[1]};{words[2]};1' 
            else:
                csv_line = f'{words[0]};{words[1]};{words[2]};0'
            fo.write(f'{csv_line}\n')
               