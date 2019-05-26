from typing import Optional, List
import math

from grades import Grades

'''
Grades
     name: str,
     weight: Optional[float],
     grade_total: Optional[float],
     goal_percent: Optional[int]
     -> None
'''


def test_single_percent() -> None:
    """Test for single unnested grade
    """
    tests = Grades("tests", None, None, 90)
    test01 = Grades("test 01", 100, None, None)

    tests.add_subgrade(test01)
    assert test01.goal_percent == 90


def test_two_percent_no_rcv() -> None:
    """Test for two unnested grades with no grades received
    """
    tests = Grades("tests", None, None, 90)
    test01 = Grades("test 01", 50, None, None)
    test02 = Grades("test 02", 50, None, None)

    tests.add_subgrade(test01)
    tests.add_subgrade(test02)
    assert test01.goal_percent == 90
    assert test02.goal_percent == 90


def test_remove_subgrade() -> None:
    """
    """
    tests = Grades("tests", None, None, 90)
    test01 = Grades("test 01", 25, None, None)
    test02 = Grades("test 02", 25, None, None)
    test03 = Grades("test 03", 50, None, None)

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
    tests = Grades("tests", None, None, 90)
    test01 = Grades("test 01", 50, 100, None)
    test02 = Grades("test 02", 50, 100, None)

    tests._subgrades.append(test01)
    test01._parent = tests
    tests._subgrades.append(test02)
    test02._parent = tests

    test02.grade_received = 80

    assert tests.update_remaining_percent() == 100


def test_goal_percent_two_percent_single_rcv() -> None:
    """Test for two unnested grades with single grade received.
    """
    tests = Grades("tests", None, None, 90)

    test01 = Grades("test 01", 50, 100, None)
    test02 = Grades("test 02", 50, 100, None)

    tests.add_subgrade(test01)
    tests.add_subgrade(test02)

    assert test01.goal_percent == 90
    assert test02.goal_percent == 90

    test01.update_grade_received(80)

    assert test02.goal_percent == 100


def test_goal_percent_nested_percent() -> None:
    """Test for nested grades with grades received.
    """
    tests = Grades("tests", None, None, 90)

    midterm = Grades("midterm", 100, 50, None)

    tests.add_subgrade(midterm)

    question01 = Grades("question 01", 10, 10, None)
    midterm.add_subgrade(question01)
    question02 = Grades("question 02", 10, 10, None)
    midterm.add_subgrade(question02)
    question03 = Grades("question 03", 10, 10, None)
    midterm.add_subgrade(question03)
    question04 = Grades("question 04", 10, 10, None)
    midterm.add_subgrade(question04)
    question05 = Grades("question 05", 10, 10, None)
    midterm.add_subgrade(question05)

    question01.update_grade_received(10)
    question02.update_grade_received(10)
    question03.update_grade_received(10)
    question04.update_grade_received(5)

    assert question05.goal_percent == 100


def test_goal_percent_updating() -> None:
    """"""
    tests = Grades("tests", None, None, 90)
    midterm = Grades("midterm", 100, 50, None)
    tests.add_subgrade(midterm)
    question01 = Grades("question 01", 10, 10, None)
    midterm.add_subgrade(question01)
    question02 = Grades("question 02", 10, 10, None)
    midterm.add_subgrade(question02)
    question03 = Grades("question 03", 10, 10, None)
    midterm.add_subgrade(question03)
    question04 = Grades("question 04", 10, 10, None)
    midterm.add_subgrade(question04)
    question05 = Grades("question 05", 10, 10, None)
    midterm.add_subgrade(question05)

    for q in [question01, question02, question03, question04, question05]:
        assert q.goal_percent == 90

    # one grade received
    question01.update_grade_received(8)
    for p in [question01]:
        assert p.goal_percent is None
    for q in [question02, question03, question04, question05]:
        assert q.goal_percent == 93

    # two grade received
    question02.update_grade_received(8)
    for p in [question01, question02]:
        assert p.goal_percent is None
    for q in [question03, question04, question05]:
        assert q.goal_percent == 97

    # three grade received
    question03.update_grade_received(10)
    for p in [question01, question02, question03]:
        assert p.goal_percent is None
    for q in [question04, question05]:
        assert q.goal_percent == 95

    # four grade received
    question04.update_grade_received(10)
    for p in [question01, question02, question03, question04]:
        assert p.goal_percent is None
    for q in [question05]:
        assert q.goal_percent == 90

    # five grade received
    question05.update_grade_received(10)
    for p in [question01, question02, question03, question04, question05]:
        assert p.goal_percent is None


if __name__ == '__main__':
    import pytest
    pytest.main(['grades_test.py'])

    print()

    course = Grades("CSC 101", None, None, None)

    # WEEKLY PREPS
    preps = Grades("weekly preps", 5, None, None)
    course.add_subgrade(preps)

    # PSETS
    assignments = Grades("assignments", 20, None, None)
    course.add_subgrade(assignments)

    pset01 = Grades("pset 01", 5, 10, None)
    assignments.add_subgrade(pset01)
    pset02 = Grades("pset 02", 5, 10, None)
    assignments.add_subgrade(pset02)
    pset03 = Grades("pset 03", 5, 10, None)
    assignments.add_subgrade(pset03)
    pset04 = Grades("pset 04", 5, 10, None)
    assignments.add_subgrade(pset04)

    # EXAMS
    exams = Grades("tests", 75, None, None)
    course.add_subgrade(exams)

    midterm01 = Grades("midterm 01", 15, 40, None)
    exams.add_subgrade(midterm01)
    midterm02 = Grades("midterm 02", 15, 40, None)
    exams.add_subgrade(midterm02)
    final = Grades("final", 45, 80, None)
    exams.add_subgrade(final)

    course.print_tree()
    print('-' * 70 + '\n' * 3)

    course.set_goal_percent(85)
    # preps.set_goal_percent(100)
    # assignments.set_goal_percent(95)

    course.print_tree()
    print('-' * 70 + '\n' * 3)
