def read_polynomial():
    n = int(input())
    polynomial_dict = dict()
    for i in range(n):
        power, coefficient = list(map(int, input().split()))
        polynomial_dict[power] = coefficient
    return polynomial_dict


def get_coefficient(power, polynomial):
    try:
        return polynomial[power]
    except KeyError:
        return 0


def add(a, b):
    result = dict()
    for power in (a.keys() | b.keys()):
        result[power] = get_coefficient(power, a) + get_coefficient(power, b)
    return result


def get_value(coefficient, power):
    coefficient = abs(coefficient)
    term = "none"
    if coefficient == 0:
        term = ""
    elif coefficient != 0 and power ==0:
        term = "{}".format(coefficient)
    elif coefficient != 0 and power == 1:
        term = "{}x".format(coefficient)
    elif coefficient == 1 and power != 0:
        term = "x^{}".format(power)
    else:
        term = "{}x^{}".format(coefficient,power)
    return term


def get_polynomial_equation(polynomial):
    print(polynomial)
    expression = ""
    degree = max(sorted(polynomial.keys()))
    for power in sorted(polynomial.keys(), reverse=True):
        coefficient = polynomial[power]
        result = get_value(coefficient, power)
        if power == degree:
            if coefficient < 0:
                expression = "-{}".format(result)
            elif coefficient > 0:
                expression = "{}".format(result)
            else:
                expression = "{}".format(expression)
        elif power != degree:
            if coefficient < 0:
                expression = "{} - {}".format(expression, result)
            elif coefficient > 0:
                expression = "{} + {}".format(expression, result)
            else:
                expression = "{}".format(expression)
    if expression == "":
        expression = 0
    return expression


def main():
    a = read_polynomial()
    b = read_polynomial()
    polynomial = add(a, b)
    print(get_polynomial_equation(polynomial))


main()