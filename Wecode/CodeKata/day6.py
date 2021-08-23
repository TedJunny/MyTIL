def roman_to_num(s):
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }
    answer = 0
    loop_num = len(s) - 1

    i = 0
    while i <= loop_num:
        if i < loop_num and s[i] + s[i + 1] in roman_dict:
            answer += roman_dict[s[i] + s[i + 1]]
            i += 2
            continue

        answer += roman_dict[s[i]]
        i += 1

    return answer


print(roman_to_num("IIII"))
