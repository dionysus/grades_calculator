class Grade {
  String _name;
  String _nullString = '---';
  // tree
  List<Grade> _subGrades = [];
  Grade _parent;

  // attributes
  num _weight; // as a percent eg. 30
  num _grade;
  bool _gradeSet = false;
  num _gradeTotal;
  bool _goalSet = false;
  num _goal;

  num get percent => _grade / _gradeTotal * 100;

//! ----------------------------------------------------------------Constructors
  Grade(this._name);
  Grade.asRoot(this._name, num goal) {
    this.setGrade(null, 100);
    this.setGoal(goal);
  }
  Grade.asGrade(this._name, num grade, num gradeTotal, this._weight) {
    this.setGrade(grade, gradeTotal);
  }
  Grade.asPercent(this._name, num grade, this._weight) {
    this.setGrade(grade, 100);
  }

//! -------------------------------------------------------------------- GETTERS

  String getName() => this._name;
  Grade getParent() => this._parent;
  List<Grade> getSubGrades() => this._subGrades;
  num getGradeTotal() => this._gradeTotal;
  num getWeight() => this._weight;
  bool getGradeSet() => this._gradeSet;
  num getGoal() => this._goal;
  bool getGoalSet() => this._goalSet;

  Grade getRoot() {
    Grade root = this;
    while (root.getParent() != null) {
      root = root.getParent();
    }
    return root;
  }

//! ------------------------------------------------------------------ SUBGRADES

  addSubGrade(Grade other) {
    // add Grade to subGrade
    this._subGrades.add(other);
    other._parent = this;
    // updateAll();
  }

  removeSubGrade(Grade other) {
    // remove Grade from subGrade
    this._subGrades.remove(other);
    //other.delete();
    // updateAll();
  }

  moveGrade(Grade src, Grade dst) {
    // move this subGrade from one Grade to Another
    src._subGrades.remove(this);
    dst._subGrades.add(this);
    this._parent = dst;
    // updateAll();
  }

//! ---------------------------------------------------------------------- GRADE

  getGrade() {
    if (!this._gradeSet && this._goalSet) {
      return this.getGoal();
    } else {
      return this._grade;
    }
  }

  void setGrade(num grade, num gradeTotal) {
    // Sets grade, gradeSet, gradeTotal.
    // nulls gradeSet and grade if grade is null
    this._gradeSet = (grade != null);
    this._grade = grade;
    this._gradeTotal = gradeTotal;
    // updateAll();
  }

  void setPercent(num percent) {
    setGrade(percent, 100);
  }

//! ----------------------------------------------------------------------- GOAL

  setGoal(num goal) {
    this._goalSet = (goal != null);
    this._goal = goal;
  }

//! ---------------------------------------------------------------- UPDATE TREE
  // update (GRADE or GOAL) and WEIGHT

  updateAll() {
    // navigate up to root
    Grade root = getRoot();
    root._weight = 100;
    // calculate child weights
    updateChildGoals();
  }

  updateChildGoals() {
    if (this._gradeSet) {
      return;
    }

    // calculate children by _weight
    num sumGrade = 0;
    num sumWeight = 0;

    this.getSubGrades().forEach((child) {
      if (child.getGradeSet()) {
        sumGrade += child.getWeight() / this.getGradeTotal() * child.getGrade();
        sumWeight += child.getWeight();
      } else if (child.getGoalSet()) {
        sumGrade += child.getWeight() / this.getGradeTotal() * child.getGoal();
        sumWeight += child.getWeight();
      }
    });

    num reqPercent =
        (this.getGoal() - sumGrade) / (this.getWeight() - sumWeight);

    this.getSubGrades().forEach((child) {
      if (!child.getGradeSet() && !child.getGoalSet()) {
        child._goal = reqPercent * child.getGradeTotal();
      }
    });
  }

//! ---------------------------------------------------------------------- PRINT
  getParentName() {
    var parent = this._parent;
    if (parent != null) {
      return parent.getName();
    } else {
      return _nullString;
    }
  }

  getGoalString(n) {
    var goal = this._goal;
    if (goal != null) {
      return goal.toStringAsFixed(n);
    }
    return _nullString;
  }

  getWeightString(n) {
    var weight = this._weight;
    if (weight != null) {
      return weight.toStringAsFixed(n);
    } else {
      return _nullString;
    }
  }

  getGradeString(n) {
    var grade = this.getGrade();
    if (grade != null) {
      return grade.toStringAsFixed(n);
    } else {
      return _nullString;
    }
  }

  printAll() {
    print("Name".padRight(20) +
        "Grade".padRight(20) +
        "Goal".padRight(10) +
        "Weight".padRight(10));
    Grade root = this.getRoot();
    root.printDescendents();
  }

  printSelf(level) {
    // prefix
    String prefix = '  ' * level + "└── " + this._name;
    prefix = prefix.padRight(20);
    // suffix

    String grade = this._grade.toString();
    String grade_string = (this._gradeSet) ? '(${grade})' : '[${grade}]';
    String grade_total = this.getGradeTotal().toString();
    grade_string =
        ' ' * level + '${grade_string} / ${grade_total}'.padRight(20);
    String weight = this.getWeight().toString();
    String weight_string = ' ' * level + '(${weight})';
    String goal = this._goal?.toStringAsFixed(2);
    String goal_string = ' ' * level +
        ((this._goalSet) ? '(${goal})' : '[${goal}]').padRight(10);
    String suffix = '${grade_string} ${goal_string} ${weight_string}';

    print(prefix + suffix);
  }

  printDescendents([level = 0]) {
    this.printSelf(level);
    for (int i = 0; i < this._subGrades.length; i++) {
      this._subGrades[i].printDescendents(level + 1);
    }
  }

  @override
  String toString() {
    String grade = this.getGrade().toString();
    String grade_total = this.getGradeTotal().toString();
    return '${this._name.padRight(20)} | ${grade} / ${grade_total} G:${this.getGoalString(2).padRight(4)} | W: ${this.getWeight()}';
  }
}
