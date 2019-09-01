<a name=top>&nbsp;<p> </a>
[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 



#  Evolutionary Optimization

src="https://www.youtube.com/embed/plVk4NVIUh8"

<a href="http://www.youtube.com/watch?feature=player_embedded&v=src="plVk4NVIUh8" target="_blank"><img src="http://img.youtube.com/vi/plVk4NVIUh8/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

## Preamble

Here's a very simple optimizer that tries to find what `x` values
lead to better `y` values.

```python
import math,random
r = random.random
sq= math.sqrt; e= math.e; log= math.log; cos= math.cos; pi= math.pi

def model(x):
  "just some function that we need to minimize"
  return e**(-(x-2)**2) + 0.8 * e**(-(x+2)**2)

class Num:
  def __init__(i,inits=[],mu=0, sd=0):
    i.mu,i.sd = mu,sd
    # the stuff you coded before
    [i + x for x in inits]
  # all the other stuff you coded
  def any(i):
    "pull a random number from this distribution"
    return i.mu + i.sd * sq(-2*log(r()))*cos(2*pi*r())

def optimize(f       = model,
             epsilon = 0.0000001,
             n       = 100,
             best    = 10,
             mu      = -6,
             sd      = 100):
  pop = Num(mu=mu, sd=sd)
  for _ in range(n):
    if pop.sd <= epsilon: break
    xs  = [ pop.any() for _ in range(n) ] # draw from before
    ys  = [ f(x) for x in some ]          # find new values
    ys  = sorted(ys)[:best]               # rank them, find best
    pop = Num( ys[:best] )                # reset, using best 
  return pop.mu
```

There is much that can be improved here:

- 

## GA
- An EO procedure does not usually use gradient information in its
search process. Thus, EO methodologies are direct search procedures,
allowing them to be applied to a wide variety of optimization
problems.

- An EO procedure uses more than one solution (a population approach)
in an iteration, unlike in most classical optimization algorithms
which updates one solution in each iteration (a point approach).
The use of a population has a number of advantages: (i) it provides
an EO with a parallel processing power achieving a computationally
quick overall search, (ii) it allows an EO to find multiple optimal
solutions, thereby facilitating the solution of multi-modal and
multi-objective optimization problems, and (iii) it provides an EO
with the ability to normalize decision variables (as well as objective
and constraint functions) within an evolving population using the
population-best minimum and maximum values.

- An EO procedure uses stochastic operators, unlike deterministic
operators used in most classical optimization methods. The operators
tend to achieve a desired effect by using higher probabilities
towards desirable outcomes, as opposed to using predetermined and
fixed transition rules. This allows an EO algorithm to negotiate
multiple optima and other complexities better and provide them with
a global perspective in their search.


1. **Start:** Generate random population of n chromosomes (suitable solutions for the problem)
2. **Fitness:** Evaluate the fitness f(x) of each chromosome x in the population
3. **New population:** Create a new population by repeating following steps until the new population is complete
  - **Selection:** Select two parent chromosomes from a population according to their fitness (the better fitness, the bigger chance to be selected)
  - **Crossover:** With a crossover probability cross over the parents to form a new offspring (children). If no crossover was performed, offspring is an exact copy of parents.
  - **Mutation:** With a mutation probability mutate new offspring at each locus (position in chromosome).
  - **Accepting:** Place new offspring in a new population
4. **Replace:** Use new generated population for a further run of algorithm
5. **Test:** If the end condition is satisfied, stop, and return the best solution in current population
6. **Loop:** Go to step 2


Examples:
