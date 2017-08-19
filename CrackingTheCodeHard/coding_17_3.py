from random import randint


def generate_random_number(upper_limit):
    return randint(0, upper_limit)


def generate_sub_array(original_array, sub_array_size):
    subset = original_array[:sub_array_size]
    for index, num in enumerate(original_array[sub_array_size:]):
        k = generate_random_number(index + sub_array_size)
        if k < sub_array_size:
            subset[k] = original_array[index + sub_array_size]
    return subset

if __name__ == '__main__':
    original_array = list(xrange(0, 10))
    print original_array
    m = 6
    print generate_sub_array(original_array, m)