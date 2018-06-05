def findMinAndMax(L):
    if len(L) <= 1:
        return L
    index = len(L) // 2
    middle = L[index]
    L = L[:index] + L[index + 1:]
    left = []
    right = []
    for i in L:
        if i < middle:
            left.append(i)
        else:
            right.append(i)
    return findMinAndMax(left) + [middle] + findMinAndMax(right)


print(findMinAndMax([4, 9, 3, 9, 3, 2, 5, 3, 7]))
