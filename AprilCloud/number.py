import math

if __name__ == '__main__':
    print((50 + 50) + (100 - 10))
    print(30 * 6)
    # bitwise xor returns 0000 as they are the same number 0110
    print(6 ^ 6)
    print(6 ** 6)
    print(6 + 6 + 6 + 6 + 6 + 6)
    print("Hello World")
    print("Hello World : " + str(10))

    p = 800000
    r = 6
    l = 103


    def calculate_monthly_payment(p, r, l):
        amount = r / 12 / 100 * p / (1 - (1 + r / 12 / 100) ** -l)
        return math.ceil(amount)


    print(calculate_monthly_payment(p, r, l))
