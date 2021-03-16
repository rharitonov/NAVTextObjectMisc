# Copyright by HR:)
#
# split one big file of objects to separate files, one object per file
#

counter = 0
object_text = []
files = []
output_path = 'c:/temp/bonava/'
with open('c:/temp/BONAVA-DEV-2021-03-16.txt', 'r', encoding='cp866') as fi:
    for line in fi:
        if line.startswith('OBJECT '):
            if object_text:
                with open(f'{output_path}{object_filename}', 'w', encoding='cp866') as fo:
                    fo.write(''.join(object_text))
                object_text = []
                counter += 1
            words = line.split(' ', 3)
            object_filename = f'{(words[1].lower()[0])}{words[2]}.txt'
            files.append(object_filename)    
        object_text.append(line)

with open(f'{output_path}_list.csv', 'w') as fo:
    fo.write('filename')
    fo.write('\n'.join(files))

print(f'{counter} objects was splitted into separate file')
