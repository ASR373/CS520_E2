from src.flatten import flatten

def test_flatten():
    assert flatten([1, [2, 3], 4]) == [1,2,3,4]
    assert flatten([[[]]]) == []
    assert flatten([1,[2,[3,[4]]]]) == [1,2,3,4]
    assert flatten([]) == []
    assert flatten(["a", ["b", ["c"]]]) == ["a","b","c"]
