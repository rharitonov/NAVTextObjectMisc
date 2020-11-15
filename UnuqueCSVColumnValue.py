item = {}


with open('C:/src/azure_category_prediction/datasets\item.csv', 'r', encoding='utf-8') as fi:
    for n, line in enumerate(fi):
        words = line.strip().split(';')
        if item.get(words[0], 0) == 1:
            print(n)
        else:
            item[words[0]] = 1
               