# python3


def poly_hash(text, begin, length, a, p, last=None):
    '''
    h(a, p) = sum([])
    '''
    # if not last:
    #     ret = 0
    #     for i in range(begin, begin + length):
    #         ret += (ord(text[i]) * a) % p
    # else:
    #     ret = last -
    #     pass
    return 0

def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    return [
        i for i in range(len(text) - len(pattern) + 1)
        if text[i:i + len(pattern)] == pattern
    ]


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
