class Frange:
    def __init__(self, left, right=None, step=None):
        self._left = left
        self._right = right
        self._step = step

        if not step:
            self._step = 1

        if self._right is None:
            self._right = 0
            self._left, self._right = self._right, self._left

    def __next__(self):
        if self._left >= self._right and self._step >= 0:
            raise StopIteration("stop")

        if self._left <= self._right and self._step < 0:
            raise StopIteration("stop")

        result = self._left
        self._left += self._step
        return result

    def __iter__(self):
        return self


assert list(Frange(5)) == [0, 1, 2, 3, 4]
assert list(Frange(2, 5)) == [2, 3, 4]
assert list(Frange(2, 10, 2)) == [2, 4, 6, 8]
assert list(Frange(10, 2, -2)) == [10, 8, 6, 4]
assert list(Frange(2, 5.5, 1.5)) == [2, 3.5, 5]
assert list(Frange(1, 5)) == [1, 2, 3, 4]
assert list(Frange(0, 5)) == [0, 1, 2, 3, 4]
assert list(Frange(0, 0)) == []
assert list(Frange(100, 0)) == []
print("SUCCESS!")
