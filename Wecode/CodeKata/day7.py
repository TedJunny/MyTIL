from collections import Counter


def more_than_half(nums):
    return Counter(nums).most_common(1)[0][0]


# def more_than_half(nums):
#     # 아래 코드를 입력해주세요.
#     result = []
#     for a in nums:
#         if nums.count(a) >= len(nums) / 2:
#             if a not in result:
#                 result.append(a)
#     return result[0]
