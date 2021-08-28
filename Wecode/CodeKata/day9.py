from collections import Counter


def top_k(nums, k):
    # return [tup[0] for tup in Counter(nums).most_common(k)]
    answer = []
    most_common_tuple = Counter(nums).most_common(k)

    for tup in most_common_tuple:
        answer.append(tup[0])

    return answer


print(top_k([1, 1, 1, 2, 2, 3], 2))
