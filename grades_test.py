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

    test02 = Grades(100, None, 95)
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


def test_remove_subgrade() -> None:
    """
    """
    tests = Grades(None, None, 90)
    test01 = Grades(25, None, None)
    test02 = Grades(25, None, None)
    test03 = Grades(50, None, None)

    tests.add_subgrade(test01)
    tests.add_subgrade(test02)
    tests.add_subgrade(test03)

    assert test01.goal_percent == 90
    assert test02.goal_percent == 90
    assert test03.goal_percent == 90

    test03.update_grade_received(100)

    assert test01.goal_percent == 80
    assert test02.goal_percent == 80

    tests.remove_subgrade(test03)

    assert test01.goal_percent == 90
    assert test02.goal_percent == 90


def test_update_remaining_percent() -> None:
    """Test for update_remaining_percent method
    """
    tests = Grades(None, None, 90)
    test01 = Grades(50, 100, None)
    test02 = Grades(50, 100, None)

    tests._subgrades.append(test01)
    test01._parent = tests
    tests._subgrades.append(test02)
    test02._parent = tests

    test02.grade_received = 80

    tests.update_remaining_percent()

    assert tests._remaining_percent == 100


def test_goal_percent_two_percent_single_rcv() -> None:
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


def test_goal_percent_nested_percent() -> None:
    """Test for nested grades with grades received.
    """
    tests = Grades(None, None, 90)

    midterm = Grades(100, 50, None)

    tests.add_subgrade(midterm)

    question01 = Grades(10, 10, None)
    midterm.add_subgrade(question01)
    question02 = Grades(10, 10, None)
    midterm.add_subgrade(question02)
    question03 = Grades(10, 10, None)
    midterm.add_subgrade(question03)
    question04 = Grades(10, 10, None)
    midterm.add_subgrade(question04)
    question05 = Grades(10, 10, None)
    midterm.add_subgrade(question05)

    question01.update_grade_received(10)
    question02.update_grade_received(10)
    question03.update_grade_received(10)
    question04.update_grade_received(5)

    assert question05.goal_percent == 100


if __name__ == '__main__':
    import pytest
    pytest.main(['grades_test.py'])
