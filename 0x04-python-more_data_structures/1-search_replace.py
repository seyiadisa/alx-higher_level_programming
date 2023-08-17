#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()

    try:
        while new_list.index(search):
            new_list[new_list.index(search)] = replace
    except ValueError:
        return new_list
