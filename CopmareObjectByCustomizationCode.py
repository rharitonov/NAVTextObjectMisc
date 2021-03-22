
import os 
import collections

obj_file_dev_body, obj_file_wrk_body: str

root_dev = 'c:/Users/roman/YandexDisk/Navicon/~Merlion/DEV/'
root_wrk = 'c:/Users/roman/YandexDisk/Navicon/~Merlion/WRK/'
task_file= 'c:/Users/roman/YandexDisk/Navicon/~Merlion/task.csv'

def get_filename(base_dir: str, csv_splitted_line: list) -> str:
    fn = f'{csv_splitted_line[1]}/{csv_splitted_line[2].lower()[0]}{csv_splitted_line[3]}.txt'
    return os.path.join(base_dir, fn)


def read_file(filename: str) -> list:
    with open(filename, 'r', encoding='cp866') as fi:  
        return fi.read()

diff_log = collections.defaultdict(list)

with open(task_file, 'r') as fi:
    for ln in fi:
        ln = ln.strip()
        part = ln.split(';')
        task_code = part[0]
        object_id = f'{part[2]} {part[3]}'
        database = part[1]


        obj_file_dev = get_filename(root_dev, part)
        obj_file_dev_body = read_file(obj_file_dev)

        obj_file_wrk = get_filename(root_wrk, part)
        obj_file_wrk_body = read_file(obj_file_wrk)

        # if not os.path.exists(obj_file_dev):
        #     diff_log[task_code].append(f'{object_id} is not exist in DEV {database}')
        # if not os.path.exists(obj_file_wrk):
        #     diff_log[task_code].append(f'{object_id} is not exist in WRK {database}')


        found_dev = obj_file_dev_body.find(task_code)
        found_wrk = obj_file_wrk_body.find(task_code)
        

        


        



for task_code, messages in diff_log.items():
    print(task_code, '\n')
    for msg in messages:
        print('\t', msg, '\n')
    print('\n')


