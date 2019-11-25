<a name=top>&nbsp;<p> </a>
[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 

# Review 8

## Review:

| English     |       got to  | logic    |     
-------------|----------|----------------|
|x requires y |               | -x or y     |
|x implies   y |  x requires y | -x or y     |  
|p is parent of feature c | c implies p |
|x excludes y |                | -x or -y|
|x conflicts y | x excludes y            | |
|p can have 1 or more of g.i | p implies (g1 or g2 )| -x or y or z|
|p must  have 1 or more of g.i | p implies (g1 and g2 ) | (-x or g1) and (-x or g2) |
|p depends on g.i | g implies (g1 and g2 )|
|cross tree constraints | arbitrary formula|


## Modeling costs

- What is the purpose of

  - The systems model
  - The properties models

- Given an example wehre the propoerites oldeing ahs to be processed via multi-obkjective optimziation

- What is the relevant size of the systems and properties models?
  - Explain, with an example. the systems model is about being inside the code and the properties model can be the connection to the external world.
- What is the execution code of modeling?
  - When is that  cost be:
    - Very small (give an example)
    - Very large (give and example)
- What is the verification cost of modeling?
  - When is that  cost be:
    - Very small (give an example)
    - Very large (give and example)

## Feature Model Logic


1a. Assuming x,y, z and variable numbers 0,1,2, write down the DIMACS CNF formula for each of the following.Recall 
that  each line of the DIAMCNF
is an "or" and all the lines are "and"ed together
If any of the following are synonyms, write down (see "XXX" where "XXX" is the synonyms}

- x needs y
- x is a parent of feature y
- x stops y


1b. Here is a feature model were B and C are a required part of A but C  is  optional. 
For this model, write down:
- its English form (using the above words). 
- its logical form
- its DIAMCS CNF form

```
   A
 / | \
B  C  D
```

1c. Repeat the exercise for 1b but now there is a cross-tree constraint forbidding C is D is used:

```
    A
 /  |  \
B   C   D
    |   |
    .-x-.
```

1d. For the model of 1c, write down settings to a,b,c,d that satisfy that model.


2. The picosat literature suggests a method for finding more than one solution. Describe that method.

3. When using sat solvers for, say, 5 goals:
   - Why might indicator dominance  be better than boolean dominance
   - How to do a "reduced goal initial forward chaining study" to handle hard-to reach goals
   - How might random projections over the goals make reasoning about these goal any easier?

4. Explain: for CNF and sat solvers, verification is faster than repair than generation. Note 
   that you will need to explain _verification, repair, generation_.

