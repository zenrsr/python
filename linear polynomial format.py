def read_polynomial():
    n = int(input())
    polynomial_dict = {}
    for i in range(n):
        power,coefficient = list(map(int,input().split()))
        polynomial_dict[power] = coefficient
    return polynomial_dict

def get_term(coefficient, power):
    coefficient = abs(coefficient)
    global term
    if coefficient == 1 and power != 0:
        term = ""
    elif coefficient == 0 and power == 0:
        term = ""
    elif coefficient !=0 and power ==0:
        term = "{}".format(coefficient)
    elif power == 1:
        term = "{}x".format(coefficient,power)
    else:
        term = "{}x^{}".format(coefficient,power)
    return term


def get_polynomial_equation(polynomial):
    result = ""
    coefficient_values = polynomial.values()
    power_values = polynomial.keys()
    degree_of_polynomial = max(sorted(power_values))
    for i in sorted(power_values, reverse=True):
        coefficient = polynomial[i]
        value = get_term(coefficient,i)
        if i == degree_of_polynomial:
            if coefficient < 0:
                result = "-{}".format(value)
            elif coefficient > 0:
                result = "{}".format(value)
        else:
            if coefficient < 0:
                result = "{} - {}".format(result,value)
            elif coefficient > 0:
                result = "{} + {}".format(result,value)
    if result == "":
        result = 0
    return result



def main():
    polynomial = read_polynomial()
    print(get_polynomial_equation(polynomial))

main()