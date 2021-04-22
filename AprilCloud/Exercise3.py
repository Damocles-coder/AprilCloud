if __name__ == '__main__':
    print("Hello World"[8])
    print("thinker"[2:5])
    s = "hello"
    print(s[1])
    s = "Sammy"
    print(s[2:])
    print(set("Mississippi"))


    def is_palindrome(word):
        if word.lower()[::-1] == word.lower():
            return "Y"
        return "N"

    print("input data:")
    x = int(input())
    a = []
    for i in range(x):
        a.append(input())
    print("\nanswer:")
    y = ""
    for i in range(x):
        y += is_palindrome(a[i])
    print(y)
