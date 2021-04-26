def inflate_books(book):
    if book[3] < 100:
        book[3] += 10
    return book


def inflate_books_tuple(book):
    lst = [book[1][0], book[1][1]]
    if book[1][2] < 100:
        lst.append(book[1][2] + 10)
    new_book = [book[0], tuple(lst)]
    return new_book


def inflate_books_list(books):
    return [tuple(books), tuple(map(lambda book: inflate_books(book), books))]


def inflate_books_list_tuple(books):
    return [tuple(books), tuple(map(lambda book: inflate_books_tuple(book), books))]


if __name__ == '__main__':
    # 2
    book_list = [[34597, 'Learning Python, Mark Lutz', 4, 40.95],
             [98762, 'Programming Python, Mark Lutz', 5, 56.80],
             [77226, 'Head First Python, Paul Barry', 3, 32.95],
             [88112, 'Einfujrung in Python3, Bernd Klein', 3, 24.99]]
    print(book_list)
    print(inflate_books_list(book_list))

    # 3
    book_list = [[34597, ('Learning Python, Mark Lutz', 4, 40.95)],
             [98762, ('Programming Python, Mark Lutz', 5, 56.80)],
             [77226, ('Head First Python, Paul Barry', 3, 32.95)],
             [88112, ('Einfujrung in Python3, Bernd Klein', 3, 24.99)]]
    print(book_list)
    print(inflate_books_list_tuple(book_list))
