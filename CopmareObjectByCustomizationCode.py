
import os 
import collections
import re


no_file: bool = False

ec = 0

root_dev = 'c:/Users/roman/YandexDisk/Navicon/~Merlion/DEV/'
root_wrk = 'c:/Users/roman/YandexDisk/Navicon/~Merlion/WRK/'
task_file= 'c:/Users/roman/YandexDisk/Navicon/~Merlion/task.csv'

# root_dev = 'c:/Users/hrs/YandexDisk/Navicon/~Merlion/DEV/'
# root_wrk = 'c:/Users/hrs/YandexDisk/Navicon/~Merlion/WRK/'
# task_file= 'c:/Users/hrs/YandexDisk/Navicon/~Merlion/task.csv'
log_file= 'c:/Users/roman/YandexDisk/Navicon/~Merlion/log.txt'


def get_filename(base_dir: str, csv_splitted_line: list) -> str:
    fn = f'{csv_splitted_line[1]}/{csv_splitted_line[2].lower()[0]}{csv_splitted_line[3]}.txt'
    return os.path.join(base_dir, fn)


def get_count_task_code_marks(filename: str, task_code: str) -> int:
    if not os.path.exists(filename):
        return 0
    
    file_body: str
    with open(filename, 'r', encoding='cp866') as fi:  
         file_body = fi.read()
    
    if not file_body:
        return 0
    
    found = re.findall(rf'{task_code}', file_body, re.IGNORECASE)
    return len(found)

diff_log = collections.defaultdict(list)

with open(task_file, 'r') as fi:
    for cc, ln in enumerate(fi):
        ln = ln.strip()
        part = ln.split(';')
        task_code = part[0]
        object_id = f'{part[2]} {part[3]}'
        database = part[1]


        obj_file_dev = get_filename(root_dev, part)
        obj_file_wrk = get_filename(root_wrk, part)

        no_file = False
        if not os.path.exists(obj_file_dev):
            diff_log[task_code].append(f'{object_id} is not exist in DEV {database}')
            no_file = True

        if not os.path.exists(obj_file_wrk):
            diff_log[task_code].append(f'{object_id} is not exist in WRK {database}')
            no_file = True

        
        if no_file:
            ec += 1
        else:
            if get_count_task_code_marks(obj_file_dev, task_code) != get_count_task_code_marks(obj_file_wrk, task_code):
                diff_log[task_code].append(f'{object_id} is not equal in WRK and DEV {database}')
                ec += 1



# print(f'Errors in {ec} line of {cc}')
# for task_code, messages in diff_log.items():
#     print(task_code, '\n')
#     for msg in messages:
#         print('\t', msg)
#     print('\n')


with open(log_file, 'w') as fo:
    fo.write(f'Errors in {ec} line of {cc}\n\n')
    for task_code, messages in diff_log.items():
        fo.write(f'{task_code}\n')
        for msg in messages:
            fo.write(f'x\t{msg}\n')
        fo.write('\n')

