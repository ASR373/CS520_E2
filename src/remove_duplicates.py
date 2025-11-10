from typing import Iterable, List, TypeVar

T = TypeVar("T")

def remove_duplicates(items: Iterable[T]) -> List[T]:
    """
    Remove duplicates while preserving first occurrence order.
    Examples:
      [1,1,2,2,3,1]        -> [1,2,3]
      ["a","a","b","A"]    -> ["a","b","A"]  (case-sensitive)
    """
    seen = set()
    out: List[T] = []
    for x in items:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out
