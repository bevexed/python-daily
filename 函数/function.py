def a():
    """
    这是一个函数
    :return:
    """
    print('function')


a()


def sum1(*args):
    res = 0
    for item in args:
        res += item
        pass
    return res


print(sum1(1, 3, 4, 5))


def get_odd(args):
    lists = []
    for item in args:
        if item % 2 == 1:
            lists.append(item)

    return lists


print(get_odd([1, 2, 3, 4, 5]))
