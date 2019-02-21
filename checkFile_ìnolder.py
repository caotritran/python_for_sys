import os


def main():
    filename = '/home/tritran/Desktop/checkfile/'

    for i in os.listdir(filename):
        #print(i)
        if i.endswith('.tld'):
            #print(i)
            path = filename + i
            print(path)
            with open(path, 'at') as f:
                f.write("HAPPY NEW YEAR 2019!!!\n")


if __name__ == '__main__':
    main()
