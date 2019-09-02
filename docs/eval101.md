<a name=top>&nbsp;<p> </a>
[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 



# Evalaution (101)

Sometimes you can achieve on one goal and fail on another.
So 

- not everything wins on every goal
- the goals we set determines the conclusions we condone.

But what are the goals often seen in practice?

## Numeric Goals

- residual = RE = predicted - actual
- magnitude of RE = MRE= abs(predicted - actual)
- PRED(N) = how may estimates are less than N
     - e.g. PRED(30) is standard (how many estimates within 30% of actual)
- medianRE = median of lots of RE
- meanRE = mean of lots of RE (not recommended)

Some argue that these numbers need to be baselined as a ratio against "do
the dumbest thing you can":

- let `y` = mean of the training set
-  let `x` = your numeric estimate from the more
- _Standardised accuracy_ = (1- x/y) * 100
    - Larger values are better

![](../etc/img/rank101.png)

## Discrete goals

(For code to implment the following, see [abcd.lua](http://menzies.us/lean/abcd.lua).

Consdier the output stream,

```
%are you a dog?
 predicted truth
 --------- -----
 yes       no
 yes       yes
 no        no
 yes       yes
 no        no
 ...       ...
```
Note that somethimes `dog`s are correctly predicted and sometimes
they ain't (line one).

How do we convert these pairs into evaluation measures?

Discrete detectors can be assessed according to the following measures:

```
+-------------+------------+
|           truth          |
|     no            yes    |
+-------------+------------+
|      a      |      b     | classifer predicts = no
+-------------+------------+
|      c      |      d     | classifier predicts = yes
+-------------+------------+
```

- accuracy                   = acc          = (a+d)/(a+b+c+d
- probability of detection   = pd  = recall = d/(b+d)
- probability of false alarm = pf           = c/(a+c)
- precision                  = prec         = d/(c+d)
- distance2heaven            = d2h          = sqrt( (1-pd)^2 + pf^2 )
- pos/neg                    =              = (b+d) / (a+c)

(We'll use pos/neg later on, see below.)

```
 no,  yes,   <-- classified as
 120,  20,   no   
  20,  20,   yes
```

For more that two classes, need to build one table per class of
e.g. (a,nota), (b,notb), (c,notc) then report seperately for each.

```
 a,   b,    c,  <-- classifieed as
50,  10,    5,  a
 5,  80,   10,  b
20,  30,  100,  c
```

### Ideally...

Ideally, detectors have high PDs, low PFs, and low
 effort. This ideal state rarely happens:
 
- PD and effort are linked. The more modules that trigger
 the detector, the higher the PD. However, effort also gets
 increases
- High PD or low PF comes at the cost of high PF or low PD
(respectively). 

These links can be seen in a standard
receiver operator curve (ROC).  Suppose, for example, 
LOC&lt;x
is used as the detector (i.e. we assume large modules have
more errors). LOC&lt;x represents a family of detectors:

- At
x=0, EVERY module is predicted to have errors. This detector
has a high PD but also a high false alarm rate. 
- At x=0, NO
module is predicted to have errors. This detector has a low
false alarm rate but won't detect anything at all. At 0&lt;x&lt;1,
a set of detectors are generated as shown below:

```
        pd
      1 |           x  x  x     KEY:
        |        x     .         "."  denotes the line PD=PF
        |     x      .           "x"  denotes the roc curve 
        |   x      .                  for a set of detectors
        |  x     .
        | x    . 
        | x  .
        |x .
        |x
        x------------------ pf    
       0                   1
```

Note that:

- The only way to make no mistakes (PF=0) is to do nothing (PD=0)
- The only way to catch more detects is to make more
mistakes (increasing PD means increasing PF).
- Our detector bends towards the "sweet spot" of
<PD=1,PF=0> but does not reach it.
- The line pf=pd on the above graph represents the "no information"
line. If pf=pd then the detector is pretty useless. The better
the detector, the more it rises above PF=PD towards the "sweet spot".

For more on the connection of pd,pf,precision, etc, see
[Problems with Precision](http://menzies.us/pdf/07precision.pdf)
where it is derived that

```
pf = pos / neg * (1-prec)/prec * recall
```

![](../etc/img/versus.png)

## Special Measures for SE

Softare engineering, we might have some other measures.

### IFA

In 2011,
[Parnin and Orso](https://www.cc.gatech.edu/home/orso/papers/parnin.orso.ISSTA11.pdf)
noted that developers are not using debugging tools since they
grow impatient when they generate false alarms. 

So one measure of success of a defect predictor is to minimize
`IFA` (see section V of [Supervised vs Unsupervised
Models: A Holistic Look at Effort-Aware Just-in-Time Defect
Prediction](https://xin-xia.github.io/publication/icsme173.pdf));
i.e.  number of initial false alarms encountered before we find the
first defect.

### Popt(20)

Another measure of success is "how little do you need to read to find
most bugs". The usual rule is you want find 20% of the code to find
80% of the defects.

For exaple, if we know how many locs of code are seen in the methods
in the above cells `a,b,c,d`, then we can define how many lines of
code we need to read to find the bugs (and our goal is read _less_
and find _more_ bugs):

- build a defect predictor
- find the code where the prediction = yes, no
- Build `S(m)` as follows: 
    - `tmp1` = sort the yes _ascending_ on lines of code
    - `S(m)` = sort the no _ascending_ on lines of code, append to `tmp1`
- Build `S(worst)` as follows:
    - `tmp2` = sort the yes _descending_ on lines of code
    - `S(worst)` = sort the no _descedning_ on lines of code, append to `tmp2`
- Build `S(optimial)` as follows:
    - Sort all code _descending_ on number of defects
- Walk the curves left to right, recording what defects we find
- `Popt = 1 - ( S(optimal) - S(m) ) / (S(optional) - S(worst) ) `
- Usually, we report the recall when Popt = 20%

![](../etc/img/auc2.png)

### Multi-Obejctive Goals


Different business contexts need different goals.

So what we need are goal-aware learners.

End data mining.

Begin multi-objective optimization.


