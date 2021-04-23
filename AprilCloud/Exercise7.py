import random

if __name__ == '__main__':
    # 1
    s = set()
    for i in range(1500, 2701):
        if (i % 7) == 0:
            if (i % 5) == 0:
                s.add(i)
    print(str(s)[1:len(s)-1])

    # 2
    def convert(temp, c):
        if c == 'C':
            return temp*9/5 + 32
        elif c == 'F':
            return ((temp-32)/9)*5
        else:
            return 'not accepted'
    # Could use list comprehension
    print('60 C is ' + str(convert(60, 'C')) + ' F')
    print('45 F is ' + str(convert(45, 'F')) + ' C')

    # 3
    y = random.randint(1, 9)
    while True:
        print("Guess a number between 1 and 9")
        x = input()
        if x == str(y):
            print('Well guessed!')
            break

    # 4
    for i in range(1, 10):
        s = ''
        if i <= 5:
            for j in range(i):
                s += '*'
        else:
            for j in range(5-(i-5)):
                s += '*'
        print(s)

    # 6
    x = input()
    print(x[::-1])

    # 7
    def odd_even_counter(lst_param):
        odd = 0
        even = 0
        for item in lst_param:
            if item % 2 == 0:
                even += 1
            else:
                odd += 1
        print('Number of even numbers: ' + str(even))
        print('Number of odd numbers: ' + str(odd))
    odd_even_counter((1, 2, 3, 4, 5, 6, 7, 8, 9))

    # 8
    datalist = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
    for item in datalist:
        print(str(item) + '\t' + str(type(item)))

    # 9
    s = ''
    for i in range(7):
        if i == 3 or i == 6:
            continue
        s += ' ' + str(i)
    print(s)
