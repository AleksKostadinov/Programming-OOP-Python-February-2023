def squares(parameter: int):
    for num in range(1, parameter + 1):
        yield num * num


print(list(squares(5)))
