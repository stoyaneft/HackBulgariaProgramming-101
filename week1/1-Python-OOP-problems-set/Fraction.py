class Fraction:

    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __add__(self, other):
        sum_numer = self.numer * other.denom + self.denom * other.numer
        sum_denom = self.denom * other.denom
        return Fraction(sum_numer, sum_denom)

    def __sub__(self, other):
        sub_numer = self.numer * other.denom - self.denom * other.numer
        sub_denom = self.denom * other.denom
        return Fraction(sub_numer, sub_denom)

    def __lt__(self, other):
        return self.numer / self.denom < other.numer / other.denom

    def __gt__(self, other):
        return self.numer / self.denom > other.numer / other.denom

    def __eq__(self, other):
        return self.numer / self.denom == other.numer / other.denom

print(Fraction(1, 2) == Fraction(3, 4))
