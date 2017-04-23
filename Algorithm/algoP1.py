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

# http://stackoverflow.com/questions/28375843/shortest-word-in-a-dictionary-containing-all-letters
# google question. Here license number is the array of characters


def smallest_word_dictionary(dictionary, license_no):
    dictionary.sort(key=len)
    inverted_index = create_inverted_index(dictionary)
    license_dict = create_license_dict(license_no)
    valids = []
    for key, value in license_dict.iteritems():
        if value > 1:
            a1 = find_valid_words(value, inverted_index[key])
        else:
            a1 = inverted_index[key]
        valids.append(a1)
    x1 = valids[0]
    for s in xrange(1, len(valids)):
        x2 = valids[s]
        x = find_intersection(x1, x2)
        x1 = x
    return dictionary[x1[0]]


def create_license_dict(license_no):
    import re
    license_dict = {}
    valid_no = re.sub(r"[^A-Za-z]+", '', license_no)
    for x in valid_no:
        if not license_dict.get(x.lower(), None):
            license_dict[x.lower()] = 1
        else:
            v = license_dict[x.lower()]
            license_dict[x.lower()] = v + 1
    return license_dict


def create_inverted_index(dictionary):
    inverted_index = {}
    for i, word in enumerate(dictionary):
        for c in word:
            if not inverted_index.get(c.lower(), None):
                inverted_index[c] = [i]
            else:
                existing_list = inverted_index[c.lower()]
                existing_list.append(i)
    return inverted_index


def find_intersection(arr1, arr2):
    result = []
    i = j = 0
    while (i < len(arr1) and j < len(arr2)):
        if arr1[i] == arr2[j]:
            result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return result


def find_valid_words(value, word_list):
    d = {}
    l = []
    for w in word_list:
        if not d.get(w, None):
            d[w] = 1
        else:
            v = d[w]
            d[w] = v + 1
    for key, val in d.iteritems():
        if val == value:
            l.append(key)
    return l

    # hill problem
    '''
    Given a list/array of integers A[].

There're a list of queries having a structure of: Check(Left, Right) to check
 if array elements from Left => Right forming a hill.

A hill is a sequence of integers, that at first it doesn't decrease, but then
 it doesn't increase after the peak.

For example: 2 3 3 6 5 4 is a hill with 6 as the peak. 2 3 6 4 5 isn't because
 4 < 5 and it shouldn't decrease after the peak.

A bigger example

A = [2, 3, 3, 6, 5, 4, 7]
Check(0, 5) => True
Check(0, 1) => True
Check(3, 4) => True
Check(3, 5) => True
Check(4, 6) => False
'''


def is_hill(numbers, start, finish):
    initial = current = 1
    change = False
    if numbers[start] > numbers[start + 1]:
        initial = current = -1
    for i in xrange(start + 1, finish):
        if numbers[i] <= numbers[i + 1]:
            current = 1
        else:
            current = -1
        # if started downhill you can't go up
        if initial == -1 and current == 1:
            return False
        # started up then went down this is when changed = True and again up
        if change and initial == current:
            return False
        # started up then went down changed = True
        if not change and (initial != current):
            change = True
    return True

# combination using grey code logic
# http://www.martinbroadhurst.com/combinatorial-algorithms.html#permutations


def combinations():
    word = ['a', 'b', 'c', 'd', 'e']
    current = [False, False, False, False, False]
    j = 0
    count = 0
    while(True):
        j = get_bit_to_change(current)
        print_combinations(current, word)
        if j > len(current) - 1:
            break
        current[j] = not (current[j])
        count += 1


def get_bit_to_change(current):
    no_of_1 = 0
    first_pos_of_1 = -1
    for i in xrange(0, len(current)):
        if current[i]:
                no_of_1 += 1
                if first_pos_of_1 == -1:
                    first_pos_of_1 = i
        # even number
    if not no_of_1 % 2:
        j = 0
    else:
        j = first_pos_of_1 + 1
    return j


def print_combinations(current, word):
    s = ''
    for x in xrange(0, len(current)):
        if current[x]:
            s = s + word[x]
    print s


def palindrome_sentence(sentence):
    i = 0
    j = -1
    palindrome = True
    while (i - j <= len(sentence)):
        if sentence[i].isspace():
            i += 1
            continue
        if sentence[j].isspace():
            j = j - 1
            continue
        if sentence[i].lower() != sentence[j].lower():
            palindrome = False
            print sentence[i]
            print sentence[j]
            print i
            print j
            break
        else:
            i = i + 1
            j = j - 1
    return palindrome


def permutation(prefix, word):
    if not len(word):
        print prefix + word
    for i in xrange(0, len(word)):
        permutation(prefix + word[i],
                    word[0: i] + word[i + 1: len(word)])

# (google) https://www.careercup.com/question?id=5706187292016640


def get_max_count_google(a):
    pos = []
    max_count = 0
    from heapq import heappush, heappop
    min_heap = []
    for x in xrange(0, len(a)):
        heappush(min_heap, (a[x], x))
    while len(min_heap) > 0:
        number, position = heappop(min_heap)
        pos.append(position)
        # checks how many pos > current.pos have already been used up
        x = sum(i > position for i in pos)
        count = len(a) - 1 - position - x
        max_count = max(max_count, count)
    print max_count

