import pytest
from src.max_product_pair import max_product_pair

def test_max_product_pair():
    assert max_product_pair([1,2,3]) == (2,3)
    assert max_product_pair([-10,-3,1,2]) == (-10,-3)
    assert max_product_pair([0, 100, -1, -2]) == (-2,-1)
    assert max_product_pair([5,5,2]) == (5,5)

def test_max_product_pair_short_list():
    with pytest.raises(ValueError):
        max_product_pair([1])

# Additional max_product_pair tests
import pytest
from src.max_product_pair import max_product_pair

def test_max_product_pair_all_negatives():
    assert max_product_pair([-1, -2, -3]) == (-3, -2)

def test_max_product_pair_all_zeros():
    assert max_product_pair([0, 0, 0]) == (0, 0)

def test_max_product_pair_tuple_input():
    assert max_product_pair((4, 7, 1, 3)) == (4, 7)

def test_max_product_pair_largest_positives_win():
    assert max_product_pair([100, 99, -100, -1]) == (99, 100)

def test_max_product_pair_equal_pairs():
    assert max_product_pair([2, 2, 2]) == (2, 2)

def test_max_product_pair_tie_prefers_positive_pair():
    # Tie: (2*2) == (-2*-2) == 4 — correct behavior prefers the positive pair
    from src.max_product_pair import max_product_pair
    assert max_product_pair([2, 2, -2, -2]) == (2, 2)

def test_max_product_pair_tie_prefers_positive_pair_large():
    # Another tie: (5*5) == (-5*-5) == 25
    from src.max_product_pair import max_product_pair
    assert max_product_pair([5, 5, -5, -5]) == (5, 5)

