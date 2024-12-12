from math import gcd

class Rational:
    def __init__(self, numerator : int, denumerator : int):
        if numerator < 0:
            raise ValueError('numerator는 1보다 큰 수여야 합니다.')
        elif denumerator <= 0:
            raise ValueError('denumerator는 0보다 큰 수여야 합니다.')
        
        divider = gcd(numerator, denumerator)
        if divider != 1:
            numerator //= divider
            denumerator //= divider
        
        self.numerator = numerator
        self.denumerator = denumerator
    
    def __add__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("피연산자가 Rational 객체가 아닙니다.")
        
        new_numerator = (self.numerator * other.denumerator) + (other.numerator * self.denumerator)
        new_denumerator = self.denumerator * other.denumerator

        return Rational(new_numerator, new_denumerator)
    
    def __eq__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("피연산자가 Rational 객체가 아닙니다.")
        
        return (self.numerator == other.numerator) and (self.denumerator == other.denumerator)
    
    def __repr__(self):
        return f"Rational({self.numerator} / {self.denumerator})"