import 'grades.dart';

void main() {
  List<Grade> _roots = [];

  var class01 = Grade("CSC209");
  class01.setGoal(90);
  _roots.add(class01);

  var preps = Grade.asPercent("Preps", 90);
  preps.setWeight(5);
  class01.addSubGrade(preps);

  var labs = Grade("Labs");
  var lab01 = Grade.asPercent("lab01", 100);
  var lab02 = Grade.asPercent("lab02", 100);
  var lab03 = Grade.asPercent("lab03", 90);
  var lab04 = Grade.asPercent("lab04", 94);
  var lab05 = Grade.asPercent("lab05", 100);
  var lab06 = Grade.asPercent("lab06", 33);
  var lab07 = Grade.asPercent("lab07", 0);
  var lab08 = Grade.asPercent("lab08", 100);
  var lab09 = Grade.asPercent("lab09", 100);
  var lab10 = Grade.asPercent("lab10", 100);
  // var lab11 = Grade.asPercent("lab11", 0);
  labs.addSubGrade(lab01);
  labs.addSubGrade(lab02);
  labs.addSubGrade(lab03);
  labs.addSubGrade(lab04);
  labs.addSubGrade(lab05);
  labs.addSubGrade(lab06);
  labs.addSubGrade(lab07);
  labs.addSubGrade(lab08);
  labs.addSubGrade(lab09);
  labs.addSubGrade(lab10);
  // labs.addSubGrade(lab11);
  class01.addSubGrade(labs);

  Grade assignments = Grade("Assignments");
  class01.addSubGrade(assignments);

  Grade a1 = Grade.asPercent("A1", 100);
  a1.setWeight(9);
  assignments.addSubGrade(a1);
  Grade a2 = Grade.asPercent("A2", 100);
  a2.setWeight(17);
  assignments.addSubGrade(a2);
  Grade a3 = Grade.asPercent("A3", 95);
  a3.setWeight(17);
  assignments.addSubGrade(a3);
  Grade a4 = Grade("A4");
  a4.setWeight(17);
  assignments.addSubGrade(a4);

  Grade m1 = Grade.asPercent("midterm", 84);
  m1.setWeight(18);
  class01.addSubGrade(m1);

  // for (var i; i < _roots.length; i++) {

  // }
  // print(class01);
  // print(class01.getName());
  // print(class01.getParentName());
  // print(class01.getGoal());

  class01.printDescendents();
}
