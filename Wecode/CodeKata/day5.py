def get_prefix(strs):
    if strs == []:
        return ""

    strs = sorted(strs, key=len)
    answer = ""

    for i in range(len(strs[0])):
        for j in range(len(strs) - 1):
            if strs[0][i] != strs[j + 1][i]:
                return answer

        answer += strs[0][i]

    return answer
