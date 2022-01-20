class RemoteControl():
    def __init__(self):
        self.channels = ["HBO", "CNN", "ABC", "ESPN"]
        self.index = -1  # equals -1 when TV is off.

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration

        return self.channels[self.index]


if __name__ == '__main__':

    r = RemoteControl()
    itr = iter(r)
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    # print(next(itr))

    """
    a = ["just", "a", "little", "array"]

    dir(a)

    itr = iter(a)
    print(itr)

    next(itr)
    print(itr)

    next(itr)
    print(itr)

    next(itr)
    print(itr)

    next(itr)
    print(itr)
    """
