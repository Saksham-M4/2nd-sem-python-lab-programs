def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])

print(f"Sum of [1, 2, 3, 4, 5]: {list_sum([1, 2, 3, 4, 5])}")