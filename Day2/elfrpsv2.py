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
data_no_spaces = data.replace(' ', '')
file.close()

a = ''
my_list = []
total_score = 0



for i in data_no_spaces:
    if i == '\n':
        my_list.append(a)
        a = ''
        continue
    a += i

for i in my_list:
    total_score += outcome(i)

print(total_score)
