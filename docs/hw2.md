<a name=top>&nbsp;<p> </a>
[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 

## Homework 2

<img src="http://yuml.me/diagram/plain;dir:lr/class/[Tbl|oid|read(file); dump();]++rows-1..*[Row|oid; cells:list; cooked:list; dom = 0],[Tbl]++cols-1..*[Num|oid; col; hi; lo; m2; mu; n; sd; txt|Num1()],[Num]-[note: one Num for each column in the rows{bg:beige}s])">

Create a class `Tbl` `Col` `Row` (and reuse
`Num` from last time):

- `Tbl`s has many rows, which is a list of `Row`
- `Tbl`s read _named csv_ files (\*). 
    - The first line is a list of column names
    - The other lines are data that we will read and store as `Row`s in the `Tbl`s
- `Tbl`s hold a list of `cols` (one for each column in the `rows')
    - Every `Col` knows
- Whenever a line from the csv is added to a `Tbl`, then:
    - It becomes a `Row` in `Tbl`
    - And all the `Num`s in the `cols` are updates
- `Rows` keep a list of `cells` and another list called `cooked` that we won't talk about now.
- All objects have a unique id `oid`.

The input to this is a named csv file, e.g.
[weathernum](https://raw.githubusercontent.com/timm/fun/master/data/weathernum.csv).

The output is a `Tbl` with a structure like this:


```
t.cols
|  1
|  |  add: Num1
|  |  col: 1
|  |  hi: 100
|  |  lo: 0
|  |  m2: 25635.7
|  |  mu: 52.1429
|  |  n: 14
|  |  oid: 2
|  |  sd: 44.407
|  |  txt: $cloudCover
|  2
|  |  add: Num1
|  |  col: 2
|  |  hi: 85
|  |  lo: 64
|  |  m2: 561.429
|  |  mu: 73.5714
|  |  n: 14
|  |  oid: 3
|  |  sd: 6.57167
|  |  txt: $temp
|  3
|  |  add: Num1
|  |  col: 3
|  |  hi: 96
|  |  lo: 65
|  |  m2: 1375.21
|  |  mu: 81.6429
|  |  n: 14
|  |  oid: 4
|  |  sd: 10.2852
|  |  txt: $humid
|  4
|  |  add: Num1
|  |  col: 4
|  |  hi: 20
|  |  lo: 0
|  |  m2: 820.857
|  |  mu: 6.28571
|  |  n: 14
|  |  oid: 5
|  |  sd: 7.94625
|  |  txt: $wind
|  5
|  |  add: Num1
|  |  col: 5
|  |  hi: 5
|  |  lo: 0
|  |  m2: 53.5
|  |  mu: 2.5
|  |  n: 14
|  |  oid: 6
|  |  sd: 2.02864
|  |  txt: $playHours
t.oid: 1
t.rows
|  1
|  |  cells
|  |  |  1: 100
|  |  |  2: 68
|  |  |  3: 80
|  |  |  4: 0
|  |  |  5: 3
|  |  cooked
|  |  dom: 0
|  |  oid: 7
|  2
|  |  cells
|  |  |  1: 0
|  |  |  2: 85
|  |  |  3: 85
|  |  |  4: 0
|  |  |  5: 0
|  |  cooked
|  |  dom: 0
|  |  oid: 8
|  3
|  |  cells
|  |  |  1: 0
|  |  |  2: 80
|  |  |  3: 90
|  |  |  4: 10
|  |  |  5: 0
|  |  cooked
|  |  dom: 0
|  |  oid: 9
|  4
|  |  cells
|  |  |  1: 60
|  |  |  2: 83
|  |  |  3: 86
|  |  |  4: 0
|  |  |  5: 4
|  |  cooked
|  |  dom: 0
|  |  oid: 10
|  5
|  |  cells
|  |  |  1: 100
|  |  |  2: 70
|  |  |  3: 96
|  |  |  4: 0
|  |  |  5: 3
|  |  cooked
|  |  dom: 0
|  |  oid: 11
|  6
|  |  cells
|  |  |  1: 100
|  |  |  2: 65
|  |  |  3: 70
|  |  |  4: 20
|  |  |  5: 0
|  |  cooked
|  |  dom: 0
|  |  oid: 12
|  7
|  |  cells
|  |  |  1: 70
|  |  |  2: 64
|  |  |  3: 65
|  |  |  4: 15
|  |  |  5: 5
|  |  cooked
|  |  dom: 0
|  |  oid: 13
|  8
|  |  cells
|  |  |  1: 0
|  |  |  2: 72
|  |  |  3: 95
|  |  |  4: 0
|  |  |  5: 0
|  |  cooked
|  |  dom: 0
|  |  oid: 14
|  9
|  |  cells
|  |  |  1: 0
|  |  |  2: 69
|  |  |  3: 70
|  |  |  4: 0
|  |  |  5: 4
|  |  cooked
|  |  dom: 0
|  |  oid: 15
|  10
|  |  cells
|  |  |  1: 100
|  |  |  2: 75
|  |  |  3: 80
|  |  |  4: 0
|  |  |  5: 3
|  |  cooked
|  |  dom: 0
|  |  oid: 16
|  11
|  |  cells
|  |  |  1: 0
|  |  |  2: 75
|  |  |  3: 70
|  |  |  4: 18
|  |  |  5: 4
|  |  cooked
|  |  dom: 0
|  |  oid: 17
|  12
|  |  cells
|  |  |  1: 60
|  |  |  2: 72
|  |  |  3: 90
|  |  |  4: 10
|  |  |  5: 4
|  |  cooked
|  |  dom: 0
|  |  oid: 18
|  13
|  |  cells
|  |  |  1: 40
|  |  |  2: 81
|  |  |  3: 75
|  |  |  4: 0
|  |  |  5: 5
|  |  cooked
|  |  dom: 0
|  |  oid: 19
|  14
|  |  cells
|  |  |  1: 100
|  |  |  2: 71
|  |  |  3: 91
|  |  |  4: 15
|  |  |  5: 0
|  |  cooked
|  |  dom: 0
|  |  oid: 20
```

As rows are added to `Tbl`
Due 4pm Thursday.

Last time, you incrementally kept stats on a column
of numbersThis one's not hard. What we are really doing here is 
to


## Tips for Python Programmers

If you are a Python programmer, the following code might
offer some code fragments you could use. For example:

- To read from strings, or files, or zipped files, use `strings,file,zippers`.
- To kill leading and trailing whitespace, use `string.zipped()`
- to kill comments and whitespace, see the call below to `re.sub` (in `rows`)
- To find our how to convert strings to etierh floats or ints, use `compiler`.


```python
import re

def compiler(x):
  "return something that can compile strings of type x"
  try: int(x); return  int 
  except:
    try: float(x); return  float
    except ValueError: return str

def string(s):
  "read lines from a string"
  for line in s.splitlines(): yield line

def file(fname):
  "read lines from a fie"
  with open(fname) as fs:
      for line in fs: yield line

def zipped(archive,fname):
  "read lines from a zipped file"
  with zipfile.ZipFile(archive) as z:
     with z.open(fname) as f:
        for line in f: yield line

def rows(src, 
         sep=     ",",
         doomed = r'([\n\t\r ]|#.*)'):
  "convert lines into lists, killing whitespace and comments"
  for line in src:
    line = line.strip()
    line = re.sub(doomed, '', line)
    if line:
      yield line.split(sep)

def cells(src):
  "convert strings into their right types"
  oks = None
  for n,cells in enumerate(src):
    if n==0:
       yield cells
    else:
       oks = oks or [compiler(cell) for cell in cells]
       yield [f(cell) for f,cell in zip(oks,cells)]

def main(s):
  "putting it all together"
  for lst in cells(rows(string(s))):
    print(lst)

```
### What to Hand in

- Place your code  in the `hw/2` directory.
- Place a text file `hw/2/out.txt` in that same directory, showing a transcript of it work.
- Place a link to that code in http://tinv.cc/ase19give

### Extras

Next week, we will add some more tricks which, if you want, you could
get a head start on how.

If a coluLooking ahead



