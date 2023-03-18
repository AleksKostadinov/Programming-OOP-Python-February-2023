class Rhombus:
    def __init__(self, number: int):
        self.number = number

    def call_rhombus(self):
        for start_count in range(1, self.number):
            self.print_rhombus(start_count)

        for start_count in range(self.number, 0, -1):
            self.print_rhombus(start_count)

    def print_rhombus(self, start_count: int):
        for row in range(self.number - start_count):
            print(' ', end='')
        for row in range(1, start_count):
            print('*', end=' ')
        print('*')


result = Rhombus(int(input()))
result.call_rhombus()

