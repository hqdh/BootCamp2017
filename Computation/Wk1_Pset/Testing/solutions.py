import math
import itertools
# Problem 1 Write unit tests for addition().
# Be sure to install pytest-cov in order to see your code coverage change.


def addition(a, b):
    return a + b


def smallest_factor(n):
    """Finds the smallest prime factor of a number.
    Assume n is a positive integer.
    """
    if n == 1:
        return 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n


# Problem 2 Write unit tests for operator().
def operator(a, b, oper):
    if type(oper) != str:
        raise ValueError("Oper should be a string")
    if len(oper) != 1:
        raise ValueError("Oper should be one character")
    if oper == "+":
        return a + b
    if oper == "/":
        if b == 0:
            raise ValueError("You can't divide by zero!")
        return a/float(b)
    if oper == "-":
        return a-b
    if oper == "*":
        return a*b
    else:
        raise ValueError("Oper can only be: '+', '/', '-', or '*'")

# Problem 3 Write unit test for this class.
class ComplexNumber(object):
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def norm(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumber(real, imag)

    def __mul__(self, other):
        real = self.real*other.real - self.imag*other.imag
        imag = self.imag*other.real + other.imag*self.real
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        if other.real == 0 and other.imag == 0:
            raise ValueError("Cannot divide by zero")
        bottom = (other.conjugate()*other*1.).real
        top = self*other.conjugate()
        return ComplexNumber(top.real / bottom, top.imag / bottom)

    def __eq__(self, other):
        return self.imag == other.imag and self.real == other.real

    def __str__(self):
        return "{}{}{}i".format(self.real, '+' if self.imag >= 0 else '-',
                                                                abs(self.imag))
def numberofsets(file):
    def isaset(cards): #define a function that takes 3 lists of quadruples of integers, and checks if all the component-wise sums are divisible by 3
        list1, list2, list3=cards
        return (list1[0]+list2[0]+list3[0])%3==0 and (list1[1]+list2[1]+list3[1])%3==0 and (list1[2]+list2[2]+list3[2])%3==0 and (list1[3]+list2[3]+list3[3])%3==0
    with open(file) as setgame:
        cards=''.join(setgame.readlines()).split('\n')      
        cards=list(cards)                               #convert the text file into a list of strings
        if len(cards)!=12:
            raise ValueError("File must contain 12 cards.")
        cardint=cards                          
        for j in range(0,len(cardint)):
            cardint[j]=list(map(int, list(cards[j]))) #convert every string in the list into a list of integers
            for l in range(0,4):
                if cardint[j][l] not in [0,1,2]:
                    raise ValueError("Cards must be valid.")
        for K in itertools.combinations(cardint,2):
            if K[0]==K[1]:
                raise ValueError("No two cards can be the same.")
        iters=0
        for U in itertools.combinations(cardint,3):  #go through every 3-tuple of cards and consider if they form a Set.
            if isaset(U):
                iters+=1
            else:
                iters+=0 
    return iters
