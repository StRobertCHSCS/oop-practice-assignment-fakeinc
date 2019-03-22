# import # logging
import math

# # logging.basicConfig(format="%(levelname) -10s %(module)s:%(lineno)s %(funcName)s %(message)s",
#                     level=# logging.DEBUG)


# Define your Fraction class here
class Fraction:
    # declare special methods
    def __init__(self, numerator: int, denominator: int):
        # set
        self.numerator = numerator
        self.denominator = denominator
        # logging.debug("{0}/{1}".format(self.numerator, self.denominator))

        # check
        self.check_if_the_denominator_is_valid()

    def __str__(self):
        return "{0}/{1}".format(self.numerator, self.denominator)

    # declare getters
    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    # declare setters
    def set_numerator(self, new_numerator: int):
        self.numerator = new_numerator
        # logging.debug("{0}/{1}".format(self.numerator, self.denominator))

    def set_denominator(self, new_denominator: int):
        self.denominator = new_denominator
        # logging.debug("{0}/{1}".format(self.numerator, self.denominator))
        self.check_if_the_denominator_is_valid()
        # logging.info("{0}/{1}".format(self.numerator, self.denominator))

    # declare adding and subtracting methods
    def add(self, other_fraction):
        # reduce the fractions to lowest terms
        self.__reduce()
        other_fraction.__reduce()

        # get the greatest common factor of the denominators
        gcd_of_denominators = math.gcd(self.denominator, other_fraction.denominator)
        # logging.info(gcd_of_denominators)

        # get the number each numerator should multiply
        multiplier_for_other_fraction = self.denominator // gcd_of_denominators
        multiplier_for_self = other_fraction.denominator // gcd_of_denominators
        # logging.info(str(multiplier_for_self) + ", " + str(multiplier_for_other_fraction))

        # update result denominator to the lowest common multiple
        self.denominator = multiplier_for_self * self.denominator

        # update result numerator to the sum of two multiplied numerators
        self.numerator = multiplier_for_self * self.numerator + multiplier_for_other_fraction * other_fraction.numerator

        # logging.info(str(self))

        # reduce the fraction to lowest terms
        self.__reduce()
        self.check_if_the_fraction_is_zero()

    def subtract(self, other_fraction):
        # reduce the fractions to lowest terms
        self.__reduce()
        other_fraction.__reduce()

        # get the greatest common factor of the denominators
        gcd_of_denominators = math.gcd(self.denominator, other_fraction.denominator)
        # logging.info(gcd_of_denominators)

        # get the number each numerator should multiply
        multiplier_for_other_fraction = self.denominator // gcd_of_denominators
        multiplier_for_self = other_fraction.denominator // gcd_of_denominators
        # logging.info(str(multiplier_for_self) + ", " + str(multiplier_for_other_fraction))

        # update result denominator to the lowest common multiple
        self.denominator = multiplier_for_self * self.denominator

        # update result numerator to the sum of two multiplied numerators
        self.numerator = multiplier_for_self * self.numerator - multiplier_for_other_fraction * other_fraction.numerator

        # logging.info(str(self))

        # reduce the fraction to lowest terms
        self.__reduce()

    def multiply(self, other_fraction):
        # reduce self to lowest terms
        self.__reduce()
        if self.numerator != 0:
            # reduce other_fraction to lowest terms
            other_fraction.__reduce()

            # cross __reduce()
            if other_fraction.numerator != 0:
                # self denominator and other fraction numerator
                while True:
                    gcd_of_self_denominator_and_other_fraction_numerator = math.gcd(self.denominator,
                                                                                    other_fraction.numerator)
                    if gcd_of_self_denominator_and_other_fraction_numerator == 1:
                        break
                    other_fraction.numerator = other_fraction.numerator // gcd_of_self_denominator_and_other_fraction_numerator
                    self.denominator = self.denominator // gcd_of_self_denominator_and_other_fraction_numerator
                    # logging.info("{0}/{1}".format(self.numerator, self.denominator))

                # self denominator and other fraction numerator
                while True:
                    gcd_of_other_fraction_denominator_and_self_numerator = math.gcd(other_fraction.denominator,
                                                                                    self.numerator)
                    if gcd_of_other_fraction_denominator_and_self_numerator == 1:
                        break
                    self.numerator = self.numerator // gcd_of_other_fraction_denominator_and_self_numerator
                    # logging.info("{0}/{1}".format(self.numerator, self.denominator))
                    other_fraction.denominator = other_fraction.denominator // gcd_of_other_fraction_denominator_and_self_numerator

            # multiply the left
            self.numerator = self.numerator * other_fraction.numerator
            self.denominator = self.denominator * other_fraction.denominator
            # logging.info("{0}/{1}".format(self.numerator, self.denominator))

    # declare misc useful functions
    def check_if_the_fraction_is_zero(self):
        if self.numerator == 0:
            self.denominator = 1

    def check_if_the_denominator_is_valid(self):
        if self.denominator == 0:
            raise ValueError

    def __reduce(self):
        if self.numerator != 0:
            while True:
                gcd_of_denominator_and_numerator = math.gcd(self.denominator, self.numerator)
                # logging.info(gcd_of_denominator_and_numerator)
                if gcd_of_denominator_and_numerator == 1:
                    break
                self.numerator = self.numerator // gcd_of_denominator_and_numerator
                self.denominator = self.denominator // gcd_of_denominator_and_numerator
                # logging.info("{0}/{1}".format(self.numerator, self.denominator))
        else:
            self.denominator = 1


if __name__ == '__main__':
    # put your code that utilizes your Fraction class here
    pass
