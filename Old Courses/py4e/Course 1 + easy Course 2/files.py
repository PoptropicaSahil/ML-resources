f_read = input('Enter file name - ')
f_work = open(f_read)

for lx in f_work:
    ly = lx.rstrip()
    print(ly.upper())
