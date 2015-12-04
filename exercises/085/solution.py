def sort_a_list(l):
    for i in l:
        return sorted(l, reverse=True)


def sort_by_mark(my_class):
    for i in my_class:
        return sorted(my_class, reverse=True)


import operator
def sort_by_name(my_class):
    for i in my_class:
        return sorted(my_class, key=operator.itemgetter(1))
