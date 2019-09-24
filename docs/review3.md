<a name=top>&nbsp;<p> </a>
[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 


# Review 3

## KNN

- Define
- Here is a distance function that might be used in KNN : &sum; (x-y)<sup>p</sub>))<sup>1/p</sup>
    - At p=2, does this function have another name?
    - Assuming p=2, what is the distance between (1,0,0) and (0,1,0)?
- Explain the following terms: KNN grabs some **smaple** of all the data then applies a **kernel** to summarize then **k** neighbors
- What are some possible values for
   - **kernel**
   - **k** 
   - **p** 
- If applying KNN to **all** 1000 training examples, what is the value of **sample**
- Explain: "KNN is a lazy learner"
- Explain: "KNN is very slow on large data sets"
- Explain: "KNN can be optimized via clustering"

## K-Means

<img width=300 src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/K_Means_Example_Step_1.svg/1280px-K_Means_Example_Step_1.svg.png">

- At each step of k-means, examples label themselves with their nearest centroid. Using the above example, illustrate that labelling step.
- How are the initial K centroids selected (give any one method)
- How are the K centroids updates?
- How does K-means terminate??
- How can K-means optimize KNN? Be specific.
##  ZeroR

For the following data:

```
outlook  temperature  humidity   windy   play
-------  -----------  --------   -----   ----
rainy    cool        normal    TRUE    no
rainy    mild        high      TRUE    no
sunny    hot         high      FALSE   no
sunny    hot         high      TRUE    no
sunny    mild        high      FALSE   no
overcast cool        normal    TRUE    yes
overcast hot         high      FALSE   yes
overcast hot         normal    FALSE   yes
overcast mild        high      TRUE    yes
rainy    cool        normal    FALSE   yes
rainy    mild        high      FALSE   yes
rainy    mild        normal    FALSE   yes
sunny    cool        normal    FALSE   yes
sunny    mild        normal    TRUE    yes
```

- After reading the above data, what does Zero predict for the following? How does it comptue it?


```
Outlook       Temp.         Humidity    Windy         Play
Sunny         Cool          High        True          ?
``` 

- Explain: KNN and K-Means are unsupervised learners but ZeroR is a supervised learner.
- The above data is symbolic. If it were numeric, how would you adjust a Naive Bayes classifier?

##  Naive Bayes

- For the same data and example as above, what does NB predict? Show all working.
- Explain: "Naive Bayes is **not** a lazy learner"
- Explain why Naive Bayes is "naive".
- "Naive" Bayes has a low memory footprint and fast incremental update. Why?
- Is Naive Bayes a supervised or unsupervised learner?


## Test and split:

- What is the over-fitting problem? Give an example. How  can separating data into train and split address that issue?
- What are order effects? Given an example. How can randomizing the order of the data mitigate that problem?
- Define:
    - N-way cross-validation
    - M\*N-way cross-validation
- Explain and expand
    - "For a very small data set, do not do 10-way."
-   - "For very slow learners (e.g. deep learning), cross-val is hard"
- Explain (definition terms as needed):
    - "Leave one out is an extreme case of N-way cross validation"
    - "Level one out is not recommended for very slow learners"
- Incremental validation
    - Define
    - Explain: "when the learner is slow to update, best to read the data incrementally in large chunks"
    - Explain and fix:  "in my incrementally learning, I saw the test case variance increase towards to end of the run"
- Temporal cross-validation:
    - Define
    - Explain: "temporal cross-val avoids the problem where standard n-way uses future data to predict the past"
    - What to do when the data set has no time stamps?

## Statistics

Given N learners, an N\*M cross-val will generate N\*M results per data set. Now we have to check is learner A is better than learnerB. 

Ttests:

T-tests check if they can a sample might come from either of two distrubtions.

- Draw normal bell curves for which it is 
    - **easy** to show that the sampels are different.
    - **hard** to show that the sampels are different.
- Explain: "t-tests make parametric assumptions about the data"
- Draw two distrubutions that would not be suitable for t-tests

```python
DULL=0.147
def cliffsDelta(lst1,lst2, dull = DULL):
     Warning: O(N)^2."""
  n= gt = lt = 0.0
  for x in lst1:
    for y in lst2:
      n += 1
      if x > y:  gt += 1
      if x < y:  lt += 1
  return abs(lt - gt)/n <= dull
```

Cliffs-Delta

- The above code shows the cliff's Delta effect size test for checking if one list of numbers is different to another
  - Explain this code.
- Explain: "Cliff's Delta  is a non-parametric test"

Scott-Knott:

- Explain: "Its like a recursive clustering algorithm"
- When splitting treatments, what is the function Scott-Knott is trying to maximize?
- Explain: "When recursing, sometimes Scott-Knott will not descend into a split"
- Explain: "Scott-Knott could use Cliffs-Delta or t-tests or any other statistical test"
- For the following example:
    - Sort by medians
    - sketch the quartiles (or, as done in class, the 10ths 30ths 50ths 70ths 90ths)
    - propose groupings where similar results are placed together

```
RX   10 %   30 %   50 %   70 %   90 %
--   ----   ----   ----   ----   ----
x1 : 0.34,  0.49,  0.51,  0.51,  0.60
x2 : 0.60,  0.70,  0.80,  0.80,  0.90
x3 : 0.15,  0.25,  0.35,  0.35,  0.40
x4 : 0.60,  0.70,  0.80,  0.80,  0.90
x5 : 0.10,  0.20,  0.30,  0.30,  0.40
```
   
