# -- PROBLEM --
# John is preparing for an algorithms exam and, just in case, is writing cheat sheets.
# To fit as much information as possible, he omits spaces between words, resulting in one very long string.
# To avoid getting confused while reading it during the exam—especially when feeling nervous —
# he asks you to write a program that, given this long string and a set of allowed words,
# determines whether the text can be broken down into individual words from that set.

# More formally: given a text T and a set of strings s₁, ..., sₙ.
# Determine whether T can be represented as sₖ₁ sₖ₂ ... sₖᵣ,
# where kᵢ are indices of the strings. Indices may repeat.
# Any string sᵢ can appear any number of times in the decomposition of T.
# It is not required to use every string from the set, and the strings may appear in any order.

# -- INPUT FORMAT --
# The first line contains a text T that needs to be split into words.
# The length of T does not exceed 100100. The text consists of lowercase English letters.
# The second line contains the number of allowed words, 1 ≤ n ≤ 100.
# The following n lines contain the words themselves, consisting of lowercase Latin letters. The length of each word does not exceed 100.

# -- OUTPUT FORMAT --
# Output "YES" if the text can be broken down into words from the given dictionary, or "NO" otherwise.

# -- Example 1 --
# INPUT:
# examiwillpasstheexam
# 5
# will
# pass
# the
# exam
# i
# OUTPUT:
# YES

# -- Example 2 --
# INPUT:
# abacaba
# 2
# abac
# caba
# OUTPUT:
# NO

# -- SOLUTION OPERATING PRINCIPLE --
# We create a dictionary containing empty arrays—one for each letter of the alphabet—and place words into the corresponding array based on their starting letter. Then, as we iterate through each character of the text, we check for the presence of elements from the dictionary.

# -- SOLUTION TIME COMPLEXITY --
# In the worst case, the time complexity is O(n^2), where n is the length of the string.

# -- SOLUTION SPACE COMPLEXITY --
# It requires O(n) additional memory, where n is the length of the string.

def is_splitable(text, words):
    parts = [[] for _ in range(26)]

    for part in set(words):
        key = ord(part[0]) - ord('a')
        parts[key].append(part)

    l = len(text)
    res = [0] * (l + 1)
    res[0] = 1

    for i in range(l):
        if not res[i]:
            continue

        key = ord(text[i]) - ord('a')
        for part in parts[key]:
            if text.startswith(part, i):
                res[i + len(part)] = 1

    return bool(res[l])


if __name__ == '__main__':
    text = input()