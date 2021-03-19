import re

object_id_name_map = {}

def wrap_quotes_name(name: str, delete_quote = False, use_double_quotes = True) -> str:
    s_quote = "\'"
    d_quote = '\"'
    if use_double_quotes: 
        quote = d_quote 
    else:
        quote = s_quote
    if not name:
        return None
    if (name[0] == quote) and (name[-1] == quote):
        return name  
    if delete_quote:
        name = name.replace('"', '') 
    if not use_double_quotes: 
        if (name[0] == d_quote) and (name[-1] == d_quote):
            name = name.lstrip(d_quote) 
            name = name.rstrip(d_quote)
        return f'{quote}{name}{quote}'
    else:           
        name = name.lstrip("\'") 
        name = name.rstrip("\'")
        if re.search(r'\s|\\|\.|\-|\(|\)|=|\/', name):                
            return f'{quote}{name}{quote}'
        else:
            return name

with open('/home/roman/Yandex.Disk/text-db/BONAVA-DEV-2021-03-16.txt', 'r', encoding='cp866') as fi:
    for ln in fi:
        if ln.startswith('OBJECT '):
            
            pp = ln.strip()
            pp = pp.split(' ', 3)
            pp[1] = pp[1].lower()
            if pp[1] in ['table', 'form', 'codeunit', 'report']:
                key = f'{pp[1]}{pp[2]}'
                object_id_name_map[key] = wrap_quotes_name(pp[3])    

with open('/home/roman/src/object_id_name_map.txt', 'w') as fo:
    fo.write('object_id_name_map = {\n')
    coma = ''
    for k, v in object_id_name_map.items():
        fo.write(f"\t{coma} '{k}' : '{v}'\n")
        coma = ','
    fo.write('}\n')