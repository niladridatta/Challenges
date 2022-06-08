#! /usr/bin/python3

from metadata import metadata

def dict_extract(key, var):
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in dict_extract(key, d):
                        yield result


def find_key(key):
    data = metadata()
    return list(dict_extract(key, data))


if __name__ == '__main__':
    key = input("Enter key: ")
    data = find_key(key)
    print(data)
