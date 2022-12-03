def rps_vs_A_dict(argument):
    switcher = {
        'X': 3,
        'Y': 6,
        'Z': 0
        }
    return switcher.get(argument)

def rps_vs_B_dict(argument):
    switcher = {
        'X': 0,
        'Y': 3,
        'Z': 6
        }
    return switcher.get(argument)

def rps_vs_C_dict(argument):
    switcher = {
        'X': 6,
        'Y': 0,
        'Z': 3
        }
    return switcher.get(argument)
def rps_value_dict(argument):
    switcher = {
        'X': 1,
        'Y': 2,
        'Z': 3
        }
    return switcher.get(argument)


file = open('input.txt', mode = 'r', encoding = 'utf-8-sig')
data = file.read()
data_strip_spaces = data.replace(' ', '')
data_stripped = data_strip_spaces.replace('\n', '')
file.close()

opp_list = []
my_list = []
n = 0
total_score = 0


for c in data_stripped:
    if len(opp_list) > len(my_list):
        my_list.append(c)
    else:
        opp_list.append(c)

while n < len(opp_list):
    if opp_list[n] == 'A':
        total_score += rps_value_dict(my_list[n]) + rps_vs_A_dict(my_list[n])
    elif opp_list[n] == 'B':
        total_score += rps_value_dict(my_list[n]) + rps_vs_B_dict(my_list[n])
    else:
        total_score += rps_value_dict(my_list[n]) + rps_vs_C_dict(my_list[n])
    n += 1

print(total_score)
