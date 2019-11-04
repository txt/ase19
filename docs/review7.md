<a name=top>&nbsp;<p> </a>
[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 

# Review 7

## Simulated Annealling (SA)

- Write down psuedocode for SA. Assume you are running three vectors:
   `current`, `next`, `best``.  You may use  the function:

```
def maybeJump2WorseSolution(old,new,t,cooling=1):
  return math.exp((old - new)/t) < r()**cooling: 
```

Annealling is a process of slowly cooling a crystalline structure such that
the particles reach minimum distance to all other atoms.

- What is the connection of annealling to simulated annealling (SA)?
- SA using "cooling". What is the difference between "hot" SA and "cool" SA?
- Without "hot" SA, what might go wrong with SA- optimization?
- Traditional SA is single objective optimizer:
  - Give an example of a _aggregation function_ that can turn an n-goal optimization
    problem into a 1-goal optiization problem.
  - Such aggregation functions has a problem with "magic weights". What is that problem?

## Local search

- Write down psuedocode for MaxWalkSat. Hint: start with with simulated annealling,
  keep the same three vectors, remove cooling, at restarts.


## Genetic algorithms

- Explain:  GAs evolve a population over multi-generations
- Given a population of vectors of candidate solutions, define:
  - mutate
  - crossover (assume single point crossover)
  - select (assume binary domination and select via exhaustive domination search)
- Suggest alternatives for single point crossover.

## Differential Evolution


- Write down the psuedo-code for DE. 
  - Include _cr_ (probability of crossover); 
  - _f_ (the crossover amount); and 
  - _np_ (the number of candidates in the population)
- Explain (ensuring that you take special care explaining the terms in _italics_):www  
  DE is an _evolutionary program_ that uses a small _external archive_ as the source for mutations

## Particle Swarm Optimization

In PSO, canidates mutate at some velocity,
At every step of PSO, a particle's velocity is changed  using  

- _v = v<sub>0</sub> + (&Phi;<sub>1</sub> \* r \* X) + (&Phi;<sub>2</sub> \* r \* Y)_  

where  _r_ is a random number _0 &le; r &le; 1_. 

In the above 
- How is  the role of 
  _&Phi;<sub>1</sub>_ different to
  _&Phi;<sub>2</sub>_?
- What is _X,Y_?
- What is the role of the _v<sub>0</sub>_ term?
- SA, DE, GAs, optimize to a plateau, and stop. PSO is a better way to continual
  check and, maybe, update colutions.
