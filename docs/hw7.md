<a name=top>&nbsp;<p> </a>

[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 

# Homework 7


Last week you did supervised tree learning on raw attributes.

This week you will do unsupervised tree learning on artifical attributes (random projections).

Next week we'll use that code to implement an optimizer.

## What to do 
Wrote code to recursively cluster data from `xoxo10000` and `pom310000`. Hand in the cluster trees you generate
(as well as all your source code).

Sample output shown here. Your results may different

- [XOMO10000] 
    - [input](../data/xomo10000.csv)
    - [output](../data/xomo10000.txt)
    - Note now the instances in the leaves differ
    - Efforts,  months, defects, risks baseline=  735, 26, 6884, 1
    - Efforts,  months, defects, risks row 190 =  443, 22, 3973, 1

- [POMS310000] 
    - [input](../data/pom310000.csv)
    - [output](../data/pom310000.txt)
    - Note now the instances in the leaves differ
    - Cost,  completion, idle baseline = 830, 0.8. 0.2
    - Cost,  completion, idle row 120 = 270, 0.8. 0.2


## How to do it

### Step1: Distance function

Build a distance function that reports the distance between two rows:

```python
  # "i" and "j" are rows, "cols" are the columns to be used for distance
  # (typically the independent variables) and "p=2"
  def dist(i,j,cols):
    p = THE.row.p
    d = n = 0
    for col in cols:
      n += 1
      d0 = col.dist(i.cells[col.pos], j.cells[col.pos])
      d += d0**p
    return d**(1/p) / n**(1/p) # normalize distance 0..1
```

This will need some way to decide the distance between two values in the same column:

You'll need one for `Sym`bols:

```python
  # "i" is a Sym instance, "x" and "y" and symols, "n=?"
  def dist(i,x,y):
    no = THE.char.skip
    if x is no and y is no: return 1
    if x != y : return 1
    return 0
```

And one for `Num`bers:

```python
  # "i" is a Num instance, "x" and "y" are numbers, "no=?".
  def dist(i,x,y):
    norm = lambda z: (z - i.lo)/(i.hi - i.lo + 10**-32)
    no = THE.char.skip
    if x is no:
      if y is no: return 1
      y = norm(y)
      x = 0 if y > .5 else  1
    else:
      x = norm(x)   
      if y is no:
        y = 0 if x > .5 else  1
      else:
        y = norm(y)
    return abs(x-y)
```

### Step2: find two pivots.

Remember Fastmap? 
- Pick any point at random 
- Find `x` which is something distant from the first point. 
- Find `y` which is distant to `y`. 
- Return x,y and the distance `c` between them.

Note the phrase `distant`. Best not to go for most distant. Instead, 90\% of max is best (this avoids outliers).

### Step3: find two good pivots:

- Repeat Step3 `n=10` times (say) and return the pivots that most seperate the data (data is nearest to half/half closet to `x,y`).

###  Step4: Divide the data 

-  a point `z` falls on a line between `x,y` at distance determined by the cosine rule:

```
def cos(i,x,y,z,c):
  return (i.dist(x,z)**2 + c**2 - i.dist(y,z)**2)/(2*c)
```
- If a point is less than the median value of all the cosine distances, it goes into `left`. Else, it goes to `right`.

### Step5: Recurse
 
- If either half is smaller than some `min` value (i use `sqrt(N)`, then build a table just for that leaf node.
- Else, recurse on both halves.




