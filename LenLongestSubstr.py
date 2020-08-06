#!/usr/bin/env python

"""
    Alex Gavin, Winter 2020

    Longest Substring length without repeating characters
    solution in LeetCode class format.
"""


class Solution:

    def length_longest_substring(self, string):
        """
            Time:  O(n), Space: O(k)
            [k = length of the longest substring w/o repeating characters]
        """
        longest = 0
        left, right = 0, 0
        chars = set()

        while left < len(string) and right < len(string):
            if string[right] not in chars:
                chars.add(string[right])
                right += 1
                longest = max(longest, right - left)
            else:
                chars.remove(string[left])
                left += 1

        return longest


sol = Solution()

while True:
    input_str = input("String to consider: ")

    substr_len = sol.length_longest_substring(input_str)

    print(f"Longest substring length of \"{input_str}\" is {substr_len}.")
