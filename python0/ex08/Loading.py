def ft_tqdm(lst: range):
  total_len = len(lst)
  completed = 0
  last_percent = 0
  for item in lst:
    completed += 1
    percent = int((completed / total_len) * 100)
    if percent != last_percent:
      progress_bar = "█" * int(percent * 0.5) + " " * (50 - int(percent * 0.5))
      print(f"{percent}%|{progress_bar}| {completed}/{total_len}", end="\r")
      last_percent = percent
    yield item
