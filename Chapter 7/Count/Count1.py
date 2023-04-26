class Count:
    def __init__(self, count=0):
        self.count = count


def main():
    c = Count()
    n = 1
    m(c, n)
    print("count is ", c.count)
    print("n is ", n)


def m(c, n):
    c.count += 1
    n = 3


main()
