def callLimit(limit: int):
    """python decorator that limits the calling \
            of a function, takes number of call \
            limits you wants as argument"""
    count = 0

    def callLimiter(func):

        def limit_function(*args: any, **kwargs: any):
            nonlocal count
            if count < limit:
                count += 1
                return func(*args, **kwargs)
            else:
                print(f"Error: {func} call too many times")
        return limit_function
    return callLimiter
