import re

dd = ['50000', '51000', '94014']
s = 'lksdlkjfs 500mslfj kds;f(50000)kksds ; s s51000'
s = 'NoSeriesMgt@1101495014 : Codeunit 396;'
if result := re.findall(r'\b\d{5}', s):
    for res in result:
        if res in dd:
            print(res)