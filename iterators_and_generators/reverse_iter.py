class reverse_iter:
    def __init__(self, list_numbers: list):
        self.list_numbers = list_numbers

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.list_numbers.pop()
        except IndexError:
            raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
