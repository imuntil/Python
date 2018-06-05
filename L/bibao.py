def createCounter():
    num = 1

    def counter():
        nonlocal num
        num += 1
        return num

    return counter


c = createCounter()
print(c(), c(), c())