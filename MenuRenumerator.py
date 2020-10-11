
objmap = {}

obj_type_map ={}


with open('c:/Temp/license_check.csv', 'r', encoding='cp866') as fi:
    for line in fi:
        words = line.strip().split(';')
        objmap[f'{words[0]}{words[1]}'] = words[2]


obj_type = ''
obj_id = ''
with open('c:/temp/mnu-renum.csv', 'w', encoding='cp866') as fo:
    with open('c:/Temp/mnu.txt', 'r', encoding='cp866') as fi:
        for i, line in enumerate(fi):
            sline = line.strip()
            if sline.startswith('RunObjectType='):
                words = sline.strip(';').split('=')
                obj_type = words[1]
            elif sline.startswith('RunObjectID='):
                if not obj_type:
                    raise(ValueError( f'parsing error!: {i}'))
                words = sline.strip(';').split('=')
                obj_id = words[1]

                obj_new_id = objmap.get(f'{obj_type}{obj_id}')
                if obj_new_id:
                    text = line.replace(obj_id, obj_new_id)
                else:
                    text = line
                obj_type = ''
                obj_id = ''
            else:
                if obj_type:
                    raise(ValueError(f'parsing error!: {i}'))
                text = line
            fo.write(text)
