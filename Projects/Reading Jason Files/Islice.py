'''
Make an iterator that returns selected elements from the iterable. If start is non-zero,
then elements from the iterable are skipped until start is reached. Afterward, elements are returned consecutively unless
step is set higher than one which results in items being skipped. If stop is None,
then iteration continues until the iterator is exhausted, if at all; otherwise, it stops at the specified position.
If start is None, then iteration starts at zero. If step is None, then the step defaults to one.

*args allows us to pass a variable number of non-keyword arguments to a Python function.
'''
import sys


def islice(interable, *args):
    # islice('ABCDEFG', 2) --> A B
    # islice('ABCDEFG', 2, 4) --> C D
    # islice('ABCDEFG', 2, None) --> C D E F G
    # islice('ABCDEFG', 0, None, 2) --> A C E G
    s = slice(args)
    start, stop, step = s.start or 0, s.stop or sys.maxsize, s.step or 1
    it = iter(range(start, stop, step))
    try:
        nexti = next(int)
    except StopIteration:
        
