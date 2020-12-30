import re

ruchars = "AАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
#enchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZzyxwvutsrqponmlkjihgfedcba"
enchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = list('0123456789/$&!_')

lexeme = {}
#with open('C:/Temp/Objects-60_NAV2009R2_RU.txt', 'r', encoding='cp866') as fi:
with open('C:/Temp/Objects-71_NAV2013R2_RU.txt', 'r', encoding='cp866') as fi:
    for line in fi:
        words = re.split(" |=|:=|\+|-|\\|, |\*|:|::|<>|<|>|'|{|}|\n|;|.\n|@|\(|\)|\.|\"|,|\[|\]", line)
        for w in words:
            lexeme[w] = lexeme.get(w, 0) + 1


#..или просто пишем в файл
#with open("C:/temp/Objects-60_NAV2009R2_RU-result.txt", "w", encoding='cp866') as fo:
with open("C:/temp/Objects-71_NAV2013R2_RU-result.txt", "w", encoding='cp866') as fo:
    for k, v in sorted(lexeme.items()):
        if len(k) > 2:
            if (k[0] in enchars) and not any(d in digits for d in k):
                #fo.write(f'{k} : {v}\n')
                fo.write(f'{k}\n')
        
                    
                
                    


