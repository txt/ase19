<a name=top>&nbsp;<p> </a>
[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 

## Homework 4

<em>WARNING! Now things are getting...interesting. This might take 2 weeks to complete. But make you must hand in something each week, even if it is incomplete (else you will lose points).</em>

Using the `Abcd` class, score the performance of

- `ZeroR`
- and `Nb` 

on [weathernom](https://github.com/timm/fun/blob/master/data/weathernon.csv)
and [diabetes](https://github.com/timm/fun/blob/master/data/diabetes.csv).
In all cases:

- Read rows, one at a time
- For each row:
  - If you've already seen, say, 4 rows then make a prediction about the class of the newest row.
  - Always update a `Tbl` with that row (but always remember that, if you are making
    predictions, then do that before the update). Why? Well, this ensures that you
    are not using data from the row to predict for that row.

For sample implementation of this 
see [Abcd1](http://menzies.us/fun/abcd).

### ZeroR

`ZeroR` predicts that the class of the next row is the mode of the classes seen so far.

- A sample `ZeroR` implementation is given at [here](http://menzies.us/fun/zeror).

### NB

`Nb` (Naive Bayes) builds one table for each separate class. So:

- Each time a row is read
- Look at its class
- Ensure that you have a table from that class. That is:
  - If you have _not_ seen that class before, then create a new table.
- Add the new row to the table for that row's class.
- Also, maintain a separate table for "overall"; i.e. each new row
  updates 
  1. One table, just for the class of that row
     - So if the data contains 5 classes, we maintain five tables.
  2. A second table that stores info on all rows
- A sample `Nb` implementation is given at [here](http://menzies.us/fun/nb).
  - The main loop of this `Nb` looks at each row. For each row, it then looks
    at each class table and finds the one that "likes" this row the most.
  - Note that, at its core, this code asks each column of each class how much
    it likes some column of the current row.
  - My code spreads out that `like` implemetnation between 
    [NumLike](http://menzies.us/fun/num#like) 
    and 
    [SymLike](http://menzies.us/fun/sym#like) 
    each row how much it "likes" this

### Output

Your code should print something like the following (and don't worry if the numbers do not exactly match).

Here's `AbcdReport` describing what happens after
`ZeroR` runs over `weathernon` and `diabetes`. In the following,
we read 3 rows before doing any classification.
Note that, `diabetes` that testedpositive is in the minority
so the recalls (pd) and false alarms for this class are very low
(since ZeroR rarely predicts them).

```
#--- zerorok -----------------------

weathernon
    db |    rx |   num |     a |     b |     c |     d |  acc |  pre |   pd |   pf |    f |    g | class
  ---- |  ---- |  ---- |  ---- |  ---- |  ---- |  ---- | ---- | ---- | ---- | ---- | ---- | ---- |-----
  data |    rx |    12 |     6 |     3 |     3 |       | 0.50 | 0.00 | 0.00 | 0.33 | 0.00 | 0.00 | no
  data |    rx |    12 |     0 |     3 |     3 |     6 | 0.50 | 0.67 | 0.67 | 1.00 | 0.67 | 0.00 | yes

diabetes
    db |    rx |   num |     a |     b |     c |     d |  acc |  pre |   pd |   pf |    f |    g | class
  ---- |  ---- |  ---- |  ---- |  ---- |  ---- |  ---- | ---- | ---- | ---- | ---- | ---- | ---- |-----
  data |    rx |   766 |    24 |    25 |   243 |   474 | 0.65 | 0.66 | 0.95 | 0.91 | 0.78 | 0.16 | tested_negative
  data |    rx |   766 |   474 |   243 |    25 |    24 | 0.65 | 0.49 | 0.09 | 0.05 | 0.15 | 0.16 | tested_positive
```

Here's `AbcdReport` describing what happens after
`Nb` runs over `weathernon` and `diabetes`. In the following,
we read 4/20 rows of weathernon/diabetes
before doing any classification. Note now the recall (pd) and
false alarms (pf) for testedpositive and much healthier.

```
#--- nbok -----------------------

weathernon
    db |    rx |   num |     a |     b |     c |     d |  acc |  pre |   pd |   pf |    f |    g | class
  ---- |  ---- |  ---- |  ---- |  ---- |  ---- |  ---- | ---- | ---- | ---- | ---- | ---- | ---- |-----
  data |    rx |    11 |     5 |     2 |     3 |     1 | 0.55 | 0.25 | 0.33 | 0.38 | 0.29 | 0.43 | no
  data |    rx |    11 |     1 |     3 |     2 |     5 | 0.55 | 0.71 | 0.62 | 0.67 | 0.67 | 0.43 | yes

diabetes
    db |    rx |   num |     a |     b |     c |     d |  acc |  pre |   pd |   pf |    f |    g | class
  ---- |  ---- |  ---- |  ---- |  ---- |  ---- |  ---- | ---- | ---- | ---- | ---- | ---- | ---- |-----
  data |    rx |   765 |   176 |   115 |    90 |   384 | 0.73 | 0.81 | 0.77 | 0.34 | 0.79 | 0.71 | tested_negative
  data |    rx |   765 |   384 |    90 |   115 |   176 | 0.73 | 0.60 | 0.66 | 0.23 | 0.63 | 0.71 | tested_positive
```
