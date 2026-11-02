"""
LONGEST COMMON PREFIX
["flower","flow","flight"] -> "fl".

Approaches
  1. Shrink prefix until every word starts with it  -> O(total chars)
  2. Vertical scan (column by column)
  3. min/max trick: compare only smallest and largest word alphabetically
"""


def longest_common_prefix(words):
    if not words:
        return ""
    prefix = words[0]
    for w in words[1:]:
        while not w.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


def longest_common_prefix_minmax(words):
    if not words:
        return ""
    lo, hi = min(words), max(words)
    i = 0
    while i < len(lo) and lo[i] == hi[i]:
        i += 1
    return lo[:i]


def test():
    for f in (longest_common_prefix, longest_common_prefix_minmax):
        assert f(["flower", "flow", "flight"]) == "fl"
        assert f(["dog", "car"]) == "" and f([]) == "" and f(["alone"]) == "alone"


if __name__ == "__main__":
    print(longest_common_prefix(["flower", "flow", "flight"]))
    test()
    print("All tests passed")
