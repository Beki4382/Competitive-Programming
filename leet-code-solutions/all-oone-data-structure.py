class AllOne:
    def __init__(self):
        self.counter = dict()  
        self.prev_max_key = None
        self.prev_min_key = None

    def inc(self, key: str) -> None:
        self.prev_max_key, self.prev_min_key = None, None

        if key not in self.counter:
            self.counter[key] = 1
        else:
            self.counter[key] += 1

    def dec(self, key: str) -> None:
        self.prev_max_key, self.prev_min_key = None, None

        if self.counter[key] == 1:
            self.counter.pop(key)
        else:
            self.counter[key] -= 1

    def getMaxKey(self) -> str:
        if len(self.counter) == 0:
            return ""
        else:
            if self.prev_max_key is not None:
                return self.prev_max_key

            res = sorted(self.counter.items(), key=lambda x: x[1])[-1][0]
            self.prev_max_key = res

            return res

    def getMinKey(self) -> str:
        if len(self.counter) == 0:
            return ""
        else:
            if self.prev_min_key is not None:
                return self.prev_min_key
            res = sorted(self.counter.items(), key=lambda x: x[1])[0][0]
            self.prev_min_key = res
            return res
