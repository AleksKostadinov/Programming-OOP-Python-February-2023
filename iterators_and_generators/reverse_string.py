def reverse_text(text):
    for i in text[::-1]:
        yield i


for char in reverse_text("step"):
    print(char, end='')
