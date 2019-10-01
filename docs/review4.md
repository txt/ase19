<a name=top>&nbsp;<p> </a>
[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 


# Review 4


## Ensembles

### Bagging

- What is bagging
- Why can 10 "bags" do better than one?
- What is the connection of bagging to cross-validation?


### Boosting

- What is boosting?
- Why can 10 "boosts" for better than one?
- What is the difference between bagging and boosting
- Explain: bagging is inherently parallel while boosting is inherently sequential

## Statistics (more)


### T-tests

T-tests report the overlap of two normal bell shaped curves.  Describe how they might be used in a 10-way cross-val experiments to rank different learners (note: your description should be high-level: no formulas required).


Using the terms standard deviation and mean, describe two such curves that t-tests would find

- easy to distinguish. Draw those two curves.
- hard to distinguish due to some value of the means. Draw those two curves.
- hard to distinguish due to some value of the standard deviations. Draw those two curves.

A t-test is a parametric statistical significance test
- what parametric assumptions re made by the t-test?
- for what kind(s) of curves does the t-test not hold?

### Bootstrap

A bootstrap is a non-parametric test of statistically significant difference:

- What is the role of the "test statistic" in the bootstrap?
- What is the role of "sampling with replacement" in the bootstrap? 
     -     Given the list of numbers [10,20,30,40] write down 5 such samples
- Using the terms "test statistic" and "sample with replacement", describe
  the bootstrap (note: your description should be high-level: no formulas required).

### Cliff's Delta

Cliff's Delta is a non-parametric effect size test:

- What is the difference between an effect size test and a significance test?
- How does Cliff's Delta sample two lists to see if one is more than trivially different to the other? Use  pseudocode
- Explain: non parametric methods are slower than parametric method since they have to using sampling, not summarize , of the data

## Clustering:

### Distance

- Describe the distance measure presented in lectures and how it can do distances between vectors containing symbolic or continuous values
- Why does that distance metric normalize numbers 0..1 min..max
- How does that metric handle missing numerics?
- How does that metric handle missing symbols?

### Mini-batch k-means (MBKM)

- Explain. MBKM works in batches to move centroids less and less.
- Explain: MBKM is a better choice than K-means for  very large data sets 

### KD-trees

- Describe the KD-tree algorithm. Assume ranking via max standard deviation and splits at mean.
- Explain: KD-trees suffer from the curse of dimensionality 

### Random projections

- Given the distance measure described above
    -  describe a random projections clustering algorithm that divides 900 examples into clusters of  around size 30
     - Describe how to reduce the curse of dimensionality in KD-trees
- Given a matrix generation algorithm that files columns with gaussians pulled from (mean,sd)=0,1 describe how to
     - reduce a matrix A with m × n rows and columns
     - to a narrower matrix B with m × p rows and columns (p &lt; n)

Aside:

For this kind of RP, it has shown that the Gaussian distribution can be replaced by a much simpler distribution such as

R[i,j] = sqrt(3) with probability 1/6, zero with probability 2/3, and -sqrt(3) with  probability 1/6.
 
$$
{\displaystyle R_{i,j}={\sqrt {3}}\times {\begin{cases}+1&{\text{with probability }}{\frac {1}{6}}\\0&{\text{with probability }}{\frac {2}{3}}\\-1&{\text{with probability }}{\frac {1}{6}}\end{cases}}}
$$
