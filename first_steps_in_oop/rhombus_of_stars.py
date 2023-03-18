def logic_func(number_, i):
    for col in range(number_ - i):
        print(' ', end='')
    for col in range(1, i):
        print('*', end=' ')
    print('*')

def start_func(number_):
    for i in range(1, number_):
        logic_func(number_, i)


def revert_func(number_):
    for i in range(number_, 0, -1):
        logic_func(number_, i)


number = int(input())

start_func(number)
revert_func(number)
