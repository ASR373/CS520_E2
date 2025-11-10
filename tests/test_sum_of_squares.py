from src.sum_of_squares import sum_of_squares

def test_sum_of_squares():
    assert sum_of_squares([1,2,3]) == 14
    assert sum_of_squares([]) == 0
    assert sum_of_squares([-1,2,-3]) == 14
    assert sum_of_squares([10**3]) == 10**6
