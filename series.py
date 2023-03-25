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
    
    

