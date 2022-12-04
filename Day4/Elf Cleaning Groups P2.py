def incrementer(arg1, arg2):
    
    a = []
    
    while arg1 <= arg2:
        a.append(arg1)
        arg1 += 1

    return set(a)

file = open('input.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

pairs = 0

for line in lines:
    a = line.split(',')
    b = a[0].split('-')
    c = a[1].split('-')
    runb = incrementer(int(b[0]), int(b[1]))
    runc = incrementer(int(c[0]), int(c[1]))
    if runb & runc:
        pairs += 1
    else:
        continue

print(pairs)
