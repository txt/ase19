<a name=top>&nbsp;<p> </a>
[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 

## Homework 6

This week we build a single tree learner.

- Why do I say simple? 
- Well, to see how the grown ups do it, see [here](http://washstat.org/presentations/20150604/loh_slides.pdf) and [here](http://pages.stat.wisc.edu/~loh/treeprogs/guide/LohISI14.pdf)
  - Like I say, we're going to keep it simple.

Now that you know how to do supervised discretization on one attribute:

- do it for all
- sort the attributes by how well they separate the class variable
- find the best attribute on that sort
- divide the data on the ranges of that attribute.
- Recurse on each division.

For example, on the [diabetes.csv](../data/diabetes.csv) data set, I  get the following (note that your results may differ; e.g. i don't
prune away subtrees that lead to the same conclusion... but you could if you wanted too)

```
$plas = -inf .. 120 *
|   $mass = -inf .. 26 
|   |   $plas = -inf .. 105 * : tested_negative (80)
|   |   $plas = 105 .. inf  : tested_negative (38)
|   $mass = 26 .. inf *
|   |   $age = -inf .. 28 *
|   |   |   $mass = -inf .. 30.8  : tested_negative (58)
|   |   |   $mass = 30.8 .. inf *
|   |   |   |   $pres = -inf .. 80 *
|   |   |   |   |   $pedi = -inf .. 0.471 * : tested_negative (56)
|   |   |   |   |   $pedi = 0.471 .. inf  : tested_negative (37)
|   |   |   |   $pres = 80 .. inf  : tested_negative (10)
|   |   $age = 28 .. inf 
|   |   |   $plas = -inf .. 89  : tested_negative (32)
|   |   |   $plas = 89 .. inf *
|   |   |   |   $preg = -inf .. 6 *
|   |   |   |   |   $pres = -inf .. 88 * : tested_negative (59)
|   |   |   |   |   $pres = 88 .. inf  : tested_negative (9)
|   |   |   |   $preg = 6 .. inf  : tested_positive (40)
$plas = 120 .. inf 
|   $plas = -inf .. 154 *
|   |   $mass = -inf .. 26.1  : tested_negative (29)
|   |   $mass = 26.1 .. inf *
|   |   |   $age = -inf .. 24  : tested_negative (39)
|   |   |   $age = 24 .. inf *
|   |   |   |   $pedi = -inf .. 0.512 *
|   |   |   |   |   $mass = -inf .. 39 *
|   |   |   |   |   |   $age = -inf .. 40 * : tested_negative (50)
|   |   |   |   |   |   $age = 40 .. inf  : tested_positive (33)
|   |   |   |   |   $mass = 39 .. inf  : tested_positive (15)
|   |   |   |   $pedi = 0.512 .. inf 
|   |   |   |   |   $age = -inf .. 29  : tested_negative (18)
|   |   |   |   |   $age = 29 .. inf * : tested_positive (43)
|   $plas = 154 .. inf 
|   |   $pedi = -inf .. 0.326  : tested_positive (44)
|   |   $pedi = 0.326 .. inf *
|   |   |   $pres = -inf .. 76 * : tested_positive (47)
|   |   |   $pres = 76 .. inf  : tested_positive (31)
```

For example, on the [auto.csv](../data/auto.csv) data set, we get:

```
$displacement = -inf .. 151 *
|   $horsepower = -inf .. 70 
|   |   cylinders = 4 *
|   |   |   $model = -inf .. 76  : 29.2 (23)
|   |   |   $model = 76 .. inf *
|   |   |   |   $displacement = -inf .. 91 * : 37.39 (28)
|   |   |   |   $displacement = 91 .. inf  : 33.45 (19)
|   |   cylinders = 5  : 36.4 (1)
|   $horsepower = 70 .. inf *
|   |   cylinders = 3  : 20.55 (4)
|   |   cylinders = 4 *
|   |   |   $model = -inf .. 78 *
|   |   |   |   $weight = -inf .. 2219  : 28.25 (20)
|   |   |   |   $weight = 2219 .. inf *
|   |   |   |   |   $weight = -inf .. 2300  : 25.48 (18)
|   |   |   |   |   $weight = 2300 .. inf *
|   |   |   |   |   |   $weight = -inf .. 2855 * : 23.61 (36)
|   |   |   |   |   |   $weight = 2855 .. inf  : 20.29 (7)
|   |   |   $model = 78 .. inf 
|   |   |   |   $weight = -inf .. 2434  : 34.36 (17)
|   |   |   |   $weight = 2434 .. inf * : 28.56 (27)
|   |   cylinders = 5  : 20.3 (1)
|   |   cylinders = 6  : 25.63 (3)
$displacement = 151 .. inf 
|   cylinders = 4  : 25.73 (4)
|   cylinders = 5  : 25.4 (1)
|   cylinders = 6 
|   |   origin = 1 *
|   |   |   $model = -inf .. 78 *
|   |   |   |   $displacement = -inf .. 200  : 20.81 (13)
|   |   |   |   $displacement = 200 .. inf *
|   |   |   |   |   $displacement = -inf .. 232 * : 19.12 (25)
|   |   |   |   |   $displacement = 232 .. inf  : 17.32 (22)
|   |   |   $model = 78 .. inf  : 23.25 (14)
|   |   origin = 2  : 16.57 (3)
|   |   origin = 3  : 24.28 (4)
|   cylinders = 8 *
|   |   $model = -inf .. 76 *
|   |   |   $weight = -inf .. 3609  : 16.0 (10)
|   |   |   $weight = 3609 .. inf *
|   |   |   |   $weight = -inf .. 4341 * : 14.26 (36)
|   |   |   |   $weight = 4341 .. inf  : 12.89 (32)
|   |   $model = 76 .. inf  : 18.21 (25)
```

So, your task:

1. do it for decision trees (symbolic classes in the leaves)
2. do it for regression trees (numeric values in the leaves)
3. write one algorithm that does it for both
   - If you are brave, you'll just do this 3rd part
   - If you are humble, you do it one at a time, then refactor the two separate implementations into the third one.
4. Hand in all the code in the usual way (github). Include files showing the output trees.

## Code tips


My tree learner are methods inside my `Tbl` class.

- And the difference between decision trees and regression trees is very small:


```python
  def decisionTree(i):
     return i.tree(i.rows,
                  y   = lambda z: z.cells[i.cols.klass.pos],
                  yis = Sym)
  def regressionTree(i):
     return i.tree(i.rows,
                  y   = lambda z: last(z.cells),
                  yis = Num)
```

Here's my tree learner. 

- I don't sort all the attributes and their cuts (too much memory). Instead, I just keep the best one seen so far
- When splitting, I call tree recursively to build the kids
  - And for that recursion, I iterate over all the cuts found in my best column
```python
  def tree(i,lst,y,yis,lvl=0):
    if len(lst) >= THE.tree.minObs*2:
      # find the best column
      lo, cut, col = 10**32, None, None
      for col1 in i.cols.indep:
        x = lambda row: row.cells[col1.pos]
        cut1, lo1 = col1.div(lst, x=x, y=y, yis=yis)
        if cut1:
          if lo1 < lo:
            cut, lo, col = cut1, lo1, col1
      # if a cut exists
      if cut:
        # split data on best col, call i.tree on each split
        x = lambda row: row.cells[col.pos]
        return [o(lo   = lo,
                  hi   = hi,
                  n    = len(kids),
                  txt  = col.txt,
                  kids = i.tree(kids,y,yis,lvl+1)
                ) for lo,hi,kids in col.split(lst, x, cut)]
    return yis(lst,key=y)
```

Debugging tip #1

- See the `lvl` argument in `tree`? 
- incremented on each recursive call
- If used in a  print statement, you can watch your tree growth working, or growing out of control.

Debugging tip #2:

- Write a tree print utility FIRST since you will be using it all the time during debugging.

```python
def showt(tree,pre= '',rnd=THE.tree.rnd):
  most = sorted(x.n for x in tree)[-1]
  for x  in tree:
    after =""
    s = x.txt + ' = ' + str(x.lo)
    if x.n == most:
      after,most = "*", None
    if x.lo != x.hi:
      s += ' .. ' + str(x.hi)
    if isa(x.kids,Thing):
       print(pre + s,after,
             ":",x.kids.middle(rnd),
            '('+str(x.kids.n) +')')
    else:
       print(pre + s,after)
       showt(x.kids,pre + '|   ')
```
## Some engineering tips:

- Column column values many be "?". Be careful never to make them splitters.
- For part3 (one code base that does decision trees or regression trees)
    - I added a `variety` method to  my `Num` and `Sym` class 
      - Num.variety = standard deviation
      - Sym.variety = entropy
    - I have a `trivial=1.05` variable that tells me when variety reduction is some proposed splits is only trivially better than the _Prior_ variety that was `best` before:
      - i.e. trivial if 	`new.variety*trivial < prior`
- For tree learning:
  - I have a `minObs=4` variable that tells me when there are too few data points to merit splitting the data into subtrees
  - To rank sort columns (to find the thing that is best to split on), I have a `div` method that is different for `Num` and `Sym`:
    - The '`Num` div does the supervised descritzation for each column, then returns the expected value of `variety` after the split
     - The `Sym` div builds on `Sym` or `Num` object for each unique value in each column. So if we are doing regression trees and the column has values "yes" and "no"
       - "yes" has a `Num` object storing that `variety` of the target class when for the rows with "yes" in this column
       - "yes" has a `Num` object storing that `variety` of the target class when for the rows with "no" in this column
       - Note:`Sym.div` is optional for this homework. Feel free to ony andle classes with numeric data
  - I used a  `Range` object that has `lo` and `hi` bounds that are initialized to negative and positive infinity
    - Can you see the use of that object in the tree, above?
    - These have their own print methods (`__repr__` for Python programmers), sot he tree can print easy
- For column discretization
  - I have a `min=0.5` variable that tells me when to stop splitting the numeric independent variables (so a split has to have at least _N<sup>min</sup>_ rows from _N_ rows in total)
  - I have a `cohen=0.3` variable that tells me when to stop splitting the n of one split is not different to the next one.
    - So the means have to be different by more than `sd*cohen`.


