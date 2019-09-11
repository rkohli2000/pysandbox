""" get the nth fib number 0, 1, 1, 2, 3, 5... """


# Time O(2 ^ n)  Space O(n)
def getNthFib1(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib1(n - 1) + getNthFib1(n - 2)



# use memoization
# Time O(n)  Space O(n)
def getNthFib2(n, memoize = {1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib2(n - 1, memoize) + getNthFib2(n - 2, memoize)
        return memoize[n]

if __name__ == "__main__":
    print('fib is %d' % (getNthFib1(9)))
    print('fib is %d' % (getNthFib2(10)))
    print('fib is %d' % (getNthFib1(11)))

    for i in range(0, 20):
        print(getNthFib1(i))


