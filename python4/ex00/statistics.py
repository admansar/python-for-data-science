def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Calculates basic descriptive statistics for a list of numbers and prints
    them based on keyword arguments.

    Args:
        *args (any): Variable-length arguments representing a list of numbers.
        **kwargs (any): Keyword arguments specifying which statistics to print.
            Valid keywords include:
                - 'mean': Calculate and print the mean.
                - 'median': Calculate and print the median.
                - 'quartile': Calculate and print the 1st and 3rd quartiles.
                - 'var': Calculate and print the variance.
                - 'std': Calculate and print the standard deviation.

    Returns:
        None
    """
    try:
        arr = sorted([el for el in args])
        wargs = [el for el in kwargs.items()]
        num = len(arr)
        if num != 0:
            mean = sum(i for i in arr) / num
            pos1 = int(num / 2)
            q1 = int(num / 4)
            q3 = int(3 * num / 4)
            median = arr[pos1] if num % 2 else (arr[pos1 - 1] + arr[pos1]) / 2
            quartile = [float(arr[q1]), float(arr[q3])]
            var = sum((x - mean) ** 2 for x in arr) / num
            std = var ** 0.5  # power 1/2
            dict = {
                    'mean': mean,
                    'median': median,
                    'quartile': quartile,
                    'std': std,
                    'var': var
                    }
            for tuple in wargs:
                for key, value in dict.items():
                    if key == tuple[1]:
                        print(f"{key} : {value}")
        else:
            for _ in wargs:
                print("ERROR")
    except Exception as e:
        print(f"Error: {e}")