# (google) https://www.careercup.com/question?id=5687411305611264


class LargeNumbers():
    numbers = []

    def __init__(self, numbers):
        self.numbers = numbers

    @property
    def display_large_no(self):
        print (''.join([str(n) for n in self.numbers]))

    @property
    def increment_no(self):
        first_pos = -len(self.numbers)
        for x in xrange(-1, first_pos - 1, -1):
            number = self.numbers[x] + 1
            if number % 10 == 0:
                self.numbers[x], carry_forward = self.get_no(
                    number, self.numbers[x])
            else:
                self.numbers[x] = number
                carry_forward = False
            if not carry_forward:
                break
        if carry_forward:
            self.numbers[first_pos] = '1' + self.numbers[first_pos]

    def get_no(self, number, x):
        s = ''
        if len(str(number)) == len(str(x)):
            return number, False
        for p in xrange(0, len(str(x))):
            s = s + '0'
        return s, True

# (google) https://www.careercup.com/question?id=5660887265312768


def MatchAllPatterns(pattern, str_list):
    output = []
    for p in str_list:
        if isPatternMatch(pattern, p):
            output.append(p)
    print pattern, '->', output


def isPatternMatch(pattern, a_str):
    split_list = splitAtUpperCase(pattern)
    if not a_str.startswith(split_list[0]):
        return False
    split_len = len(split_list[0])
    idx = 0
    for x in split_list[1:]:
        if x in a_str[idx + split_len:]:
            idx = a_str.index(x)
            split_len = len(x)
            print idx, split_len, x
        else:
            return False
    return True


def splitAtUpperCase(word):
    char_list = [c for c in word]
    for char in char_list:
        if char != char_list[0] and char.isupper():
            char_list[char_list.index(char)] = ' ' + char
    return ''.join(char_list).split(' ')

# http://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python/11015381#11015381

# (google) https://www.careercup.com/question?id=5651833474252800


def get_hotels(scores, min_avg):
    # hotel_rates = { hotel_id: (sum_score, frequency_of_hotel_occurence)}
    hotel_rates = {}
    hotels = []
    for s in scores:
        hotel_id = s['hotel_id']
        hotel_rates[hotel_id] = (
            hotel_rates.get(hotel_id, (0, 0))[0] + s['score'],
            hotel_rates.get(hotel_id, (0, 0))[1] + 1)
    print hotel_rates
    for key, value in hotel_rates.iteritems():
        if value[0] / value[1] >= min_avg:
            hotels.append(key)
    print hotels


def binary_search(s, min_no, max_no, no):
    while max_no >= min_no:
        mid = (min_no + max_no) / 2
        if no == s[mid]:
            return True
        if no > s[mid]:
            min_no = mid + 1
        else:
            max_no = mid - 1
    return False


def binary_search_recursive(s, no):
    min_no = 0
    max_no = len(s) - 1
    if len(s) == 1:
        if s[0] == no:
            return True
        else:
            return False
    mid = len(s) / 2
    if no == s[mid]:
        return True
    if no > s[mid]:
        min_no = mid + 1
    else:
        max_no = mid - 1
    return binary_search_recursive(s[min_no:max_no + 1], no)

# (google) https://www.careercup.com/question?id=5767203879124992


def calculate_no_of_zero(matrix):
    total_zeros = 0
    for x in xrange(0, len(matrix)):
        total_zeros += count_zeros_per_row(matrix[x], 0, len(matrix[x]) - 1)
    print total_zeros


def count_zeros_per_row(row, i_min, i_max):
    index = -1
    while i_max >= i_min:
        mid = (i_min + i_max) / 2
        if row[mid] == 0:
            i_min = mid + 1
        else:
            i_max = mid - 1
            index = mid
    if index == -1:
        return len(row)
    else:
        return index


class CachedItem(object):
    def __init__(self, key, value):
        self.worker_id = key
        self.name = value


class LRU(object):
    def __init__(self, max_cache_length):
        self.cache = []
        self.cache_map = dict()
        self.max_cache_length = max_cache_length
        self.max_priority = 0

    def insert(self, item):
        self.max_priority += 1
        if len(self.cache) < self.max_cache_length:
            self.cache.append((self.max_priority, item.worker_id))
            self.cache_map[item.worker_id] = item
        else:
            self.cache.sort()
            self.cache_map.pop(self.cache[0][1], None)
            self.cache = self.cache[1:]
            self.cache.append((self.max_priority, item.worker_id))
            self.cache_map[item.worker_id] = item

    def increment_priority(self, key):
        # cache = [(priority, worker_id)...]
        self.max_priority += 1
        for i in xrange(len(self.cache)):
            worker_id = self.cache[i][1]
            if worker_id == key:
                self.cache[i][0] = self.max_priority
                break

    def get(self, key):
        if self.cache_map.get(key, None):
            self.increment_priority(key)
            print 'Cache hit'
            return self.cache_map[key]
        else:
            item = CachedItem(key, "TestName")
            self.insert(item)
            print 'Cache Miss'
            return item


def create_objects_to_cache():
    c1 = CachedItem('c1')
    c2 = CachedItem('c2')
    c3 = CachedItem('c3')
    c4 = CachedItem('c4')
    return c1, c2, c3, c4
