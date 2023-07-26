import collections


def remove_nulls(item: dict):
    formatted = dict()
    for key, value in item.items():
        if type(value) is dict:
            formatted[key] = remove_nulls(value)
        elif value is not None:
            formatted[key] = value
    print(formatted)
    return formatted
