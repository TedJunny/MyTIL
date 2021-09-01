def complex_number_multiply(a, b):
    split_a = a.split("+")
    split_b = b.split("+")
    split_a[1] = split_a[1].replace("i", "")
    split_b[1] = split_b[1].replace("i", "")

    if split_a[1] == "-":
        split_a[1] = "-1"

    if split_b[1] == "-":
        split_b[1] = "-1"

    result = complex(int(split_a[0]), int(split_a[1])) * complex(
        (int(split_b[0])), int(split_b[1])
    )
    real = result.real
    imag = result.imag
    return str(int(real)) + "+" + str(int(imag)) + "i"


print(complex_number_multiply("3+-i", "99+99i"))
