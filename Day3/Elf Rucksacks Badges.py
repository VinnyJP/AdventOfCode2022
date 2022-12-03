file = open('input.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

alphadict = {}
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = 1
accum = 0

for i in alphabet:
    alphadict[i] = n
    n += 1

while len(lines) > 0:
    a = list(set(lines.pop().replace('\n', ''))&set(lines.pop().replace('\n', ''))&set(lines.pop().replace('\n', '')))
    accum += alphadict[a[0]]
    
print(accum)
