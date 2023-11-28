class DataStream:

    def __init__(self, value: int, k: int):
        self.counter = 0
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:

        if num == self.value:
            self.counter += 1
        else:
            self.counter = 0

        if self.counter >= self.k:
            return True
        else:
            False
