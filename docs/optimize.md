<a name=top>&nbsp;<p> </a>
[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 



#   Optimization

Having read [lst](lsr.md), we have some idea how data miners can find the structure within data.
How is that different to Optimizers? Well:

- Data miners report "what is"
- Optimizers report "what to do",  in order to reach some goal.

Optimization is a process that happens all the time;

-  Here's a little video show how life optimizes to make more life. 
- In the video, bands of antibiotics of increasing concentration and smeared across a large plate of bug food (4 feet long, 2 feet wide).
- E.coli are added to the two end zones (that have no antibiotics),
- In a matter of days, these bugs learn how to grow even in the presence of massive amounts of antibiotics.
  E.coli are what's know as prokaryotic cells which means that they are simple bags of water containing floating strands of DNA (they have no nucleus or any internal membrane-bounded organelle). 
  - When two prokaryotes rub against each other, they can exchange material just by mixing this floating bits.  
  - That means that as E.coli grow across the agar plate in the above video, they keep exchanging genetic material with the other bugs that they meet along the way.
  - So its like the bacteria and floating around in a kind of  a blender that keeps mixing and matching all the different bits.
  - (For your information, you are a eukaryote which means your cells are far more structured and include nucleus and varying organelles including, 
     something called mitochondria-- which are the batteries that give us the juice needed to build large structures, then
    run them around, quickly. And you should not be too proud about being a eukaryote since, across the whole planet, yours is the least successful way to organizing living things. In marine environments, prokaryotes 
   [out-number everything else by a ratio of 6 to 1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC33863/).


[![Agar plate](https://img.youtube.com/vi/plVk4NVIUh8/0.jpg)](https://www.youtube.com/watch?v=plVk4NVIUh8)

All you need
for an optimizer is a _jiggle_ step and a _select_ step. 
At the start of this video, all the bacteria are just a little bit different (due to random mutations, which occur once [every .4 to 170 hours](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC33863/))

For the E.coli in this video, bugs are selected to make more bugs if they are
not killed by some antibiotic. As to jiggling, 

if you put a lot of E.coli into a tub (or, in the above case, a large agar plate)
everything.


## Preamble

Here's a very simple optimizer that tries to find what `x` values
lead to better `y` values.

```python
import math,random
r = random.random
sq= math.sqrt; e= math.e; log= math.log; cos= math.cos; pi= math.pi

def model1(x, b=2):
  "just some function that we need to minimize"
  return e**(-(x-b)**2) + 0.8 * e**(-(x+b)**2)

def model2(b):
   "trying to guess b to best fit model to data"
   data=[ (-4.5, 0.01) ,(  -4, 0.04) ,(-3.5, 0.14) ,(  -3, 0.37) ,(-2.5, 0.66) 
         ,(  -2, 0.80) ,(-1.5, 0.66) ,( -1,  0.37) ,(-0.5, 0.15) ,(   0, 0.08) 
         ,( 0.5, 0.18) ,(  1, 0.46)  ,( 1.5, 0.82) ,(   2, 1.00) ,( 2.5, 0.82) 
         ,(   3, 0.46) ,( 3.5, 0.17) ,(   4, 0.05) ,(4.5, 0.01) ]
   err=0
   for x,actual in data:
     predict = model1(x,b)
     err    += abs(predict - actual)
   return err

class Num:
  def __init__(i,inits=[],mu=0, sd=0):
    i.mu,i.sd = mu,sd
    # the stuff you coded before
    [i + x for x in inits]
  # all the other stuff you coded
  def any(i):
    "pull a random number from this distribution"
    return i.mu + i.sd * sq(-2*log(r()))*cos(2*pi*r())

def optimize(f       = model1,
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
