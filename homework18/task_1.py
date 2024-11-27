with open('homework18/data.txt','r') as file:
    with open('homework18/high.txt','w') as high , open('homework18/small.txt','w') as small:
        for line in file:
            line=line.strip
            value = float(line.split(',')[2])*float(line.split(',')[3])
            if  value >= 10:
                high.write(f'{line}\n')
            elif value < 10:
                small.write(f'{line}\n')
