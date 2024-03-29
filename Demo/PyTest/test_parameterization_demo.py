import pytest
def sum(a,b):
    return a+b
@ pytest.mark.parametrize("input1, input2, output",
                          [
                              (2,3,5),
                              (3,3,6),
                              (5,5,9)
                          ]
                          )
def test_calc_1(input1, input2, output):
    result = sum(input1,input2)
    assert result == output

# def test_calc_2():
#     result = sum(3,3)
#     assert result == 6
#
# def test_calc_3():
#     result = sum(5,5)
#     assert result == 10