
import re

obj_def_written = False

go = False

old_id_list = []
#with open('c:/Temp/rn/1/all_mapping_v2.csv', 'r', encoding='cp866') as fi:
with open('c:/Temp/all_mapping_v2.csv', 'r', encoding='cp866') as fi:
    for line in fi:
        words = line.strip().split(';')
        old_id_list.append(words[1])



#with open('c:/temp/rn/1/Obj_under50_result.txt', 'w', encoding='cp866') as fo:
with open('c:/temp/obj-result.txt', 'w', encoding='cp866') as fo:    
#    with open('c:/Temp/rn/1/Obj_under50.txt', 'r', encoding='cp866') as fi:
    with open('c:/Temp/obj.txt', 'r', encoding='cp866') as fi:
        for line in fi:
            if line.startswith('OBJECT '):
                obj_def = line
                obj_def_written = False
            else:
                if result := re.findall(r'\b\d{5}', line):
                    for res in result:
                        if res in old_id_list:
                            if not obj_def_written:
                                fo.write(obj_def)
                                obj_def_written = True
                            fo.write(f'>>{line}')



