def bmi_answer(x, y):
    bmi = x / y**2
    if bmi >= 30:
        return 'obese '
    elif bmi >= 25:
        return 'over '
    elif bmi >= 18.5:
        return 'normal '
    else:
        return 'under '


def bmi_list(z):
    s = ''
    for i in range(int(z)):
        xy = input().split()
        s += bmi_answer(float(xy[0]), float(xy[1]))
    return s


if __name__ == '__main__':
    print('input data:')
    answer = bmi_list(input())
    print('\nanswer:')
    print(answer)

