import hashlib

obj_checksum = {}
obj_code = ''
obj_id = ''
obj_to_extract = []
def get_checksum(text: str) -> str:
    h = hashlib.sha1()
    h.update(text.encode())
    return h.hexdigest()

with open('c:/temp/objects_orig.txt', 'r', encoding='cp866') as fi:
    for line in fi:
        if not line.startswith('OBJECT '):
            obj_code += line
        else:
            obj_checksum[obj_id] = get_checksum(obj_code)
            words = line.split(' ', 3)
            obj_id = words[2]
            obj_code = line 
        obj_checksum[obj_id] = get_checksum(obj_code)   


with open('c:/temp/objects_renamed.txt', 'r', encoding='cp866') as fi:
    for line in fi:
        if not line.startswith('OBJECT '):
            obj_code += line
        else:
            if obj_checksum[obj_id] != get_checksum(obj_code):
                obj_to_extract.append(obj_id)
            words = line.split(' ', 3)
            obj_id = words[2]
            obj_code = line 
        if obj_checksum[obj_id] != get_checksum(obj_code):
            obj_to_extract.append(obj_id)

total = 0
exported = 0
with open('c:/temp/objects_out.txt', 'w', encoding='cp866') as fo:
    with open('c:/temp/objects_renamed.txt', 'r', encoding='cp866') as fi:
        for line in fi:
            if line.startswith('OBJECT '):
                total += 1
                words = line.split(' ', 3)
                if words[2] in obj_to_extract:
                    write_line = True
                    exported += 1
                else:
                    write_line = False
            if write_line:
                fo.write(line)

print(f'Exported {exported} of {total}')









