import functools


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('{} executed in {} ms'.format(fn.__name__, '11.00'))
        return fn(*args, **kw)

    return wrapper


@metric
def test():
    print('this is test func')


test()
print(test.__name__)
