from random import randint


def generate_random_number(x, y):
    return randint(x, y)


def shuffle(cards):
    for index, num in enumerate(cards):
        swap_with = generate_random_number(0, index)
        temp = cards[index]
        cards[index] = cards[swap_with]
        cards[swap_with] = temp
    return cards;

if __name__ == '__main__':
    cards = list(xrange(1, 53))
    shuffled = shuffle(cards)
    print shuffled
