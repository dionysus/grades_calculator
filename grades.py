from __future__ import annotations
from typing import Optional, List
import math

GOAL_PERCENT = 90   # default goal


class Grades:
    """
    Grades Tree

    == attributes ==
    weight - percentage of weight.  if none, count marks
    grade_received - mark received
    grade_total - total possible grade
    goal_percent - goal of grade in percent

    == private attributes ==

    _subgrades - list of sub grades
    _parent - parent of the tree
    _remaining_percent - percent needed for sub grades to achieve goal percent
    _max_percent - maximum percent achievable

    == precondition ==
    all values (except grade_received) >= 0


    """
    weight: Optional[float]
    grade_received: Optional[float]
    grade_total: Optional[float]
    goal_percent: Optional[int]

    _remaining_percent: int
    _max_percent: float
    _subgrades: List[Grades]
    _parent: Optional[Grades]

    def __init__(self,
                 weight: Optional[float],
                 grade_total: Optional[float],
                 goal_percent: Optional[int]
                 ) -> None:
        """
        """
        self.weight = weight

        self.grade_received = None

        if grade_total is None:
            self.grade_total = 100
        else:
            self.grade_total = grade_total

        self._subgrades = []
        self._parent = None

        if goal_percent is not None:
            self.goal_percent = goal_percent
        elif self._parent is None:
            self.goal_percent = GOAL_PERCENT
        else:
            self.goal_percent = self._parent._remaining_percent

        self._remaining_percent = self.goal_percent
        self._max_percent = 100

    def add_subgrade(self, grade: Grades):
        """
        add subgrade to parent

        eg. question -> midterm -> tests
        """
        self._subgrades.append(grade)
        grade._parent = self

        if grade.weight is not None:
            if self.weight is None:
                self.weight = grade.weight
            else:
                self.weight += grade.weight

        self.update_all_goal_percents()

    def update_grade_received(self, grade: Optional[float]) -> None:
        """update the grade received with a float rounded to 1 decimal point
        or None
        """
        self.grade_received = grade

        # update all
        if self._parent is not None:
            self._parent.update_all_goal_percents()

    def update_all_goal_percents(self) -> None:
        """update the goal percent with goal_percent of tree and children
        """
        # TODO: but what if goal is set for a subgrade?

        self.update_remaining_percent()

        for sub in self._subgrades:
            if sub.grade_received is None:
                sub.goal_percent = self._remaining_percent

    def update_remaining_percent(self) -> None:
        """
        for parent nodes, update remaining_percent needed for subgrades
        to received desired grade
        """
        total_weight = 0

        rcv_weight = 0
        rcv_value = 0

        for sub in self._subgrades:

            total_weight += sub.weight

            if sub.grade_received is not None:
                rcv_weight += sub.weight
                rcv_value += sub.weight * sub.grade_received / sub.grade_total

        self.weight = total_weight

        self._remaining_percent = math.ceil(
            (self.goal_percent / 100 * total_weight - rcv_value) /
            (total_weight - rcv_weight) * 100
        )

    def get_goal_grade(self) -> int:
        """get required grade to achieve goal_percent
        """
        return math.ceil(self.goal_percent / 100 * self.grade_total)
