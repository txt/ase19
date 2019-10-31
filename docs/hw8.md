<a name=top>&nbsp;<p> </a>

[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 

# Homework 8


Last week you did divided up decision space (unsupervised recursive partitioning of the independent variables).

This week you will learn deltas in the objective (a.k.a. goal) space.

## Step1: divide decision space (done! see last week)

## Step2: find centroids

- Mean/mode of independent variables

## Step3: Envy

For each leaf cluster, find out who you envy. 
    We  envy things that are close by and which are much better than us


For each pair of centroids _(C1,C2)_:

- Let &Delta; = Compute the delta between their  independent variables for _C1,C2_ 
  - using the distance calculations from last week
supervised tree learning on raw attributes.
- Let &epsilon; = How much  times this centroid's goals _dominate_ the other centroids
- Engineering tip: express both those numbers as ratios of zero to one
    - So divide &Delta; by sqrt(number of independent attributes)
    - So normalize _&epsilon;(C1,C2)_ by divide it by the sum of all &epsilon;_(C1,Cx)_ where _Cx_ are all the other centroids in from the cluster tree.
- Envy can now be calculated  many ways  
    - We will use _envy = (1-&Delta;) - &epsilon;_
       - The minus sign on &epsilon; comes from below.

To compute domination:

- Modify your table class so it knows about goals we want to minimize and maximize. Anything column marked
 with "<,>"  gets a wright of -1,1 and denotes goals you want to minimize,maximize.
  - Engineering tip: 
    - Give each column a default weight of 1, in the `__init__` method
    - Only for the columns with `<` do you need to change that to -1
- Add a function that returns true if one set of goals is better than another. 
  - Engineering tip: Best way to do this is reflect on the delta in the value
of each goal, raised to a power (see below). WARNING: normalize the goals 0..1
    before raising to a power. Otherwise, it will blow up!
  - The official domination predicate is `i` dominates `j` when _s1/n < s2/n_.
    So large negative numbers are better! Your code needs to handle that.


```python
def dominates(i,j,goals): # i and j are rows.
    z = 0.00001
    s1, s2, n = z,z,z+len(goals)
    for goal in goals:
      a,b = i.cells[goal.pos], j.cells[goal.pos]
      a,b = goal.norm(a), goal.norm(b)  
      s1 -= 10**(goal.w * (a-b)/n)
      s2 -= 10**(goal.w * (b-a)/n)
    return s1/n - s2/n # i is better if it losses least (i.e. this number under 0)
```

## Check your Domination Predicate

For the [auto.csv](../data/auto.csv) data, sort each row by

- picking 100 randomly selected other rows.
- Count how often this row `i` has dominates(i,j) <0` with the other 100 rows
- Sort this rows by that count

Hand in the first 4 and the last 4 rows in that sort. You should be seeing  something like the following
(i.e.  the best rws have lowest weight , faster acceleration, longest miles per hour).


|      |cylinder&nbsp;| displacmnt&nbsp;| hpower&nbsp;| <weight&nbsp;| >acceltn&nbsp;| model&nbsp;| origin&nbsp;| >mpg|
|------|--------|----------|-------|-------|---------|------|------|-------|
|best |4       | >85       | <46   | 1975  |  19.4   |  >81 |  3   |   40  |
|best |4       | >85       | <65   | 1985  |  21.5   |  >78 |  2   |   40  |
|best |4       | >85       | <65   | 2085  |  21.7   |  >80 |  2   |   40  |
|best |4       | >96       | <65   | 2130  |  24.6   |  >82 |  2   |   40  |
|..  .|...     | ...       | ...   | ...   |  ..     |  ... |  ... |   ... |
|worst|8       | >383      | >165  | 4746  |  12     |  <71 |  1   |   10  |
|worst|8       | >3835     | >165  | 4951  |  11     |  <73 |  1   |   10  |
|worst|8       | >383      | >165  | 4952  |  11.5   |  <73 |  1   |   10  |
|worst|8       | >383      | >165  | 4955  |  11.5   |  <71 |  1   |   10  |
|     |        |           |       | minimize| maximize|    |       | maximize      |

## Learn a Contrast Set

For each cluster, build a two class data set:

- class1= this cluster
- class2= the cluster you most envy

Learn a decision tree that seperates the two clusters.

Hand in the print out of the trees

Comment: good knowledge is succinct knowledge. Are the trees generated in this way "good"?

## Comment on Local vs Global Reasoning:

You have just built a local reasoner that produces N different models for each N clusters.

The opposite approach would be to build one global by, say:

- Rank each row by how much it dominates everyone else
- Build a two class system: one for the best 20% rows, one for the 80% rest
- Learn a tree from those classes


The great philosopher of knowledge Rui Shu, has comments on the value 
of local vs global reasoning in 
[sections 2.1 and 2,2](../etc/img/rui.pdf). Read those sections and write about a page of ascii text commenting on the value (or otherwise) of your local reasoner. Feel free with disagree with Rui. After all, he only did this class a year ago.


