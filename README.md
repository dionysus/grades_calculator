# grades_calculator

Personal project: a grades calculator for setting course goals to achieve optimal grades.

---

## Structure

The data is organized using a tree structure, with a parent tree, (ex. 'CS101'), containing subgrades (ex. `exercises`, `assignments`, and `exams`), each with subtrees breaking down individual items.

Taking the syllabus of an example course, this is organized into a tree:

```
CS101
├── weekly preps
│   ├── week 1
│   ├── week 2
│   ├── week 3
│   ├── week 4
│   └── week 5
├── assignments
│   ├── PSet 1
│   ├── PSet 2
│   ├── PSet 3
│   └── Pset 4
├── exams
│   ├── midterm 1
│   ├── midterm 1
│   └── final
```
---

## Weight

For each tree, the `weight` is defined as the percent the item accounts for of the final mark.

In our example, the syllabus provides a thorough breakdown of what each course item weighs:

```
CS101               WEIGHT
├── weekly preps    [5%]
│   ├── week 1        [1%]
│   ├── week 2        [1%]
│   ├── week 3        [1%]
│   ├── week 4        [1%]
│   └── week 5        [1%]
├── assignments     [20%]
│   ├── PSet 1        [5%]
│   ├── PSet 2        [5%]
│   ├── PSet 3        [5%]
│   └── Pset 4        [5%]
├── exams           [75%]
│   ├── midterm 1     [15%]
│   ├── midterm 2     [15%]
│   └── final         [45%]
```

The final weight should be 100%, but we should account for bonus marks, or grades over 100%.

---

## Goal

For each tree, there is an attribute `goal_percent`, an integer representing the percent that the user would like to achieve.

This can be inherited from the parent (calculated automatically to achieve the percent), or defined locally.

In our example, we have not set any goals, so we default to 90%

```
                    WEIGHT %    GOAL %
CS101               [100]       [90]
├── weekly preps      [5]         [90]
│   ├── week 1          [1]         [90]
│   ├── week 2          [1]         [90]
│   ├── week 3          [1]         [90]
│   ├── week 4          [1]         [90]
│   └── week 5          [1]         [90]
├── assignments       [20]        [90]
│   ├── PSet 1          [5]         [90]
│   ├── PSet 2          [5]         [90]
│   ├── PSet 3          [5]         [90]
│   └── Pset 4          [5]         [90]
├── exams             [75]        [90]
│   ├── midterm 1       [15]        [90]
│   ├── midterm 2       [15]        [90]
│   └── final           [45]        [90]
```

Then without any set goals, we will simply need to achieve 90% in every item.

But let's say that since `weekly preps` are free marks, and `assignments` we can work hard on, these are manually set (using the `()` brackets to denote this), then we can see the goals of the remaining.

```
                    WEIGHT %    GOAL %
CS101               [100]       (85)
├── weekly preps      [5]         (100)
│   ├── week 1          [1]         [100]
│   ├── week 2          [1]         [100]
│   ├── week 3          [1]         [100]
│   ├── week 4          [1]         [100]
│   └── week 5          [1]         [100]
├── assignments       [20]        (95)
│   ├── PSet 1          [5]         [95]
│   ├── PSet 2          [5]         [95]
│   ├── PSet 3          [5]         [95]
│   └── Pset 4          [5]         [95]
├── exams             [75]        [82]
│   ├── midterm 1       [15]        [82]
│   ├── midterm 2       [15]        [82]
│   └── final           [45]        [82]
```

That means for the `weekly preps`, our goal is 100%, and for `assignments`, our goal is 95%, then for our `exams`, we will need at least 82% to achieve our goal of 85%.

>`goal` = `weekly preps` + `assignments` + `exams`
> 85% = (100% * 5%) + (95% * 20%) + (`exams.goal_percent` * 75%)
> 85% = (5%) + (19%) + (`exams.goal_percent` * 75%)
> `exams.goal_percent` = 82%

But this can be tuned further.  For example, we think we can get 90% on our both `midterm 1` and `midterm 2`, so we can put those as our goals.

```
                    WEIGHT %    GOAL %
CS101               [100]       (85)
├── weekly preps      [5]         (100)
│   ├── week 1          [1]         [100]
│   ├── week 2          [1]         [100]
│   ├── week 3          [1]         [100]
│   ├── week 4          [1]         [100]
│   └── week 5          [1]         [100]
├── assignments       [20]        (95)
│   ├── PSet 1          [5]         [95]
│   ├── PSet 2          [5]         [95]
│   ├── PSet 3          [5]         [95]
│   └── Pset 4          [5]         [95]
├── exams             [75]        [82]
│   ├── midterm 1       [15]        (90)
│   ├── midterm 2       [15]        (90)
│   └── final           [45]        [78]
```

Then the minimum we need for the final will be only 78%, to achieve an overall 85%.

## Grades

As marks are received, we can call `update_grade_received` to update the grade received.  Each item, also has a `grade_total`, denoting the total possible grades for the item.

```
                    WEIGHT %    GOAL %        GRADE TOTAL   GRADE RECEIVED
CS101               [100]       (85)          [None]        [50]
├── weekly preps      [5]         (100)         [50]          [50]
│   ├── week 1          [1]         None          (10)          (10)
│   ├── week 2          [1]         None          (10)          (10)
│   ├── week 3          [1]         None          (10)          (10)
│   ├── week 4          [1]         None          (10)          (10)
│   └── week 5          [1]         None          (10)          (10)
├── assignments       [20]        (95)          [80]          [72]
│   ├── PSet 1          [5]         None          (20)          (17)
│   ├── PSet 2          [5]         None          (20)          (18)
│   ├── PSet 3          [5]         None          (20)          (19)
│   └── Pset 4          [5]         None          (20)          (18)
├── exams             [75]        [83]          [None]        [None]
│   ├── midterm 1       [15]        (90)          (40)          (36)
│   ├── midterm 2       [15]        (90)          (40)          [None]
│   └── final           [45]        [79]          (80)          [None]
```

Since we received:
- `weekly preps`: 100% of the 5% total weight
- `assignments`: 90% of the 20% total weight

Then:

>`goal` = `weekly preps` + `assignments` + `exams`
> 85% = (100% * 5%) + (90% * 20%) + `exams`
> 85% = (5%) + (18%) + (`exams.goal_percent` * 75%)
> `exams.goal_percent` = 83%

So we will now need 83% on our exams to achieve our 85% goal.

But since `midterm 1` has received its grade, and `midterm 2` has a set goal, then the `final` goal is adjusted to 79%.
