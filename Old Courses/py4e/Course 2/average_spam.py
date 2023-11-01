# Use the file name mbox-short.txt as the file name
fname = input('Enter file name: ')
fh = open(fname)

count = 0
addition = 0

for line in fh:
    if not line.startswith('X-DSPAM-Confidence:') :
        continue
    ly = line.rstrip()
    count = count + 1
    addition = addition + float(ly[19:])

print('Average spam confidence:', addition/count)
