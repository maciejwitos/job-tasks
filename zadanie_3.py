from decimal import Decimal


def numbers_generator():

    number = 2

    while number != 5.5:
        number += 0.5
        yield Decimal(number)
