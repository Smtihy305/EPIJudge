from typing import List

from test_framework import generic_test


def h_index(citations: List[int]) -> int:
    # Good Version
    citations.sort()
    n = len(citations)
    for i, c in enumerate(citations):
        if c >= n-i:
            return n-i
    return 0

    """
    # Bad Version
    result = 0
    for i in range(0, len(citations) + 1):
        count = 0
        for j in citations:
            if i <= j:
                count += 1
        if count >= i:
            if i > result:
                result = i
    return result
    """


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
