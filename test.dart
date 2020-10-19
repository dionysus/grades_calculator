import 'grades.dart';

void main() {
  List<Grade> _roots = [];

  var class01 = Grade.asRoot("CSC209", 80);
  _roots.add(class01);

  var preps = Grade.asPercent("Preps", null, 5);
  class01.addSubGrade(preps);

  var lab01 = Grade.asPercent("lab01", 100, 2);
  var lab02 = Grade.asPercent("lab02", 100, 2);
  var lab03 = Grade.asPercent("lab03", 100, 2);
  var lab04 = Grade.asPercent("lab04", 100, 2);
  var lab05 = Grade.asPercent("lab05", 100, 2);
  class01.addSubGrade(lab01);
  class01.addSubGrade(lab02);
  class01.addSubGrade(lab03);
  class01.addSubGrade(lab04);
  class01.addSubGrade(lab05);

  Grade a1 = Grade.asPercent("A1", null, 10);
  class01.addSubGrade(a1);
  Grade a2 = Grade.asPercent("A2", null, 10);
  class01.addSubGrade(a2);
  Grade a3 = Grade.asPercent("A3", null, 10);
  class01.addSubGrade(a3);
  Grade a4 = Grade.asPercent("A4", null, 10);
  class01.addSubGrade(a4);

  Grade m1 = Grade.asPercent("midterm", null, 20);
  class01.addSubGrade(m1);
  Grade f1 = Grade.asPercent("final", null, 25);
  f1.setGoal(100);
  class01.addSubGrade(f1);

  print('\n');
  class01.printAll();
  print('\n');
  class01.updateAll();
  class01.printAll();
  print('\n');
}
