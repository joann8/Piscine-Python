def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
        Args:
            function_to_apply: a function taking an iterable.
            iterable: an iterable object (list, tuple, iterator).
        Returns:
            A value, of same type of elements in the iterable parameter.
            None if the iterable can not be used by the function.
    """
    try:
        obj = next(iter(iterable))
        for i in range(1, len(iterable)):
            obj = function_to_apply(obj, iterable[i])
        return(obj)
    except TypeError:
        raise ValueError("Error Filter: Cannot Apply that function to that type")