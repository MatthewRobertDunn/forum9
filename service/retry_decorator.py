import functools
def retry(times, exceptions):
    """
    Retry Decorator
    Retries the wrapped function/method up to `times` total attempts
    if the exceptions listed in ``exceptions`` are thrown.

    :param times: Total number of attempts (including the first).
    :type times: int
    :param exceptions: Tuple of exception types to trigger a retry.
    :type exceptions: tuple[Exception]
    """
    def decorator(func):
        @functools.wraps(func)
        def newfn(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt < times - 1:
                        print(
                            f"Exception in {func.__name__}, attempt "
                            f"{attempt + 1} of {times}: {e}"
                        )
                    else:
                        raise
        return newfn
    return decorator