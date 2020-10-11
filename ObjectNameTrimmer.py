with open('c:/temp/orig_tables51_renamed.txt', 'w', encoding='cp866') as fo:
    with open('c:/temp/orig_tables51.txt', 'r', encoding='cp866') as fi:
        for line in fi:
            if not line.startswith('OBJECT '):
                out_line = line
            else:
                words = line.split(' ', 3)
                words[3] = '_' + words[3][:29]
                out_line = f'{words[0]} {words[1]} {words[2]} {words[3]}'
            fo.write(out_line)