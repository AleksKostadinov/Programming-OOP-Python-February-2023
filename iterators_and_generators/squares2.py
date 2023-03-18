def squares(parameter: int):
    num = 1
    while num <= parameter:
        yield num ** 2
        num += 1


print(list(squares(5)))
