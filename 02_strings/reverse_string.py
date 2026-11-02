"""
REVERSE A STRING / WORDS
Approaches : slicing s[::-1], two pointers on a list, stack, recursion.

Interview tips
  - Python strings are immutable - convert to list to swap in place.
  - Variants: reverse each word, reverse word order, reverse only letters.
"""


def reverse_slice(s):
    return s[::-1]


def reverse_two_pointer(s):
    chars = list(s)
    i, j = 0, len(chars) - 1
    while i < j:
        chars[i], chars[j] = chars[j], chars[i]
        i, j = i + 1, j - 1
    return "".join(chars)


def reverse_recursive(s):
    return s if len(s) <= 1 else reverse_recursive(s[1:]) + s[0]


def reverse_words_order(sentence):
    return " ".join(sentence.split()[::-1])


def reverse_each_word(sentence):
    return " ".join(w[::-1] for w in sentence.split(" "))


def test():
    for s in ["", "a", "abc", "hello world"]:
        assert reverse_slice(s) == reverse_two_pointer(s) == reverse_recursive(s) == s[::-1]
    assert reverse_words_order("the sky is blue") == "blue is sky the"
    assert reverse_each_word("hello world") == "olleh dlrow"


if __name__ == "__main__":
    print(reverse_slice("hello"), "|", reverse_words_order("the sky is blue"))
    test()
    print("All tests passed")
