class Calculator:
    @staticmethod
    def add(*nums):
        return sum(nums)

    @staticmethod
    def multiply(*nums):
        result = 1
        for num in nums:
            result *= num
        return result

    @staticmethod
    def divide(*nums):
        result = nums[0]
        for num in nums[1:]:
            result /= num
        return result

    @staticmethod
    def subtract(*nums):
        result = nums[0]
        for num in nums[1:]:
            result -= num
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
