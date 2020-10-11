obj_licensed = {}
obj_fact = {}

obj_licensed =  ['5' + str(id) for id in range(50000, 50504) ]
obj_licensed += ['6' + str(id) for id in range(50000, 50100) ]
obj_licensed += ['8' + str(id) for id in range(50000, 51200) ]
obj_licensed += ['1' + str(id) for id in range(50000, 50680) ]
obj_licensed += ['3' + str(id) for id in range(50000, 50670) ]





with open('c:/temp/license_check.csv', 'w', encoding='cp866') as fo:
    with open('c:/Temp/ObjList50.csv', 'r', encoding='cp866') as fi:
        for line in fi:
            words = line.strip().split(';')

            if f'{words[0]}{words[1]}' in obj_licensed:
                csv_line = f'{words[0]};{words[1]};{words[2]};1' 
            else:
                csv_line = f'{words[0]};{words[1]};{words[2]};0'
            fo.write(f'{csv_line}\n')





