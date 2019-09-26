<a name=top>&nbsp;<p> </a>
[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 

# Clustering

https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html:

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_0011.png)

## Distance functions.

Many. e.g. p-norm

- D= (&sum; (&delta;(x,y))<sup>p</sup>))<sup>1/p</sup>
- euclidean : p=2

But what is &delta;  ?

- Symbols: 
    - return 0 if x == y else 1
- Numbers:
    -  x - y
    - to make numbers fair with symbols, normalize x,y 0,1 using (x-min)/(max-min)

What about missing values:

- assume worst case
- if both unknown, assume &delta; = 1
- if one symbol missing, assume &delta; = 1
- if one number missing:
    - let x,y be unknown, known
    - y = normalize(y)
    - x = 0 if y > 0.5 else 1
    - &delta; =  (x-y)

## Curse of Dimensionality

Distance gets weird for high dimensions

- for an large dimensional orange, most of the mass is in the skin
- volume of the space increases so fast that the available data become sparse.
- amount of data needed to support the result grows exponentially with dimensions

## Random Projections

- technique used to reduce the dimensionality of a set of points
-  known for their power, simplicity, and low error rates when compared to other methods

- Method one: Guassian random projections
   - Matrix = rows \* cols
   - Matrix A,B
   - A =        m × n 
   - B =        n × p 
   - C = A\*B = m x  p
   - So we can reduce n=1000 cols in matrix A to p=30 cols in C via a matrix
      - 1000 row by 30 cols
   - Initialize B by filling each column with a random number pulled from a normal bell curve
   - Only works for numbers
   - Requires all the data in RAM (bad for big data sets)
- Method two:  LSH: locality sensitivity hashing
   - Find a way to get an approximate position for a row, in a reduced space
      - e.g. repeat d times
          -  Find  two  distant "pivots"  = (p,o)
              - Pick, say, 30 rows at random then find within them, the most distant rows
          - the i-th dimension:
              - this row's d.i = 0 if (row closer to p than o) else 1
      - repeat d=log(sqrt(N))+1 pivots to get  d random projectsion
   - If you want not 0,1 on each dimension but a continuous number then:
      - given pivots (p,o) seperated by "c"
      - a = dist(row,p)
      - b = dist(row,o)
      - this row's d.i = (a^2 + c^2 - b^2) / (2c)
          - Cosine rule
   - Can be done via random sampling over some of the data.
      - Better for bigger data
      - But less exact
      - still, darn useful

![](https://ars.els-cdn.com/content/image/1-s2.0-S0031320315003945-gr2.jpg)
 
## KD-trees

Simplicity itself

- Find wildest dimension 
    - e.g. Most variance, 
    - e.g. Greatest max - mix
- Divide in two on that dimension
    - e.g. At median point
- Recurs on both halves
- Stop when you've found, say,sqrt(N) of the data

Problem: curse of dimensionality

- For large dimensional problems
- After a few cuts, each cut is now to small to separated
   - and th data in each cut is still wildly variable since we've missed important dimensions

Solution:

- Random projections:
   - To find wildest dimension
   - At each level, do LSH 30 times and select the points that are most distant (*)


(*) beware outliers :  

- A safe thing might be to sort the pivots  by their distance and take something that is
  90% of max distance

## Kmeans: 

done

## Mini-batch k-means

Done

- For scaling to very large data sets, we make   a grand and glorious hack to the grand and glorious K-means hack.
- [Mini-batch K-means](https://www.eecs.tufts.edu/~dsculley/papers/fastkmeans.pdf) reads the data in eras (called "batches") of size "_b_". 
   - As with K-means, we label each arriving example with the id of its nearest sample (and initially, we pick those centroids at random). By the way, this is analogous to the  "E" step
   - For the "M" step, we assume that the more examples a centroid has seen, the
      More we believe in it and the less we want to move it 
    - "n" stores how often this centroid has been picked by new data
    - So in the "E" step, each item "pulls" its centroid  attribute "c" towards its own attribute "x"  by an amount weighted   `c = (1-1/n)*c + x/n`. 
    - Note that when "n" is large, "c" barely moves at all.


## Exercise


[A method for initialising the K-means clustering algorithm using kd-trees](http://bit.ly/2lQO7BG)

- What is the Forgy method (section 1.1)
- What  is the Bradley and Fayyad's method? (section 1.2)
- What is your favorite other method?
- What is the method of this paper?
