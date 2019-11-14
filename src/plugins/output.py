import sys
import time


def main(a):
    for dummy in range(3):
        time.sleep(.1)
        print(a)


if __name__ == '__main__':
    a = sys.stdin.read()
    main(a)