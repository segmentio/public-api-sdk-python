from tabulate import tabulate


def print_table(table, headers=None):
    print(tabulate(table, headers if headers else []))


def merge(d1, d2):
    """
    Merge two dictionaries. In case of duplicate keys, this function will return values from the 2nd dictionary

    :return dict: the merged dictionary
    """
    d3 = {}
    if d1:
        d3.update(d1)
    if d2:
        d3.update(d2)
    return d3
