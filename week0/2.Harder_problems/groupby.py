def groupby(func, seq):
    grouped_dict = {}
    for item in seq:
        key = func(item)
        if key not in grouped_dict:
            grouped_dict[key] = [item]
        else:
            grouped_dict[key].append(item)
    return grouped_dict
