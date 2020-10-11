

obj_type = '5'
obj_range = [*range(50000, 50504)]
obj_idlist =[]
free_ids = []


with open('c:/temp/ObjList50.csv', 'r', encoding='cp866') as fi:
    for l, line in enumerate(fi):
        if l == 0:
            continue
        words = line.split(';')
        if words[0] == obj_type:
            obj_id = int(words[1])
            if obj_id in obj_range:
                obj_idlist.append(obj_id)



with open(f'c:/temp/free_id_of_{obj_type}.csv', 'w', encoding='cp866') as fo:
    for uid in obj_range:
        if uid not in obj_idlist:
            fo.write(f'{uid}\n')
