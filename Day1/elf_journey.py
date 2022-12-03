file = open('input.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()
a = 0
b = 0
l = []
for line in lines:
    if line == '\n':
        l.append(b)
        b = 0
        continue
    b = int(line) + b
l.sort(reverse = True)
a = l.pop() + l.pop() + l.pop()
print(a)
