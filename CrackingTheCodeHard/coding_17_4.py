def convert_to_decimal(arr):
    decimal_arr = []
    for index, binary in enumerate(arr):
        decimal_arr.append(int(arr[index], 2))
    return decimal_arr


def find_missing_number(arr):
    should_be_sum = 0
    actual_sum = 0
    n = len(arr) + 1
    for i in xrange(0, n, 1):
        should_be_sum += i
    decimal_arr = convert_to_decimal(arr)
    for j in decimal_arr:
        actual_sum += j
    return should_be_sum - actual_sum


def is_even(n):
    return n % 2 == 0


def remove_from_array(arr, missing_bit, right_shift):
    temp = list(arr)
    for num in temp:
        binary_format = int(num, 2)
        bit = binary_format >> right_shift & 0001
        if bit != missing_bit:
            arr.remove(num)
    return arr


def calculate_no_of_x_in_y_significant_bits(arr, x, right_shift):
    count_x = 0
    for num in arr:
        binary_format = int(num, 2)
        bit = binary_format >> right_shift & 0001
        if bit == x:
            count_x += 1
    return count_x


def find_missing_number_two(arr):
    missing_no = []
    y_significant_bit = 0
    while len(arr) > 0:
        count_one = calculate_no_of_x_in_y_significant_bits(arr, 1, y_significant_bit)
        count_zero = calculate_no_of_x_in_y_significant_bits(arr, 0, y_significant_bit)
        missing_bit = 0 if count_zero <= count_one else 1
        missing_no.insert(0, missing_bit)
        arr = remove_from_array(arr, missing_bit, y_significant_bit)
        y_significant_bit += 1
    print ''.join(str(x) for x in missing_no)


if __name__ == '__main__':
    binary_arr = []
    length_of_binary_number = 4  # take 4 bit integer since we are only going for n = 13
    n = 13
    for i in xrange(0, n + 1):
        if i == 5:
            continue
        binary_arr.append(bin(i)[2:].zfill(length_of_binary_number))
    print binary_arr
    find_missing_number_two(binary_arr)
