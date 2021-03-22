
import os 




def split_object(base_dir: str, input_filename: str):
    object_source_code = []
    output_filename = ''
    with open(os.path.join(base_dir, input_filename), 'r', encoding='cp866') as fi:
        for ln in fi:
            if ln.startswith('OBJECT '):
                if output_filename:
                    with open(os.path.join(base_dir, output_filename), 'w', encoding='cp866') as fo:            
                        fo.write(''.join(object_source_code))        

                words = ln.split(' ', 3)
                obj_type = words[1].lower()[0]
                obj_id = words[2]
                output_filename = f'{obj_type}{obj_id}.txt'
            object_source_code.append(ln)
    with open(os.path.join(base_dir, output_filename), 'w', encoding='cp866') as fo:            
        fo.write(''.join(object_source_code))        



root_dir = 'c:/Users/roman/YandexDisk/Navicon/~Merlion/WRK/'
db_list = ['naCITILINK', 'SALES', 'STORE', 'SUPPLY']

for folder in db_list:
    base_dir = os.path.join(root_dir, folder)
    file_list = os.listdir(base_dir)
    for obj_file in file_list:
        if os.path.isfile(os.path.join(base_dir, obj_file)):
            split_object(base_dir, obj_file)
