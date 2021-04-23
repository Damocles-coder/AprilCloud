if __name__ == '__main__':
    lst = ['person1', 'person2', 'person3', 'person4']

    def threes_a_crowd(lst_param):
        if len(lst_param) >= 3:
            print('The room is crowded')

    threes_a_crowd(lst)
    lst.pop()
    lst.pop()
    threes_a_crowd(lst)

    # part 2
    lst = ['person1', 'person2', 'person3', 'person4']

    def threes_a_crowd(lst_param):
        if len(lst_param) >= 3:
            print('The room is crowded')
        else:
            print('The room is not very crowded')

    threes_a_crowd(lst)
    lst.pop()
    lst.pop()
    threes_a_crowd(lst)

    # part 2
    lst = ['person1', 'person2', 'person3', 'person4', 'person5', 'person6']


    def threes_a_crowd(lst_param):
        if len(lst_param) > 5:
            print('There is a mob in the room')
        elif len(lst_param) >= 3:
            print('The room is crowded')
        elif len(lst_param) > 0:
            print('The room is not very crowded')
        else:
            print('Nobody else was in the room where it happened')

    threes_a_crowd(lst)
    lst.pop()
    lst.pop()
    lst.pop()
    threes_a_crowd(lst)
    lst.pop()
    threes_a_crowd(lst)
    lst.pop()
    lst.pop()
    threes_a_crowd(lst)
