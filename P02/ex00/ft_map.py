from typing import Iterator


def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
        Args:
            function_to_apply: a function taking an iterable.
            iterable: an iterable object (list, tuple, iterator).
        Returns:
            An iterable.
            None if the iterable can not be used by the function.
    """
    try:
        for it in iterable:
            yield function_to_apply(it)
    except TypeError:
        raise ValueError("Error Map : Cannot Apply that function to that type")      