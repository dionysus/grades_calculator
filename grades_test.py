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
    test = Grades(100, 20, 95, None)
    assert test._goal_grade == 19

    test02 = Grades(None, None, 95, None)
    assert test02._goal_grade == 95


def test_tree_grade() -> None:
    """Test for nested grades
    """
    tests = Grades(None, None, 95, None)
    test01 = Grades(None, None, None, tests)

    assert test01._parent is tests
    assert test01._goal_grade == 95


if __name__ == '__main__':
    import pytest
    pytest.main(['grades_test.py'])
