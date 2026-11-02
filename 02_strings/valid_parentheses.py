"""
VALID PARENTHESES (balanced brackets)
"{[()]}" -> True,   "{[(])}" -> False.

Approach : STACK. Push opening brackets; on a closing bracket the top must match. End: stack empty.
Time O(n), Space O(n).

Interview tips
  - Classic stack question. Mention edge cases: empty string, only closers, leftover openers.
"""


def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for c in s:
        if c in "([{":
            stack.append(c)
        elif c in pairs:
            if not stack or stack.pop() != pairs[c]:
                return False
    return not stack


def test():
    assert is_valid("") and is_valid("()") and is_valid("{[()]}") and is_valid("()[]{}")
    assert not is_valid("(") and not is_valid(")") and not is_valid("{[(])}") and not is_valid("(()")
    assert is_valid("a(b)c[d]")


if __name__ == "__main__":
    print(is_valid("{[()]}"), is_valid("{[(])}"))
    test()
    print("All tests passed")
