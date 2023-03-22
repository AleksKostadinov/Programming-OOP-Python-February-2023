def vowel_filter(function):
    def wrapper():
        letters = function()

        vowels = ['a', 'e', 'o', 'i', 'u']
        filtered_letters = [x for x in vowels if x in letters]

        return filtered_letters

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
