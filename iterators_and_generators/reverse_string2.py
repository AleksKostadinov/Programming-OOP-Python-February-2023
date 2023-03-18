def reverse_text(word):
    for character in reversed(word):
        yield character


for char in reverse_text("step"):
    print(char, end='')
