class vowels:
    def __init__(self, text: str):
        self.text = text
        self.vowels = ('a', 'e', 'i', 'o', 'u')
        self.result = []
        self.start = 0
        self.end = len(text)

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.end:
            result = self.text[self.start]
            self.start += 1
            if result.lower() in self.vowels:
                return result

        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
