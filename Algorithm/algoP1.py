'''
(D1)

Given an array/list of number with N elements.

With that array/list, there's a list of queries asking: Having index X,
 calculate the multiplication of every elements except X.

Example, list [2,3,4]
- index=0, answer=12 (3 * 4)
- index=1, answer=8 (2 * 4)
- index=2, answer=6 (2 * 3)
'''


def multiply_array(sample):
    left = list(xrange(len(sample)))
    right = list(xrange(len(sample)))
    product = list(xrange(len(sample)))
    p = 1
    for i in xrange(len(sample)):
        left[i] = p
        p = p * sample[i]
    p = 1
    x = -1
    for i in xrange(len(sample)):
        right[len(sample) - 1 - i] = p
        # to iterate x from backwards
        p = p * sample[x]
        x = x - 1
    for k in xrange(len(sample)):
        product[k] = left[k] * right[k]
    print product