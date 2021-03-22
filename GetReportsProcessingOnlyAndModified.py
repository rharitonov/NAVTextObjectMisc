found = {}
with open('c:/temp/naCLDev_20200924.txt', 'r', encoding='cp866') as fi:
    for line in fi:
        if line.startswith('OBJECT '):
            obj_id = None
            words = line.split(' ', 3)
            if words[1] == 'Report':
                obj_id = words[2]
        elif obj_id is not None:
            if any(line.startswith(prop) for prop in ['    ProcessingOnly=Yes', '    Modified=Yes']):
	            found[obj_id] = found.get(obj_id, 0) + 1
# или пишем в стдаут
#print ('\n'.join([key for key, val in found.items() if val == 2]))

#..или просто  пишем в файл
with open("C:/temp/result.txt", "w") as fo:
    fo.write('\n'.join([key for key, val in found.items() if val == 2]))

