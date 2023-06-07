def fibonacci(n):
    """
    Compute the nth value in the Fibonacci series using iteration.

    Args:
        n (int): the index of the desired value in the Fibonacci series

    Returns:
        int: the nth value in the Fibonacci series
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        prev_prev = 0
        prev = 1
        current = 1
        for i in range(2, n+1):
            current = prev + prev_prev
            prev_prev = prev
            prev = current
        return current
    


def lucas_recursive(n):
    """
    Compute the nth value in the Lucas series recursively.

    Args:
        n (int): the index of the desired value in the Lucas series

    Returns:
        int: the nth value in the Lucas series
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas_recursive(n-1) + lucas_recursive(n-2)
    
    def sum_series(n, first=0, second=1):
    """
    Generate a series of numbers based on the provided parameters.

    Args:
        n (int): The index of the number to generate in the series.
        first (int, optional): The first number in the series. Defaults to 0.
        second (int, optional): The second number in the series. Defaults to 1.

    Returns:
        int: The nth number in the series.
    """
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n-1, first, second) + sum_series(n-2, first, second)

    
    

