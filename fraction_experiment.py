cross_reduce = """                while True:
                    gcd_of_self_denominator_and_other_fraction_numerator = math.gcd(self.denominator,
                                                                                    other_fraction.numerator)
                    if gcd_of_self_denominator_and_other_fraction_numerator == 1:
                        break
                    other_fraction.numerator = other_fraction.numerator / gcd_of_self_denominator_and_other_fraction_numerator
                    self.denominator = self.denominator / gcd_of_self_denominator_and_other_fraction_numerator"""

substring = ""
substring_lengths_for_self = []
substring_lengths_for_other_fraction = []

for character in cross_reduce:
    substring += character
    if substring.endswith("self"):
        substring_lengths_for_self.append(len(substring))
    if substring.endswith("other_fraction"):
        substring_lengths_for_other_fraction.append(len(substring))

for substring_length_for_other_fraction in substring_lengths_for_other_fraction:
    cross_reduce = cross_reduce[:substring_length_for_other_fraction - 14] + "self" + cross_reduce[substring_length_for_other_fraction:]

print(cross_reduce)
