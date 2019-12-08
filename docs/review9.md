<a name=top>&nbsp;<p> </a>
[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 

# Review 9

These questions come from https://docs.google.com/presentation/d/1TxRuyDRnJA8JDKkhQ9uxI7wLLl4tEoRAmz-7T6Uo8LE/edit#slide=id.g6b7d091a86_0_19

Nick's code ran PSO on CART:

For each _IT_ in  (PSO, CART):

- Describe, _IT_, briefly
- Describe an alternative to _IT_
- Offer a rule of thumb for when you might use _IT_ and when you might use the alternate.

In terms of ethics, what are the transparency and accountability advantages of using tools like CART?

What might be the advantages of combining  PSO and CART?

Give an example of something that might work worse if we did **not** combine PSO and CART.


CART has several hyperparameters, including the following. For each, explain the possible effect
of doubling or halving the default values:

- max\_feature: the percent of features used when looking for a split. Default is 100.
- max\_depth: the maximum dept of the tree. Default is 10.
- min\_sample\_split: the minimum samples requires to split a node into subtrees. Default is 2.
 
PSO has several hyperparameters, including the following. For each, describe the possible effect of
doubling or halving the default values:

- number\_of\_particles: default=30
- _&Phi;<sub>1</sub>_ weighting give to a particle's own best solution. Default is 2.5
- _&Phi;<sub>2</sub>_ weighting give to a community's own best solution. Default is 1.5

Nick added some random jiggle into the process of calculating the next particle position:

- What was the observation that lead him to adding in that jiggle
- What would happen if he jiggled too much?
- What would happen if he jiggled too little?

What is hyper-hyper-parameter optimization? Why didn't Nick use it?

