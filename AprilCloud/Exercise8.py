if __name__ == '__main__':
    # 1
    def hello():
        print("Hello World")
    hello()

    # 2
    def func1(name):
        print('Hi My name is ' + name)
    func1(input())

    # 3
    def func3(x, y, z):
        if z:
            return x
        else:
            return y
    func3('hello', 'goodbye', False)

    # 4
    def func4(x, y):
        return x*y
    print(func4(2, 3))

    # 5
    def is_even(x):
        return x % 2 == 0
    print(is_even(2))
    print(is_even(3))

    # 6
    def func6(x, y):
        return x > y
    print(func6(12, 34))

    # 7
    def func7(*args):
        j = 0
        for i in args:
            j += i
        return j
    print(func7(2, 3, 5, 8))

    # 8
    def func8(*args):
        return list(filter(is_even, args))
    print(func8(10, 3, 4, 2, 7, 0, 68))

    # 9
    def func9(word):
        j = ''
        k = 0
        for i in word:
            if k % 2 != 0:
                j += i.upper()
            else:
                j += i.lower()
            k += 1
        return j
    print(func9('func9834'))

    # 10, 11, 12 not sure what python notebook exercises are referring to
    # 13 might be able to do with lambda, but not sure how to pass in index
    def func13(word):
        j = ''
        k = 0
        for i in word:
            if k == 0 or k == 3:
                j += i.upper()
            else:
                j += i
            k += 1
        return j
    print(func13('word'))
