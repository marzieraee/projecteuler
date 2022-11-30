dic = {'saeed':27, 'marzy':25}
print(dic['saeed'])
print(list(dic))

print(dict((('saeed',27),('marzy',25))))
print('mar' in dic)
print(dic['saeed'])

dic['saeed'] = dic.get('saeed') + 1
print(dic)
print(dic.values())

dic2 = dict(ali=20,saeed=27)
print(dic2)