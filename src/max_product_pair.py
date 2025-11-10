from typing import Iterable, Tuple

def max_product_pair(nums: Iterable[int]) -> Tuple[int, int]:
    arr = list(nums)
    if len(arr) < 2:
        raise ValueError("need at least two numbers")

    max1 = max2 = float("-inf")
    min1 = min2 = float("inf")

    for x in arr:
        if x > max1:
            max1, max2 = x, max1
        elif x > max2:
            max2 = x

        if x < min1:
            min1, min2 = x, min1
        elif x < min2:
            min2 = x

    cand1 = (max2, max1)
    cand2 = (min1, min2)

    prod1 = cand1[0] * cand1[1]
    prod2 = cand2[0] * cand2[1]

    # Initial best based on product
    best = cand1 if prod1 >= prod2 else cand2

    # Tie-breaker: prefer pair with non-negative elements
    if prod1 == prod2:
        if min(cand1) >= 0:     # cand1 all >= 0
            best = cand1
        elif min(cand2) >= 0:  # cand2 all >= 0
            best = cand2

    return tuple(sorted(best))
