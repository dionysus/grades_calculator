from __future__ import annotations
from typing import Optional, List
import math

GOAL_PERCENT = 90   # default goal


class Grades:
    """
    Grades Tree

    Tree that will calculate percentage required to achieve goal percent of
    parent.

    == attributes ==
    weight - percentage of weight.  if none, count marks
    grade_received - mark received
    grade_total - total possible grade
    goal_percent - goal of grade in percent

    == private attributes ==

    _name - name of grade
    _subgrades - list of sub grades
    _parent - parent of the tree
    _goal_percent_set - true if manually set (not determined by parent)

    # TODO: potential attributes
    _max_percent - maximum percent achievable

    == precondition ==
    all values (except grade_received) >= 0
    """
    weight: Optional[float]
    grade_received: Optional[float]
    grade_total: Optional[float]

    goal_percent: Optional[int]
    _goal_percent_set: bool

    _name: str
    _max_percent: float
    _subgrades: List[Grades]
    _parent: Optional[Grades]

    def __init__(self,
                 name: str,
                 weight: Optional[float],
                 grade_total: Optional[float],
                 goal_percent: Optional[int]
                 ) -> None:

        self._name = name

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
            self._goal_percent_set = True
        else:
            self._goal_percent_set = False
            self.goal_percent = GOAL_PERCENT

        self._max_percent = 100

    def add_subgrade(self, grade: Grades) -> None:
        """
        add subgrade to parent and parent to subgrade

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

    def remove_subgrade(self, grade: Grades) -> None:
        """remove subgrade from parent and parent from subgrade
        """
        self._subgrades.remove(grade)
        grade._parent = None

        if grade.weight is not None:
            self.weight -= grade.weight

        grade.update_grade_received(GOAL_PERCENT)

        self.update_all_goal_percents()

    def update_grade_received(self, grade: Optional[float]) -> None:
        """update the grade received with a float rounded to 1 decimal point
        or None
        """
        self.grade_received = grade

        if self._parent is not None:
            self._parent.update_all_goal_percents()

    def set_goal_percent(self, percent: Optional[int]) -> None:
        """update the goal_percent with a fixed goal, or clear goal
        """

        if percent is not None:
            self.goal_percent = percent
            self._goal_percent_set = True

        else:
            self.goal_percent = None
            self._goal_percent_set = False

        if self._parent is not None:
            self._parent.update_all_goal_percents()
        else:
            self.update_all_goal_percents()

    def update_all_goal_percents(self) -> None:
        """update the goal percent with goal_percent of tree and children
        """
        # TODO: Make recursive

        # if self._subgrades == []:
        #     if self.set_goal_percent():
        #         pass
        #     else:
        #         self.g

        if self._subgrades != []:
            remaining_percent = self.update_remaining_percent()

            for sub in self._subgrades:
                if sub.grade_received is None and not sub._goal_percent_set:
                    sub.goal_percent = remaining_percent
                if sub.grade_received:
                    sub.goal_percent = None

    def update_remaining_percent(self) -> int:
        """
        return grade percent needed for subgrades without received grade or
        individual goal grade to received goal grade
        """
        total_weight = 0

        rcv_weight = 0
        rcv_value = 0

        total_grade_total = 0
        total_grade_received = 0

        for sub in self._subgrades:

            total_weight += sub.weight

            if sub.grade_received is not None:
                rcv_weight += sub.weight
                rcv_value += sub.weight * sub.grade_received / sub.grade_total
                total_grade_total += sub.grade_total
                total_grade_received += sub.grade_received

            elif sub._goal_percent_set:
                rcv_weight += sub.weight
                rcv_value += sub.weight * sub.goal_percent / 100

        self.weight = total_weight

        # TODO: no weight?

        if total_weight <= rcv_weight:  # all marks received
            remaining_percent = 0
            self.grade_received = total_grade_received
            self.grade_total = total_grade_total
            self.grade_received = total_grade_received

        else:
            remaining_percent = math.ceil(
                (self.goal_percent / 100 * total_weight - rcv_value) /
                (total_weight - rcv_weight) * 100
            )

        return remaining_percent

    def get_goal_grade(self) -> int:
        """get required grade to achieve goal_percent
        """
        return math.ceil(self.goal_percent / 100 * self.grade_total)

    def print_tree(self, indentation: int = 0, indent: str = '') -> None:
        """ Print a simple text visualization of the Tree
        """

        weight = self._none_str(self.weight)

        if self._goal_percent_set:
            goal_percent = '({})'.format(self._none_str(self.goal_percent))
        else:
            goal_percent = '[{}]'.format(self._none_str(self.goal_percent))

        grade_received = self._none_str(self.grade_received)
        grade_total = self._none_str(self.grade_total)

        id_str = '[WT: {:>3.3} | GP: {:>5.5} | GR: {:>3.3} | GT: {:>3.3}]'.format(
            weight, goal_percent, grade_received, grade_total)

        level_str = indent + self._name

        f = '{0:25} {1:>25}'

        print(f.format(level_str, id_str))

        if indent == '':
            print('-' * 70)
        else:
            if indent[-4] == '├':
                indent = indent[:-4] + '│   '
            else:
                indent = indent[:-4] + '    '

        for i in range(len(self._subgrades)):

            if i == len(self._subgrades) - 1:  # last in sub
                indent_sub = indent + '└── '
            else:
                indent_sub = indent + '├── '

            self._subgrades[i].print_tree(indentation + 1, indent_sub)

    def _none_str(self, num) -> str:
        """return num as a str if num is not None, else return --- """
        if num is None:
            return '---'
        else:
            return str(num)
