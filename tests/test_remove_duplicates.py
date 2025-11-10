from src.remove_duplicates import remove_duplicates

def test_remove_duplicates():
    assert remove_duplicates([1,1,2,2,3,1]) == [1,2,3]
    assert remove_duplicates([]) == []
    assert remove_duplicates(["a","a","b","A"]) == ["a","b","A"]
