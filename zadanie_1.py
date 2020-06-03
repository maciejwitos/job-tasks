def get_postcodes_from_range(user_post_code_1, user_post_code_2):

    user_post_code_1 = int(user_post_code_1.replace('-', ''))
    user_post_code_2 = int(user_post_code_2.replace('-', ''))

    difference = user_post_code_2 - user_post_code_1

    results = []

    if difference < 0:
        while user_post_code_2 != user_post_code_1:
            user_post_code_2 += 1
            result = list(str(user_post_code_2))
            result.insert(2, '-')
            results.append("".join(result))

    else:
        while user_post_code_1 != user_post_code_2:
            user_post_code_1 += 1
            result = list(str(user_post_code_1))
            result.insert(2, '-')
            results.append("".join(result))
            results.append("".join(result))

    return results