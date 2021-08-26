def is_valid(string):
    stacker = []

    for s in string:
        if s not in stacker:
            if s == "(":
                stacker.append(")")
            elif s == "[":
                stacker.append("]")
            elif s == "{":
                stacker.append("}")
            else:
                return False
        elif s == stacker[-1]:
            stacker.pop()

    return stacker == []


# print(is_valid("([)"))
# print(is_valid("}}"))
