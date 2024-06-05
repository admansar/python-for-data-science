def ft_statistics(*args: any, **kwargs: any) -> None:
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
