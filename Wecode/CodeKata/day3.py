def get_len_of_str(str):
    my_list = []
    length = 0

    for i in range(len(str) - 1):
        if str[i] != str[i + 1]:
            if str[i] not in my_list:
                my_list.append(str[i])
                if i == len(str) - 2 and str[i + 1] not in my_list:
                    my_list.append(str[i + 1])
                print(f"my_list: {my_list}")
        elif str[i] == str[i + 1] and len(my_list) > length:
            length = len(my_list)
            my_list.clear()

    if len(my_list) > length:
        length = len(my_list)

    if length == 0:
        return len(set(str))

    return length


def get_len_of_str2(string):
    str_list = []
    max_length = 0

    for i in string:
        if i in str_list:
            str_list = str_list[str_list.index(i) + 1 :]

        str_list.append(i)
        print(str_list)
        max_length = max(max_length, len(str_list))

    return max_length


# print(get_len_of_str2("asdasdff"))
print(get_len_of_str2("aaabcaaaabcdeaaa"))
# print(get_len_of_str2("aaaa"))
