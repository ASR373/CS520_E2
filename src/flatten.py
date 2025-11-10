from typing import Any, List

def flatten(xs: Any) -> List[Any]:
    """
    Flatten arbitrarily nested lists.
    Non-list items (including strings) are treated as atomic.
    Examples:
      [1, [2, 3], 4]        -> [1, 2, 3, 4]
      [[[]]]                -> []
      ["a", ["b", ["c"]]]   -> ["a", "b", "c"]
    """
    out: List[Any] = []

    def _walk(item):
        if isinstance(item, list):
            for sub in item:
                _walk(sub)
        else:
            out.append(item)

    _walk(xs)
    return out
