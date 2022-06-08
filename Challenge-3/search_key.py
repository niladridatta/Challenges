#!/usr/bin/python3

import sys

def getKey(obj: dict):
    keys = list(obj)
    return keys[0]


def getValue(obj: dict, key: str, matched = False):

    if type(obj) is not dict and not matched:
        sys.exit("Key not found")

    if (matched or (key in obj.keys())):
        if type(obj[key]) is dict:
            return getValue(obj[key], getKey(obj[key]), True)
        else:
            return obj[getKey(obj)]
    else:
        nestedKey = getKey(obj)
        return getValue(obj[nestedKey], key, False)


if __name__ == '__main__':

    object = {'a': {'b': {'c': 'd'}}}
    print("object: ", object)

    key = input("\nEnter key: ")

    value = getValue(object, key)
    print(value)



"""

Test runs:
-------------


$ ./search_key.py

object:  {'a': {'b': {'c': 'd'}}}

Enter key: a
d


$ ./search_key.py

object:  {'a': {'b': {'c': 'd'}}}

Enter key: b
d


$ ./search_key.py

object:  {'a': {'b': {'c': 'd'}}}

Enter key: c
d


$ ./search_key.py

object:  {'a': {'b': {'c': 'd'}}}

Enter key: d
Key not found


"""