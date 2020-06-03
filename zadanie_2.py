def get_missing_element_from_range_1_to_n(n, random_list, *args, **kwargs):

    compare_list = []

    for i in range(1, n + 1):
        compare_list.append(i)

    return list(set(compare_list) - set(random_list))