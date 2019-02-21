import random


def randomIP():
    with open('listip.txt', 'rt') as f:
        data = f.readlines()

    iprandom = random.choice(data)

    with open('listip_new.txt', 'at') as f:
        f.write(iprandom)

    return 'random {} to new list'.format(iprandom)


def main():
    result = randomIP()
    print(result)


if __name__ == '__main__':
    main()
