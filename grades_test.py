from typing import Optional, List
import math

from grades import Grades


'''
Grades__init__
(self, weight: Optional[float], grade_total: float, goal_percent: Optional[int], 
parent: Optional[Grades]) -> None:
'''


def test_single_grade() -> None:
    """Test for unnested grades
    """
    test = Grades(100, 20, 95)
    assert test._goal_grade == 19

    test02 = Grades(100, None, 95)
    assert test02._goal_grade == 95
    assert test02.goal_percent == 95


def test_single_percent() -> None:
    """Test for single unnested grade
    """
    tests = Grades(None, None, 90)
    test01 = Grades(100, None, None)

    tests.add_subgrade(test01)
    assert test01.goal_percent == 90


def test_two_percent_no_rcv() -> None:
    """Test for two unnested grades with no grades received
    """
    tests = Grades(None, None, 90)
    test01 = Grades(50, None, None)
    test02 = Grades(50, None, None)

    tests.add_subgrade(test01)
    tests.add_subgrade(test02)
    assert test01.goal_percent == 90
    assert test02.goal_percent == 90


def test_update_remaining_percent() -> None:
    """Test for update_remaining_percent method
    """
    tests = Grades(None, None, 90)
    test01 = Grades(50, 100, None)
    test02 = Grades(50, 100, None)

    tests._sub_grades.append(test01)
    test01._parent = tests
    tests._sub_grades.append(test02)
    test02._parent = tests

    test02.grade_received = 80

    tests.update_remaining_percent()

    assert tests._remaining_percent == 100


def test_two_percent_single_rcv() -> None:
    """Test for two unnested grades with single grade received.
    """
    tests = Grades(None, None, 90)

    test01 = Grades(50, 100, None)
    test02 = Grades(50, 100, None)

    tests.add_subgrade(test01)
    tests.add_subgrade(test02)

    assert test01.goal_percent == 90
    assert test02.goal_percent == 90

    test01.update_grade_received(80)

    assert tests._remaining_percent == 100
    assert test02.goal_percent == 100


# def test_tree_grade() -> None:
#     """Test for nested grades
#     """
#     tests = Grades(None, None, 95, None)
#     test01 = Grades(None, None, None, tests)
#
#     assert test01._parent is tests
#     assert test01.goal_percent == 95
#     assert test01._goal_grade == 95
#
#
# def test_tree_existing_grade() -> None:
#     """Test for nested grades
#     """
#     tests = Grades(None, None, 90)
#     test01 = Grades(50, None, None)
#     test02 = Grades(50, None, None)
#
#     assert test01.goal_percent == 90
#     assert test02.goal_percent == 90
#
#     test01.update_grade_received(80)
#
#     assert test02._goal_grade == 100


if __name__ == '__main__':
    import pytest
    pytest.main(['grades_test.py'])
