<a name=top>&nbsp;<p> </a>
[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 

## Homework 5

Next week, we do decision tree learners that recursive find the best attribute
to split on, then it makes that split, then it recurses on each split.

For this week, we work on how to split on one attribute, supervised by
information in a second.

For the following, reuse (and extend) your `Num` and `Sym` classes.
Also,
it is highly recommended you do Part1 and Part12 before Part3 (and even write them into
separate code files). Otherwise, Part3 will hurt your head.

For all the following, ehre are the split rules:

- Best splits minimize the expected value of entropy/standard deviation after the split
   - But improvements of less that some `trivial=1.025` amount can be ignored.
- Splits need more than `step=sqrt(n)` items (where `n` is the size of the initial distrubution.
- Splits need to made between _different_ x-values
- The mean of adjacent splits has to differ by at least &Epsilon;=`0.3*sd` of the
  standard deviattion of the x-value.
- The first and last split has to be greater than the &Epsilon;

Hints: https://github.com/timm/ase19 has code for splitting just the x-column (not
x and y).

### Part1

```python3
import random
r= random.random
seed=random.seed

def num(i):
  if i<0.4: return [i,     r()*0.1]
  if i<0.6: return [i, 0.4+r()*0.1]
  return           [i, 0.8+r()*0.1]

def x():
  seed(1)
  return  [      r()*0.05 for _ in range(n)] + \
          [0.2 + r()*0.05 for _ in range(n)] +  \
          [0.4 + r()*0.05 for _ in range(n)] +   \
          [0.6 + r()*0.05 for _ in range(n)] +    \
          [0.8 + r()*0.05 for _ in range(n)]

def xnum():
  return  [num(one) for one in x()]
```
The x values run zero to one and group around 0, 0.2, 0.4, 0.6, 0.8.
The associated y-values are grouped around 0.05, 0.45, 0.85 as shown in the `num` function.
For example:

```
[0.006718212205620061, 0.042211657558271734]
[0.042371686846861635, 0.0029040787574867947]
[0.038188730948830706, 0.022169166627303505]
[0.012753451286971085, 0.04378875936505721]
[0.02477175435459705, 0.04958122413818507]
[0.22247455323943693, 0.023308445025757265]
[0.23257964863613817, 0.02308665415409843]
[0.23943616755677566, 0.02187810373376886]
[0.20469297933871175, 0.04596034657377336]
[0.20141737382610034, 0.02897816145904856]
[0.4417882551959935, 0.40214897052659093]
[0.4216383533952527, 0.4837577975662573]
[0.43811400412289714, 0.45564543226524334]
[0.40010530266755556, 0.4642294362932446]
[0.4222693597027401, 0.41859062658947177]
[0.6360770016170391, 0.8992543412176066]
[0.6114381110635226, 0.885994652879529]
[0.647263534777696, 0.8120889959805807]
[0.6450713728805741, 0.8332695185360129]
[0.6015294991516776, 0.8721484407583269]
[0.8012722930496731, 0.871119176969528]
[0.8270706236396749, 0.893644058679946]
[0.8469574581389255, 0.8422106999961416]
[0.8190602118844107, 0.8830035693274327]
[0.8108299698565307, 0.8670305566414072]
```

Write code that splits the x-column to minimize the expected value 
of the standard deviation in the y-column
after the split. The top-level call to that code should  be:

	Div2_1(lst,x=first, y=last)

where `lst` is a list of anything at all and `x,y`  are functions
that extract the x-y pairs from each item in `lst`. Fyi, my `x,y`
functions extract the first and last value in each list item.

Test this code on the above data.

When I run it, I get three splits (and your results may vary).

```
1 x.n    9 | x.lo 0.01275 x.hi 0.23944 | y.lo 0.00290 y.hi 0.0496
2 x.n    5 | x.lo 0.40011 x.hi 0.44179 | y.lo 0.40215 y.hi 0.4838
3 x.n   10 | x.lo 0.60153 x.hi 0.84696 | y.lo 0.81209 y.hi 0.8993


## Part2

Here is code is that generates numeric x-values and symbolic y-values

```python
def xsym():
  return  [sym(one) for one in x()] * 5

def sym(i):
  if i<0.4: return [i, "a"]
  if i<0.6: return [i, "b"]
  return           [i, "c"]

def x():
  seed(1)
  return  [      r()*0.05 for _ in range(n)] + \
          [0.2 + r()*0.05 for _ in range(n)] +  \
          [0.4 + r()*0.05 for _ in range(n)] +   \
          [0.6 + r()*0.05 for _ in range(n)] +    \
          [0.8 + r()*0.05 for _ in range(n)]
```

As before,
the x values run zero to one and group around 0, 0.2, 0.4, 0.6, 0.8.
The associated y-values are the symbols a,b,c grouped around 0.2, 0.5, and 0.8 respectively.
For example:


```
[0.006718212205620061, 'a']
[0.042371686846861635, 'a']
[0.038188730948830706, 'a']
[0.012753451286971085, 'a']
[0.02477175435459705, 'a']
[0.22247455323943693, 'a']
[0.23257964863613817, 'a']
[0.23943616755677566, 'a']
[0.20469297933871175, 'a']
[0.20141737382610034, 'a']
[0.4417882551959935, 'b']
[0.4216383533952527, 'b']
[0.43811400412289714, 'b']
[0.40010530266755556, 'b']
[0.4222693597027401, 'b']
[0.6360770016170391, 'c']
[0.6114381110635226, 'c']
[0.647263534777696, 'c']
[0.6450713728805741, 'c']
[0.6015294991516776, 'c']
[0.8012722930496731, 'c']
[0.8270706236396749, 'c']
[0.8469574581389255, 'c']
[0.8190602118844107, 'c']
[0.8108299698565307, 'c']
[0.006718212205620061, 'a']
[0.042371686846861635, 'a']
[0.038188730948830706, 'a']
[0.012753451286971085, 'a']
[0.02477175435459705, 'a']
[0.22247455323943693, 'a']
[0.23257964863613817, 'a']
[0.23943616755677566, 'a']
[0.20469297933871175, 'a']
[0.20141737382610034, 'a']
[0.4417882551959935, 'b']
[0.4216383533952527, 'b']
[0.43811400412289714, 'b']
[0.40010530266755556, 'b']
[0.4222693597027401, 'b']
[0.6360770016170391, 'c']
[0.6114381110635226, 'c']
[0.647263534777696, 'c']
[0.6450713728805741, 'c']
[0.6015294991516776, 'c']
[0.8012722930496731, 'c']
[0.8270706236396749, 'c']
[0.8469574581389255, 'c']
[0.8190602118844107, 'c']
[0.8108299698565307, 'c']
[0.006718212205620061, 'a']
[0.042371686846861635, 'a']
[0.038188730948830706, 'a']
[0.012753451286971085, 'a']
[0.02477175435459705, 'a']
[0.22247455323943693, 'a']
[0.23257964863613817, 'a']
[0.23943616755677566, 'a']
[0.20469297933871175, 'a']
[0.20141737382610034, 'a']
[0.4417882551959935, 'b']
[0.4216383533952527, 'b']
[0.43811400412289714, 'b']
[0.40010530266755556, 'b']
[0.4222693597027401, 'b']
[0.6360770016170391, 'c']
[0.6114381110635226, 'c']
[0.647263534777696, 'c']
[0.6450713728805741, 'c']
[0.6015294991516776, 'c']
[0.8012722930496731, 'c']
[0.8270706236396749, 'c']
[0.8469574581389255, 'c']
[0.8190602118844107, 'c']
[0.8108299698565307, 'c']
[0.006718212205620061, 'a']
[0.042371686846861635, 'a']
[0.038188730948830706, 'a']
[0.012753451286971085, 'a']
[0.02477175435459705, 'a']
[0.22247455323943693, 'a']
[0.23257964863613817, 'a']
[0.23943616755677566, 'a']
[0.20469297933871175, 'a']
[0.20141737382610034, 'a']
[0.4417882551959935, 'b']
[0.4216383533952527, 'b']
[0.43811400412289714, 'b']
[0.40010530266755556, 'b']
[0.4222693597027401, 'b']
[0.6360770016170391, 'c']
[0.6114381110635226, 'c']
[0.647263534777696, 'c']
[0.6450713728805741, 'c']
[0.6015294991516776, 'c']
[0.8012722930496731, 'c']
[0.8270706236396749, 'c']
[0.8469574581389255, 'c']
[0.8190602118844107, 'c']
[0.8108299698565307, 'c']
[0.006718212205620061, 'a']
[0.042371686846861635, 'a']
[0.038188730948830706, 'a']
[0.012753451286971085, 'a']
[0.02477175435459705, 'a']
[0.22247455323943693, 'a']
[0.23257964863613817, 'a']
[0.23943616755677566, 'a']
[0.20469297933871175, 'a']
[0.20141737382610034, 'a']
[0.4417882551959935, 'b']
[0.4216383533952527, 'b']
[0.43811400412289714, 'b']
[0.40010530266755556, 'b']
[0.4222693597027401, 'b']
[0.6360770016170391, 'c']
[0.6114381110635226, 'c']
[0.647263534777696, 'c']
[0.6450713728805741, 'c']
[0.6015294991516776, 'c']
[0.8012722930496731, 'c']
[0.8270706236396749, 'c']
[0.8469574581389255, 'c']
[0.8190602118844107, 'c']
[0.8108299698565307, 'c']
```

Write code that splits the x-column to minimize the expected value ofthe entropy 
in the y-column,
after the split. The top-level call to that code should  be:

	Div2_2lst,x=first, y=last)

Test this on the above data. When I run this, I get tree splits (and you results may vary):

```
1 x.n   49 | x.lo 0.00672 x.hi 0.23944 | y.mode a y.ent 0.0000
2 x.n   25 | x.lo 0.40011 x.hi 0.44179 | y.mode b y.ent 0.0000
3 x.n   50 | x.lo 0.60153 x.hi 0.84696 | y.mode c y.ent 0.0000
```


## Part3

Implement part2 and Part2 in the same code base where `Div2` accepts another argument (the type of the y-column).

If successful, then the above two examples should run as follows:

	Div2lst,x=first, y=last,yis=Num) # for part1
	Div2lst,x=first, y=last,yis=Sym) # for part2

