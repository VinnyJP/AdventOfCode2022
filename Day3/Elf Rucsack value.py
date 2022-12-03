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

for line in lines:
    x = (len(line)//2)
    a = list(set(line[:x])&set(line[x:]))
    accum += alphadict[a[0]]

print(accum)
