#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dict = a_dictionary.copy()

    try:
        del new_dict[key]
    except KeyError:
        return a_dictionary

    return new_dict
