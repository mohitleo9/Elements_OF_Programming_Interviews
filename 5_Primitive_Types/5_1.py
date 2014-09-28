def count_parity(i):
    res = 0
    while i:
        res += i & 1
        i = i >> 1
    return res


def main():
    num = 7
    print "starting"
    print bin(num)
    print count_parity(num)


if __name__ == '__main__':
    main()
