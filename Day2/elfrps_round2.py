def values(argument):
    switcher = {
        'AX': Z,
        'AY': X,
        'AZ': Y,
        'BX': X,
        'BY': Y,
        'BZ': Z,
        'CX': Y,
        'CY': Z,
        'CZ': X
        }
    return switcher.get(argument)

def outcomes(argument):
    switcher = {
        'X': 0,
        'Y': 3,
        'Z': 6
        }
    return switcher.get(argument)

file = open('input.txt', mode = 'r', encoding = 'utf-8-sig')
data = file.read()
data_stripped = data.replace(' ', '').replace('\n', '')
file.close()

X = 1
Y = 2
Z = 3
n = 0
total_score = 0

while n < len(data_stripped):
    if 'X' in data_stripped[n:n+2]:
        total_score += values(data_stripped[n:n+2]) + outcomes('X')
    elif 'Y' in data_stripped[n:n+2]:
        total_score += values(data_stripped[n:n+2]) + outcomes('Y')
    else:
        total_score += values(data_stripped[n:n+2]) + outcomes('Z')
    n += 2

print(total_score)
