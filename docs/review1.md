<a name=top>&nbsp;<p> </a>
[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 


## Review1

For  `Num`bers:

- Define mean and standard deviation. 
- What does a large sd mean? 
- What does a small sd mean? 
- Show a list of numbers for which the standard deviation is zero

For `Sym`bols:

-  There are two terms term1,term2 that  are analogous to mean and standard deviation. What are they?
-  Given the set of symbols "aaaabbc", calculate those terms (it is ok to leave the result as fractions).
- Adjust the set of symbols such that term1 changes value. 
- Adjust the set of symbols such that term2 increases or decreases.
- Show a list of symbols for which the "term2" is zero.

For each of _TOOL_ &isin; (blusterers, classifiers, regressors,  and multi-objective optimizers).

- Define what _TOOL_ does
- Give a specific example of when you would use _TOOL_.
- (Here are  two questions you may not be able to answer... yet) 
  - Name a commonly used algorithm for doing _TOOL_;
  - Very briefly, describe how _TOOL_ operators.
- Assume data headers can have the special characters;
  - "!" (for "class")
  -  "<" for ("minimize"), 
  - ">" for (maximize), 
  - "$" (for number) 
  - and that anything without any mark is an independent  symbol.
  - Assume a data set has five columns with a header `name,age,daysTillDeath, zipCode,income`
    - Write down a header that means we should use _TOOL_.

- Assuming A,B,C,D are the  true negative, false  negatives, false positives, true positives (respectively) seen
  by a classifier , then
  - define accuracy
  - define recall
  - define false alarm
  - define precision
  - When is "accuracy not accurate"? Give specific values to A,B,C,D where a classifier has a high accuracy yet
    usually misses the target concept (i.e. high accuracy, low recall)
  - When is "precision not precise"? i.e. Give a specific example where a classifier has a very low
    precision, yet still might be considered useful.
  The following question using the following function.
    - What is the accuracy seen below?
    - What is the recall for "yes"?
    - What is the false alarm rate for "no"?
    - What is the precision for "maybe"?

```awk
function _abcd(f,i,j) {
  Abcd(i)
                             # want,    got
                             #------    -------
  for(j=1; j<=6; j++) Abcd1(i,"yes",    "yes")
  for(j=1; j<=2; j++) Abcd1(i,"no",     "no")
  for(j=1; j<=5; j++) Abcd1(i,"maybe",  "maybe")
  for(j=1; i<=1; j++) Abcd1(i,"maybe",  "no")
  AbcdReport(i)
}
```

Multi-objective optimization

- define the booleana domination predicate suitable for two objectives
- Assuming we want to minimize power consumption and cost
  - draw 20 dots on a two-d grid. Mark the pareto frontier.
    - on that first drawn, draw a tiny square around any dot "_X_" then draw the (much larger)
      rectangle indicating which other
      dots are dominated by "_X_" 
  - Make a second drawing (on a new pience of paper)
    - draw 10 circles from optimizer one and 10 crosses from optimizer two
    - draw the reference frontier
- Define hypervolumns, spread, generational distance (GD), inverse generational distance (IGD)
  - On the second drawing, show one distance measurement that would be make for GD but not for IGD
- (Here are  two questions you may not be able to answer... yet) 
  - define a domination predicate suitable for 3,4,5 objectives.

