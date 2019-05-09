from __future__ import annotations
from typing import Optional, List
import math

GOAL_PERCENT = 90


class Grades:
    """
    Grades Tree

    == attributes ==
    weight - percentage of weight.  if none, count marks
    grade_received - mark received
    grade_total - total possible grade
    goal_percent - goal of grade in percent
    goal_grade - goal of grade as mark
    sub_grades - list of sub grades
    _parent - parent of the tree

    == precondition ==
        all values (except grade_received) >= 0

    """
    weight: Optional[float]
    grade_received: Optional[float]
    grade_total: Optional[float]
    goal_percent: Optional[int]
    _goal_grade: float
    _sub_grades: List[Grades]
    _parent: Optional[Grades]

    def __init__(self,
                 weight: Optional[float],
                 grade_total: float,
                 goal_percent: Optional[int] = None,
                 parent: Optional[Grades] = None
                 ) -> None:
        """
        """
        self.weight = weight
        self.grade_received = None

        if grade_total is None:
            self.grade_total = 100
        else:
            self.grade_total = grade_total

        self._sub_grades = []

        self._parent = parent
        if self._parent is not None:
            if self not in self._parent._sub_grades:
                self._parent._sub_grades.append(self)

        if goal_percent is not None:
            self.goal_percent = goal_percent
        elif self._parent is None:
            self.goal_percent = GOAL_PERCENT
        else:
            # TODO: update all goal percents
            # self.goal_percent = self.get_goal_percent()
            self.goal_percent = self._parent.goal_percent
        self._goal_grade = math.ceil((self.goal_percent / 100) * self.grade_total)

    def update_grade_received(self, grade: Optional[float]) -> None:
        """update the grade received with a float rounded to 1 decimal point
        or None
        """
        self.grade_received = grade
        if not grade:
            self._parent.update_goals()

    def update_goal_percent(self, goal_percent: int) -> None:
        """update the goal percent with goal_percent of tree and children
        """
        self.goal_percent = goal_percent
        self.update_goal_grade()

        # update children

    def update_goal_grade(self) -> None:
        """update the goal_grade with the required grade (ceil) to
        achieve goal_percent
        """
        self._goal_grade = math.ceil(self.goal_percent / 100 * self.grade_total)

    def get_goal_percent(self) -> int:
        """return goal percent required for item to achieve goal_percent
        """
        pass
