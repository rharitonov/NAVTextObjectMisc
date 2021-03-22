with open('c:/temp/renum_codeunits3.txt', 'w', encoding='cp866') as fo:

source_dir = '' 
output_filename = ''    
object_source_code = []
with open(source_dir + 'obj.txt', 'r', encoding='cp866') as fi:
    for ln in fi:
        if ln.startswith('OBJECT '):
            with open(source_dir + output_filename, 'w', encoding='cp866') as fo:            
                fo.write(''.join(object_source_code))        

            words = ln.split(' ', 3)
            obj_type = words[1].lower()[1]
            obj_id = words[2]
            output_filename = f'{obj_type}{obj_id}.txt'
        object_source_code.append(ln)
    with open(source_dir + output_filename, 'w', encoding='cp866') as fo:            
        fo.write(''.join(object_source_code))        
