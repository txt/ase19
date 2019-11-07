<a name=top>&nbsp;<p> </a>

[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 

# Homework 9: Big Data

Lets see if we can learn from large data sets, without holding all that data .

Same as homework 8 but now:

- Read in the first 5000 rows, randomize the order
- Do unsupervised clustering on the first 500 rows
- Then, one a time, dribble in the remaining 4500 rows and only update kids if the new data is anomalous
- Then, one a time, dribble in the rows and only update kids if the new data is anomalous

Engineering tips:

- Make the nodes of your tree "smart".
  - They get new rows, one at a time
    - and only if they are anomalous might they get pushed to subtrees
  - When there is enough, that node knows to make its own sub-tree.
- Define "anomaly" using the pivots
  - havea  magic constant _&alpha;=0.5_
  - If the cosine distance from east to west is _c_;
  - The if a new row is distance _a,b_ from _east west_ then if falls at distance _x_ along _c_
    - _x = (a^2 + c^2 - b^2) / (2c)_
  - And if the sub-trees are being split at _s_
    - if  _s &lt; 0.5_
	  - then _far = s*&alpha;_ and anomalous is _x &lt; far_
    - else
	  - then _far = s+ (1-s)*&alpha;_ and anomalous is _x &gt; far_

To assess the results:

For two large datasets (xomo10000 and pom310000)
  - Build a  tree using all data (as in prior homeworks).
  - 100 times select rows in a leaf cluster, at random
       - Tag each of these _probes_ with the BEFORE values
          - size, mean and standard deviation of the performance scores in their leaf cluster
  - 20 times, rebuild the trees using all the data
     - Find the _probes_
     - Tag the _probes_ with the AFTER values:
        - size, mean and standard deviation of the performance scores in their leaf cluster
     - Using the code at https://gist.github.com/timm/33578871be53e604da83679dc7ccbcc5, report
       how often these probes land on the _same_  distributions in AFTER than BEFORE
           - i.e. when `Num.same` test passes.
  - Let _baseline_ be the mean _same_ score found in the above 20 repeats.
  - Now 20 times repeat:
    - build the trees incrementally
    - Compute the _same_ score (using the same 100 _probes_ as used above)
  - Write a table showing the same score seen with _all_ and _incremental_

Write a file `report.txt` commenting on how much _&alpha;_ effects the _same_ score.


## What could go wrong

The _baseline_ score is very low (in which case the random projections are finding wildly different clusters).

- If that happens, spend more time finding the pivots (i.e. lesson the "random" in the random projections)

