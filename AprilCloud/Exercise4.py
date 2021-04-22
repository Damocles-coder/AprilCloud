if __name__ == '__main__':
    lst = [21, "Eyeshield", 7.4]
    print(lst)

    lst = [[1, 1], [1, 2]]
    print(lst[1][1])

    lst = ['a', 'b', 'c']
    print(lst[1:])

    days = {'Mon': 1, 'Tues': 2, 'Wed': 3, 'Thurs': 4, 'Fri': 5, 'Sat': 6, 'Sun': 7}
    print(days)

    d = {'k1': [1, 2, 3]}
    print(d['k1'][1])

    t = (1, (2, 3))
    print(t)

    s = set("Mississippi")
    s.add('X')
    print(s)
    print({1, 1, 2, 3})

    # Question 1
    s = set()
    for i in range(2000, 3201):
        if (i % 7) == 0:
            if (i % 5) != 0:
                s.add(i)
    print(str(s)[1:len(s)-1])

    # Question 2
    def factorial(number):
        x = 1
        for i2 in range(1, number+1):
            x *= i2
        return x
    x = input()
    print(factorial(int(x)))

    # Question 3
    d = dict()
    x = int(input())
    for i in range(1, x+1):
        d[i] = i * i
    print(d)

    # Question 4
    x = input().split(',')
    t = tuple(x)
    print(x)
    print(t)

    # Question 5
    class GetAndCapString(object):
        def __init__(self):
            self.s = ""

        def getString(self):
            self.s = input()

        def printString(self):
            print(self.s.upper())

    o = GetAndCapString()
    o.getString()
    o.printString()
