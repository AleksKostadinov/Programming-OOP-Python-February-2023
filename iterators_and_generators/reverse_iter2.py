class reverse_iter:
    def __init__(self, list_of_numbers: list):
        self.list_of_numbers = list_of_numbers
        self.index_number = len(list_of_numbers)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index_number > 0:
            self.index_number -= 1
            return self.list_of_numbers[self.index_number]
        raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
