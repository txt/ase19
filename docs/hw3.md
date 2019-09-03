<a name=top>&nbsp;<p> </a>
[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 

## Homework 3

Here's the new work (in red)

<img src="http://yuml.me/diagram/plain;dir:lr/class/[Tbl|oid|read(file); dump();]++rows-1..*[Row|oid; cells:list; cooked:list; dom = 0],[Tbl]++cols-1..*[Col|oid; col; txt ], [Col]^-[Num| hi = -10^32 ; lo = 10^32 ; m2 = 0; mu = 0; n = 0; sd = 0; |Num1()],[Col]-[note: one Sym or Num for each column in the rows{bg:orange}], [Col]^-[Sym|n=0;mode;most; cnt: Dict|SymEnt(){bg:red}],[Sym]-[note:entropy is analagous to standard deviation{bg:orange}],[Abcd|rx;data;a;b;c;d;yes=0;no=0;known;{bg:red}],[Abcd]-[note: reports performance results when a classifeis tested{bg:orange}]">

Implement new classes 
[Abcd](http://menzies.us/fun/abcd) and
[Sym](http://menzies.us/fun/sym) 

- Don't worry about `SymAny` or `SymLike` (for this week, anyway).

Also, modify `Tbl` so columns can be `Num` or `Sym`s.

### Task2: new class = Abcd

`Abcd` is a class to report test results for a classifier. It knows how to report accuracy, false alarms, precision,
recall, the f-measure, and the g-measurea

- For notes on these measures, see [eval101][(eval101.md).
-  For  sample implementation, see [Abcd](http://menzies.us/fun/abcd).
- The code is a little tricky since false alarm, precision, recall, f, g are only defined for binary classifiers. If dealing
  with more than two classes, you have to divide those into N binary problems:
  - classA and notClassA,
  - classB and notClassB,
  - etc
- Also, there's one interesting catch. The first time we see a new class, that means that in all times before now
  we did not see that class. So the `a` counter has to be updated to the count up to now (see
  [Abcd](http://menzies.us/fun/abcd) for details).
 
To test your code, then something like this:

```
function _abcd(f,i,j) {
  Abcd(i)
  for(j=1; j<=6; j++) Abcd1(i,"yes", "yes")
  for(j=1; j<=2; j++) Abcd1(i,"no",  "no")
  for(j=1; j<=5; j++) Abcd1(i,"maybe",  "maybe")
  Abcd1(i, "maybe","no")
  AbcdReport(i)
}
```

Should print something like this:

```
   db |    rx |   num |     a |     b |     c |     d |  acc |  pre |   pd |   pf |    f |    g | class
  ---- |  ---- |  ---- |  ---- |  ---- |  ---- |  ---- | ---- | ---- | ---- | ---- | ---- | ---- |-----
  data |    rx |    14 |    11 |       |     1 |     2 | 0.93 | 0.67 | 1.00 | 0.08 | 0.80 | 0.96 | no
  data |    rx |    14 |     8 |       |       |     6 | 0.93 | 1.00 | 1.00 | 0.00 | 1.00 | 1.00 | yes
  data |    rx |    14 |     8 |     1 |       |     5 | 0.93 | 1.00 | 0.83 | 0.00 | 0.91 | 0.91 | maybe
```

### Task1: new class = Sym

`Sym` is like `Num`, but it keeps a count `cnt` of symbols in a row. 

- The most frequently seen symbol is the `mode`.
- `Sym` can report the `entropy` of the symbols  in a column. Given `n` entries n a column
    with symbols occuring at frequency `f1,f2,...`
     then the entropy `e` of a column is:
  - p<sub>i</sub> = f<sub>i</sub>/n
  - e = - &sum;<sub>i</sub> p<sub>i</sub>log<sub>2</sub>(p<sub>i</sub>)
  - For code to calculate this, see `SymEnt` in [sym.fun](http://menzies.us/fun/sym),
  - Entropy is like standard deviation, but for symbols:
    - the lower the standard deviation, the less variety in the numbers
    - the lower the entropy, the less variety in the symbols

To test your code:

- If your throw the letters aaaabbc into your `Sym` then the entropy should be around 1.38.

### Task3: modify class `Tbl`

Last week you built a table class that only knew about numeric columns. 

Now you need to code up a little  language for  row1 of your data to identify column types.

That language used the following symbols (in regualr expression format):

```
SKIPCOL = "\\?"
NUMCOL  = "[<>\\$]"
GOALCOL = "[<>!]"
LESS    = "<"
```

That is:

-  Any column name containing "?" will be skipped over. 
- Any column name containing "<" or ">" or "$"  will be called
a `Num`  
  - And all other columns will be `Sym`s,
- Any column name containing "<" or ">" or "!" will be called a goal. 
  - "<" and ">" are "less" or "more" goals; i.e. things we want to minimize or maximize
  - "!" and `Sym` columns that are classes that we want to predict.
  - Anyying that does not use "<>!" is a `xs` column
- All columns will be given a weight of `w=1`
  - Unless that column name includes "<" in which case `w=-1`.

For example:

```
outlook, ?$temp,  <humid, wind, !play
rainy, 68, 80, FALSE, yes # comments
sunny, 85, 85,  FALSE, no
sunny, 80, 90, TRUE, no
overcast, 83, 86, FALSE, yes
rainy, 70, 96, FALSE, yes
rainy, 65, 70, TRUE, no
overcast, 64, 65, TRUE, yes
sunny, 72, 95, FALSE, no
sunny, 69, 70, FALSE, yes
rainy, 75, 80, FALSE, yes
sunny, 75, 70, TRUE, yes
overcast, 72, 90, TRUE, yes
overcast, 81, 75, FALSE, yes
rainy, 71, 91, TRUE, no
```

- Goals are columns 3,5
- Xs are columns 1,4
- Column 1 and Column 4 and Column 5  are   `Sym`s
- Columns 3 is a Num,
- Column 2 will be ignore.
- Columns 3 is a goal to be minimized and will have a weight of -1.

To test your code:

- Read the weather data shown above.
- For the first line, create a `cols` list of `Num`s and `Sym`s.
- Also create lists `my.goals, my.xs, my.nums, my.syms` etc storing indexes of the columns
- Print `cols` and `my`. In a language where arrays are indexed 1...max, that looks like the following.
  - Your results should be nearly the same OR you can find a  bug in my code that printed the following.

```python
t.cols
|  1
|  |  add: Sym1
|  |  cnt
|  |  |  overcast: 4
|  |  |  rainy: 5
|  |  |  sunny: 5
|  |  col: 1
|  |  mode: sunny
|  |  most: 5
|  |  n: 14
|  |  oid: 2
|  |  txt: outlook
|  3
|  |  add: Num1
|  |  col: 3
|  |  hi: 96
|  |  lo: 65
|  |  m2: 1375.21
|  |  mu: 81.6429
|  |  n: 14
|  |  oid: 3
|  |  sd: 10.2852
|  |  txt: <humid
|  4
|  |  add: Sym1
|  |  cnt
|  |  |  FALSE: 8
|  |  |  TRUE: 6
|  |  col: 4
|  |  mode: FALSE
|  |  most: 8
|  |  n: 14
|  |  oid: 4
|  |  txt: wind
|  5
|  |  add: Sym1
|  |  cnt
|  |  |  no: 5
|  |  |  yes: 9
|  |  col: 5
|  |  mode: yes
|  |  most: 9
|  |  n: 14
|  |  oid: 5
|  |  txt: !play
t.my
|  class: 5
|  goals
|  |  3
|  |  5
|  nums
|  |  3
|  syms
|  |  1
|  |  4
|  |  5
|  w
|  |  3: -1
|  xnums
|  xs
|  |  1
|  |  4
|  xsyms
|  |  1
|  |  4
```



