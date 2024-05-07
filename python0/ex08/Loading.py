# import os


def ft_tqdm(lst: range) -> None:
    """
       ft_tqdm (lst: range) -> None:
    this function its for decoration while leting
    your code doing some job, its also good for progress
    """
    total_len = len(lst)
    completed = 0
    last_percent = 0
    # since we dont have the rigth to use terminal
    # length, we will do it manually
    ter_len = 80 - 40
    # change the first number with
    # os.get_terminal_size().columns after importing os
    for item in lst:
        completed += 1
        percent = int((completed / total_len) * 100)
        percent_rat = int(percent * (ter_len / 100))
        if percent != last_percent:
            progress_bar = "█" * percent_rat + " " * (ter_len - percent_rat)
            out = str(percent) + "%" + str(progress_bar)
            print(f"{out}| {completed}/{total_len}", end="\r")
        last_percent = percent
        yield item
