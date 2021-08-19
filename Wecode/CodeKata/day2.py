def reverse(number):
    str_num = str(abs(number))
    if number > 0:
        return int(str_num[::-1])
    else:
        return -int(str_num[::-1])
