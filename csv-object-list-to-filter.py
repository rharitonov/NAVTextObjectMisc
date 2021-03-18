import collections


groupp = {}
with open('/home/roman/src/Object1.csv', 'r') as fi:
    for ln in fi:
        fields = ln.split(';')
        if flt := groupp.get(fields[1]):
            pass
        else:
            flt = collections.defaultdict(list)
        flt[fields[2]].append(fields[3].strip())
        groupp[fields[1]] = flt



with open('/home/roman/src/filters.txt', 'w') as fo:
    for db, object_filters in groupp.items():
        fo.write(f"\nDatabase: {db}\n")
        for obj_type, filter_val in object_filters.items():
            fo.write(f"{obj_type}: {'|'.join(filter_val)}\n")

        

