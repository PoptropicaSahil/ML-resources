counts = dict()
names = ['csev', 'cwen', 'csev', 'zz', 'cwen','xx', 'xx','xx']
for name in names :
    counts[name] = counts.get(name,0) + 1
print(counts)
