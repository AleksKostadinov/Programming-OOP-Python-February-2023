from functools import reduce


class Calculator:
    @staticmethod
    def add(*nums):
        result = reduce(lambda a, b: a + b, nums)
        return result

    @staticmethod
    def multiply(*nums):
        result = reduce(lambda a, b: a * b, nums)
        return result

    @staticmethod
    def divide(*nums):
        result = reduce(lambda a, b: a / b, nums)  # a + b if a == 0 or b == 0 else a / b
        return result

    @staticmethod
    def subtract(*nums):
        result = reduce(lambda a, b: a - b, nums)
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
