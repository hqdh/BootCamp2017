# test_solutions.py
"""Volume 1B: Testing.
<Name>
<Class>
<Date>
"""

import solutions as soln
import pytest
import math
import itertools

# Problem 1: Test the addition and fibonacci functions from solutions.py
def test_addition():
    assert soln.addition(3,7)==10
    assert soln.addition(-1,4)==3
    assert soln.addition(-3,-5)==-8

def test_smallest_factor():
    assert soln.smallest_factor(2)==2
    assert soln.smallest_factor(15)==3
    assert soln.smallest_factor(121)==11
    assert soln.smallest_factor(2017)==2017
    assert soln.smallest_factor(1)==1

# Problem 2: Test the operator function from solutions.py
def test_operator():
    assert soln.operator(2,3,'+')==5
    assert soln.operator(1,2,'-')==-1
    assert soln.operator(6,7,'*')==42
    assert soln.operator(1,2,'/')==.5
    assert soln.operator(5,4,'/')==1.25
    with pytest.raises(Exception) as excinfo1:
        soln.operator(1,2,3)
    assert excinfo1.typename=='ValueError'
    assert excinfo1.value.args[0]=="Oper should be a string"
    with pytest.raises(Exception) as excinfo2:
        soln.operator(2,3,'+-')
    assert excinfo2.typename=='ValueError'
    assert excinfo2.value.args[0]=="Oper should be one character"
    with pytest.raises(Exception) as excinfo3:
        soln.operator(2,0,'/')
    assert excinfo3.typename=='ValueError'
    assert excinfo3.value.args[0]=="You can't divide by zero!"
    with pytest.raises(Exception) as excinfo4:
        soln.operator(2,0,'%')
    assert excinfo4.typename=='ValueError'
    assert excinfo4.value.args[0]=="Oper can only be: '+', '/', '-', or '*'"
    

# Problem 3: Finish testing the complex number class
@pytest.fixture
def set_up_complex_nums():
    number_1 = soln.ComplexNumber(1, 2)
    number_2 = soln.ComplexNumber(5, 5)
    number_3 = soln.ComplexNumber(2, 9)
    return number_1, number_2, number_3

def test_complex_addition(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 + number_2 == soln.ComplexNumber(6, 7)
    assert number_1 + number_3 == soln.ComplexNumber(3, 11)
    assert number_2 + number_3 == soln.ComplexNumber(7, 14)
    assert number_3 + number_3 == soln.ComplexNumber(4, 18)

def test_complex_multiplication(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 * number_2 == soln.ComplexNumber(-5, 15)
    assert number_1 * number_3 == soln.ComplexNumber(-16, 13)
    assert number_2 * number_3 == soln.ComplexNumber(-35, 55)
    assert number_3 * number_3 == soln.ComplexNumber(-77, 36)
def test_complex_subtraction(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1-number_2==soln.ComplexNumber(-4,-3)
    assert number_2-number_3==soln.ComplexNumber(3,-4)
    assert number_1-number_3==soln.ComplexNumber(-1,-7)
    assert number_3-number_3==soln.ComplexNumber(0,0)
def test_complex_conjugate(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1.conjugate()==soln.ComplexNumber(1,-2)
    assert number_2.conjugate()==soln.ComplexNumber(5,-5)
    assert number_3.conjugate()==soln.ComplexNumber(2,-9)
def test_complex_norm(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1.norm()==math.sqrt(5)
    assert number_2.norm()==math.sqrt(50)
    assert number_3.norm()==math.sqrt(85)
def test_complex_div(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 / number_2 == soln.ComplexNumber(0.3,0.1)
    with pytest.raises(Exception) as exc:
        number_1/soln.ComplexNumber(0,0)
    assert exc.typename=='ValueError'
    assert exc.value.args[0]=="Cannot divide by zero"
def test_complex_str(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert str(number_1)=='1+2i'




# Problem 4: Write test cases for the Set game.

def test_set():
    assert soln.numberofsets('Settrue.txt')==5
    with pytest.raises(Exception) as exc1:
        soln.numberofsets('Setnotvalid.txt')
    assert exc1.typename=='ValueError'
    assert exc1.value.args[0]=="Cards must be valid."
    with pytest.raises(Exception) as exc2:
        soln.numberofsets('Setrepeat.txt')
    assert exc2.typename=='ValueError'
    assert exc2.value.args[0]=="No two cards can be the same."
    with pytest.raises(Exception) as exc3:
        soln.numberofsets('Setlack.txt')
    assert exc3.typename=='ValueError'
    assert exc3.value.args[0]=="File must contain 12 cards."