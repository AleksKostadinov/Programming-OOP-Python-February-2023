def print_func(size, start_counts):
    for row in range(size - start_counts):
        print(' ', end='')
    for row in range(1, start_counts):
        print('*', end=' ')
    print('*')


number = int(input())

for start_count in range(1, number):
    print_func(number, start_count)

for start_count in range(number, 0, -1):
    print_func(number, start_count)
