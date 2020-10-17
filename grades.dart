class Grade {
  String _name;
  String _nullString = '---';
  // tree
  List<Grade> _subGrades = [];
  Grade _parent;

  // attributes
  double _weight; // as a percent eg. 30
  bool _weightSet = false;
  double _grade;
  bool _gradeSet = false;
  double _gradeTotal;
  bool _goalSet = false;
  double _goal;

  double get percent => _grade / _gradeTotal * 100;

  // Constructors
  Grade(this._name);
  Grade.asGrade(this._name, this._grade, this._gradeTotal) {
    this._gradeSet = true;
  }
  Grade.asPercent(this._name, this._grade) {
    this._gradeSet = true;
    this._gradeTotal = 100.0;
  }

//! -------------------------------------------------------------------- GETTERS

  getName() => this._name;
  getParent() => this._parent;
  getChildren() => this._subGrades;
  getRoot() {
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

  void setGrade(double grade, double gradeTotal) {
    // Sets grade, gradeSet, gradeTotal.
    // nulls gradeSet and grade if grade is null
    this._gradeSet = (grade != null);
    this._grade = grade;
    this._gradeTotal = gradeTotal;
    // updateAll();
  }

  void setPercent(double percent) {
    setGrade(percent, 100);
  }

//! ----------------------------------------------------------------------- GOAL
  getGoal() => this._goal;

  setGoal(double goal) {
    this._goalSet = (goal != null);
    this._goal = goal;
  }

//! --------------------------------------------------------------------- WEIGHT

  getWeight() => this._weight;

  setWeight(double weight) {
    this._weightSet = (weight != null);
    this._weight = weight;
    // updateAll();
  }

//! ---------------------------------------------------------------- UPDATE TREE
	// update (GRADE or GOAL) and WEIGHT

  updateAll() {
    // navigate up to root
    Grade root = getRoot();
    root._weight = 100;
    // calculate child weights
    root.updateWeights();
  }

  updateWeights() {

    double sumWeight = 0.0;
    int notWeightSetCount = 0;

    this._subGrades.forEach((child) {
      if (child._weightSet) {
        sumWeight += child._weight;
      } else {
        notWeightSetCount += 1;
      }
    });
    this._subGrades.forEach((child) {
      if (!child._weightSet) {
        child._weight = (100 - sumWeight) / notWeightSetCount;
      }
    });
    this._subGrades.forEach((child) {
      child.updateWeights();
    });
  }

  calcGrade() {
    // grade assigned
    if (this._gradeSet) {
      return;
    }
    // has no grade + no children
    else if (this._subGrades.length == 0) {
      return null;
    }

    // calculate children by _weight
    double sumWeight = 0.0;
    int countWeightless = 0;
    double tempGrade = 0.0;

    this._subGrades.forEach((child) {
      if (child._weight != null) {
        sumWeight += child._weight;
      } else {
        countWeightless++;
      }
    });

    this._subGrades.forEach((child) {
      if (child._weight != null) {
        var childGrade = child.getGrade();
        if (childGrade != null) {
          tempGrade += childGrade * (child._weight / 100);
        } else {
          return null;
        }
      } else {
        // assume weightless has unassigned _weight split between number of weightless
        tempGrade +=
            child.getGrade() * (((100 - sumWeight) / countWeightless) / 100);
      }
    });
    return tempGrade;
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

  printDescendents([level = 1]) {
    if (level == 1) print(this);
    for (int i = 0; i < this._subGrades.length; i++) {
      Grade child = this._subGrades[i];
      var symbol = (i == this._subGrades.length - 1) ? "└──" : "├──";
      if (level > 1) {
        print(' |' + '  ' * level + '$symbol $child');
      } else {
        print(' ' * level + '$symbol $child');
      }
      child.printDescendents(level + 1);
    }
  }

  @override
  String toString() {
    return '${this._name.padRight(10)} | %: ${this.getGradeString(0).padRight(4)} [G: ${this.getGoalString(2).padRight(4)}| W: ${this.getWeight()}]';
  }
}
