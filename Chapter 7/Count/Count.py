class Count:
    def __init__(self, count=0):
        self.count = count


def main():
    c = Count()
    times = 0
    for i in range(100):
        increment(c, times)
        print("count is ", c.count)
        print("time is ", times)


def increment(c, times):
    c.count += 1
    times += 1


main()
