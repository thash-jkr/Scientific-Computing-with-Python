import re


def arithmetic_arranger(problems, flag=False):
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for pro in problems:

        i = pro.split()
        if i[1] != '+' and i[1] != '-':
            return "Error: Operator must be '+' or '-'."
        if (re.search("[^\s0-9.+-]", pro)):
            return "Error: Numbers must only contain digits."
        if len(i[0]) > 4 or len(i[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if int(i[0]) > int(i[2]):
            line1 += '  ' + i[0] + '    '
            line2 += i[1] + (' ' * (len(i[0]) - len(i[2]) + 1)) + i[2] + '    '
            dot = (len(i[0]) + 2)
            line3 += '-' * dot + '    '
        else:
            line1 += (' ' * (len(i[2]) - len(i[0]) + 2)) + i[0] + '    '
            line2 += i[1] + ' ' + i[2] + '    '
            dot = (len(i[2]) + 2)
            line3 += '-' * dot + '    '
        if flag:
            if i[1] == '+':
                add = int(i[0]) + int(i[2])
            else:
                add = int(i[0]) - int(i[2])
            sol = str(add)
            l2 = dot - len(sol)
            line4 += (' ' * l2) + sol + '    '

    line1 = line1[:-4] + '\n'
    line2 = line2[:-4] + '\n'
    line3 = line3[:-4]
    arranged_problems = line1 + line2 + line3
    if flag:
        line4 = line4[:-4]
        arranged_problems += '\n' + line4
    return arranged_problems
