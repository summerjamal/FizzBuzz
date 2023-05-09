def fizzbuzz(number):
    output_string3 = "fizz"
    output_string5 = "buzz"
    output_string_15 = output_string3 + output_string5
    if number % 15 == 0:
        return output_string_15
    elif number % 3 == 0:
        return output_string3
    elif number % 5 == 0:
        return output_string5
    else:
        return number

