def count_letters(word):
    vowel_count = 0
    consonant_count = 0
    upper_count = 0
    lower_count = 0
    vowels = ('a', 'e', 'i', 'o', 'u')

    for letter in word:
        if letter.isupper():
            upper_count += 1
        if letter.islower():
            lower_count += 1

    word = word.lower()

    for letter in word:
        if letter.isalpha():
            if letter in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count, upper_count, lower_count


def test_count_letters():
    assert count_letters("Hello") == (2, 3, 1, 4)
    assert count_letters("hElLo") == (2, 3, 2, 3)
    assert count_letters("HELLO") == (2, 3, 5, 0)
    assert count_letters("12345") == (0, 0, 0, 0)


test_count_letters()
