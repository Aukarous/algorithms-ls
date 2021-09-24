"""
Given a string array words, return an array of all characters that show up in all strings within the words
(including duplicates). You may return the answer in any order.
Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""
from collections import Counter


def commonchars(A):
    counts = Counter(A[0])
    for w in A[1:]:
        w_count = Counter(w)
        for c in counts:
            counts[c] = min(counts[c], w_count[c])

    result = []
    for ch, cnt in counts.items():
        result += [ch] * cnt

    return result


words = ["bella", "label", "roller"]
print(commonchars(A=words))
