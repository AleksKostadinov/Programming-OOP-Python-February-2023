class dictionary_iter:
    def __init__(self, dict_obj: dict):
        self.iter = list(dict_obj.items())
        self.iterations = len(dict_obj)
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.iterations:
            raise StopIteration
        results = self.iter[self.start]

        self.start += 1

        return results


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
