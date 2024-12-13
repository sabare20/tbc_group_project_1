with open('homework18/data.txt', 'r') as file:
    with open('homework18/high.txt', 'w') as high, open('homework18/small.txt', 'w') as small:
        for line in file:
            line = line.strip()
            parts = line.split(',')
            value = float(parts[2]) * float(parts[3])
            if value >= 10:
                high.write(f'{line}\n')
            else:
                small.write(f'{line}\n')