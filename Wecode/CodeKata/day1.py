def two_sum(nums, target):
    my_dict = {}

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            my_dict[nums[i] + nums[j]] = [i, j]

    return my_dict[target]
