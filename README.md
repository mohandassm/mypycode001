# Interview Prep: Math & Logic Problems (Python 3.8+)

One file per concept. Every file has: meaning, approaches with complexity,
interview tips, solution code, a `test()` with asserts, and a demo.

## Run
    python run_all.py                       # run all tests
    python 01_basic_math/prime_number.py    # run one topic (demo + tests)

## Topics
### 01_basic_math
factor, prime_number, fibonacci, factorial, armstrong_number, perfect_number,
gcd_lcm, fizzbuzz, reverse_number, strong_number, power_of_two, leap_year,
decimal_to_binary, pascal_triangle

### 02_strings
palindrome, anagram, substring, reverse_string, vowels_count, char_frequency,
first_non_repeating_char, valid_parentheses, longest_common_prefix,
longest_palindromic_substring

### 03_arrays_matrix
matrix_transpose, matrix_rotate, linear_search, binary_search, two_sum,
max_subarray (Kadane), missing_number, second_largest, remove_duplicates,
rotate_array, merge_sorted_arrays

### 04_sorting
bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

## Interview cheat sheet
| Pattern | Use it for | Examples here |
|---|---|---|
| Loop to sqrt(n) | divisor problems | factor, prime, perfect |
| Hash map / Counter | counting, lookup in O(1) | two_sum, anagram, char_frequency |
| Two pointers | sorted arrays, palindromes | palindrome, two_sum_sorted, merge_sorted |
| Stack | matching / nesting | valid_parentheses |
| Dynamic programming | overlapping subproblems | fibonacci memo, Kadane |
| Divide and conquer | O(n log n) | merge_sort, quick_sort, binary_search |
| Bit tricks | O(1) checks | power_of_two, missing_number XOR |

## Big-O quick table
| Algorithm | Best | Average | Worst | Space |
|---|---|---|---|---|
| Linear search | O(1) | O(n) | O(n) | O(1) |
| Binary search | O(1) | O(log n) | O(log n) | O(1) |
| Bubble / Selection / Insertion | O(n)* | O(n^2) | O(n^2) | O(1) |
| Merge sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick sort | O(n log n) | O(n log n) | O(n^2) | O(log n) |
*bubble with early exit and insertion on sorted data; selection is always O(n^2)

## How to answer in an interview
1. Repeat the problem and ask about edge cases (empty, negative, duplicates).
2. Start with the brute force, state its complexity.
3. Improve it, and explain why the better version is faster.
4. Code, then walk through a small example by hand.
5. State time and space complexity at the end.
