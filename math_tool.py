from AlgebraSolution.utils import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise Exception("zero canot be denominator")
        op = 1
        if numerator < 0:
            op = -op
            numerator = -numerator
        if denominator < 0:
            op = -op
            denominator = -denominator
        tmp_gcd = gcd(numerator, denominator)
        self.numerator = (numerator // tmp_gcd) * op
        self.denominator = denominator // tmp_gcd

    def __repr__(self):
        return "fraction:{0}/{1}".format(self.numerator, self.denominator)

    def __neg__(self):
        return Fraction((-1) * self.numerator, self.denominator)

    def reciprocal(self):
        return Fraction(self.denominator, self.numerator)

    def __add__(self, other):
        return Fraction(self.numerator * other.denominator +
                        self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        return self.__add__(-other)

    def __truediv__(self, other):
        return self.__mul__(other.reciprocal())