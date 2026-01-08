# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""

    for i in range(n):
        for j in range(n):
            if i in range(1, n-1) and j in range(1, n-1):
                result += " "
            else:
                result += "*"
        result += "\n"

    return result.rstrip()


# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""

    for i in range(n):
        for j in range(i+1):
            result += f"{j+1}"
        result += "\n"

    return result.rstrip()



# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):

    sum = 0
    for i in range(1, n + 1):
        sum += i
    return(sum)



# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""

    for i in range(n):
        for j in range(n - i - 1):
            result += " "
        for k in range(2 * i + 1):
            result += "*"
        result += "\n"

    return result.rstrip()

