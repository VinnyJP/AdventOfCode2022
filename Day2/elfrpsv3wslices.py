def outcome(argument):
    switcher = {
        'AX': 4,
        'AY': 8,
        'AZ': 3,
        'BX': 1,
        'BY': 5,
        'BZ': 9,
        'CX': 7,
        'CY': 2,
        'CZ': 6
        }
    return switcher.get(argument)



file = open('input.txt', mode = 'r', encoding = 'utf-8-sig')
data = file.read()
data_stripped = data.replace(' ', '').replace('\n', '')
file.close()


total_score = 0
n = 0

while n < len(data_stripped):
    total_score += outcome(data_stripped[n:n+2])
    n += 2
print(total_score)
