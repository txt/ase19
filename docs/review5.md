<a name=top>&nbsp;<p> </a>
[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 


# Review 5

## Clustering 

### Distance Calculation Tricks

In the following code `i.fun` is some two argument function that returns the distance between two
rows `i,j`. The code illustrates an important trick for  reasoning over distance calculations. 

- Explain that trick
- Why, when doing recursive random projections might that trick be useful?
- Why, when doing a cross-validation experiment,  might that trick be useful?

```python
def dist(i,one,two):
    k1,k2 = i.key(one), i.key(two)
    if k1 > k2: 
       k1,k2   = k2,k1
    k = (k1,k2)
    if not k in i.cache:
        i.cache[k] = i.fun(one,two)
   return i.cache[k]
```

### Pivots for Random Projections

There are at least two ways to do random projections:

1. Gaussian matrix multiplication 
2.  Random pivots 

Explain: 

- "Random pivots are preferred when handling symbolic and missing values."
- "Random pivots can scale to larger data sets than Gaussian matrix multiplication."

Draw an football-shaped  cloud of points on a two-dimensional grid (and that grid have two axes  (x,y), each of which run 0..1).

- Using that cloud, explain the Fastmap algorithm for finding two distant points

Draw a second football-shaped  cloud of points on a two-dimensional grid that illustrates "the problem of outliers". Make sure you write 
text to explain that problems.

## LSR

(This section might require some self study. See [here]().)

Draw two squares.

- In square one, draw some dots showing a very very strong negative correlation between x and y
- In square one, draw some dots showing a weak positive  correlation between x and y
- In square three, draw some dots showing zero  correlation between x and y

LSR

- What is "LSR" short for?
- What is the output format of the model found by LSR?
- How could that model be used for classification?

Draw some dots that run from bottom left to top right on  a two-dimensional grid (and that grid have two axes  (x,y), each of which run 0..1).

- On that plot, show a line that might be added by LSR
- On that plot, show a line that probably would not be added by LSR

