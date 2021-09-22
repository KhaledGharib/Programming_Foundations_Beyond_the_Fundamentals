infile = open('values.txt', 'rt')
outfile = open('Total.txt', 'wt')
print('Processing input')
sum = 0
for line in infile:
    print(".")
    sum += int(line)
    print(line.rstrip(), file=outfile)
print('\nTotal: ' + str(sum), file=outfile)

outfile.close()
print('Output complete')

