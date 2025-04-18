<a name=top>&nbsp;<p> </a>
[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 



When people start using Optimizers and data miners, the algorithms that beginners find easiest to use are
LSR and NSGA-II 

LSR was discussed [before](lsr.md) and NSGA-II, later. Here, we introduce optimizing.

#   Optimization

Having read [lsr](lsr.md), we have some idea how data miners can find the structure within data.
How is that different to optimizers? Well:

- Data miners report "what is"
- Optimizers report "what to do",  in order to reach some goal.

(Aside: and to find "what is", sometimes we use optimizers since they tell us "what to do" to find a good model. More on that, later.)

Optimization is a process that happens all the time;

-  Here's a little video show how life optimizes to make more life. 
   [![Agar plate](https://img.youtube.com/vi/plVk4NVIUh8/0.jpg)](https://www.youtube.com/watch?v=plVk4NVIUh8)
- In the video, bands of antibiotics of increasing concentration are 
  smeared across a large plate of bug food (4 feet long, 2 feet wide).
- E.coli (which are little bugs) are added to the two end zones 
  (that have no antibiotics),
- In a matter of days, these bugs learn how to grow even in the 
  presence of massive amounts of antibiotics.

How do they do this? Well,
all
need 
is a _jiggler_ and a _selector_ and enough time to

1. jiggle some stuff, 
2. select the better stuff, 
3. go to 1

For the E.coli in the video,
bugs are _selected_ to make more bugs if they are
not killed by some antibiotic. 
As to the jiggling: 

- E.coli are what's know as prokaryotic cells 
- Prokaryotes have no internal membrane-bounded organelles; 
  i.e. very little internal structure.  For the most part,  
  they are just mostly  bags of water containing floating strands of DNA 
- At the start of this video, all the bacteria are just a little bit different (due to random mutations, which occur once [every .4 to 170 hours](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC33863/))
- Later on, when two prokaryotes rub into each each other, they exchange material 
  just by mixing the floating bits (and 
  [a few other tricks](https://www.khanacademy.org/science/biology/bacteria-archaea/prokaryote-structure/a/genetic-variation-in-prokaryotes).  
- That means that as E.coli grow across the agar plate in the above 
  video, they keep exchanging genetic material with the other bugs 
  that they meet along the way.
- So its like the agar plate is a big blender that
  keeps mixing and matching all the different bits of all the different bugs.
- If any of the bugs get lucky, and learn how to handle more antibiotics, those bugs move into a new band (where there is less competition for food).  Hence, the new band gets full of bugs
  that can better handle that higher level of antibiotic.

One important aspect of the above video, that might not be
immediately apparent, is that bacteria from both sides the video
<em>arrive in the middle at about the same time</em>. That is:

-  Even though
every little part of the above seen random and unreliable...
-  The whole
process is  not. Randomly jiggling and selecting things has some
emergent stable properties (better bugs are found) and that this
whole process is a repeatable, trustable, reliable effect.

<img src="../etc/img/eukprok.png" width=400 align=right>
(Just so you know, everything that is alive and big enough to be
seen with the naked eye, including you,  has "eukaryote" cells.
Such  cells are more structured and include nucleus and varying
organelles including, something called
[mitochondria](https://en.wikipedia.org/wiki/Mitochondrion)-- which
give eukaryotes  the extra juice they need to build large structures,
and run them around, quickly. You should not be too proud about
being a eukaryote--  they are the least successful way to organizing
living things.  For example, in marine environments, the prokaryotes
add up to [six times the mass of the larger eukaryotic
organisms](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC33863/).)

## Optimization is easy, right?

Just take the function, find its first derivative, solve for `dy/dx=0` and go there. 

Or, in the local region, compute the local partial deriviaties and take the direction of fastest descent

- a.k.a. if youa re sking, look around for the steepest direction, go there.

<img width=500 src="https://calcworkshop.com/wp-content/uploads/first-derivative-test.png">

Right?

### Problems with Symbols

Humans love their non-numeric knowledge. How to do optimization when everything is not numbers?

e.g. what-if queries across large fault trees:

![](https://www.researchgate.net/publication/324426610/figure/fig1/AS:614050153132063@1523412373801/Fault-Tree-of-Molding-Process.png)

### Problems with Ill-defined (or Missing) Functions

e.g. probing some poorly understand effort

- i.e. you are writing software precisely because you don't know enough and you want to know more
- Many variables not known, or not known with certainty

### Discontinuities

In software, every if and case statement divides internal state space of program into seperate regions, each with their own properties.o

- So not one global model, but model(s)

![](../etc/img/discont.png)

### Constraints

Too many of them ! Competing!

![](../etc/img/fm.png)

In modern product lines, only 1\% or less of randomly generated solutions satisfy known domain constraints

- Hence, we often use Sat-solvers to generated some initial population
- But be warned: SAT solvers do not generate random instances across the while space
  - Their solutions "clump"

### Problems with Local Minima

<img src="../etc/img/moment.gif" width=400 align=right> 
The above code chases down to lower and lower values... which makes this  a greedy search that can get trapped in local minima. 

There are several known solutions to the problem of local minima including

- Add restart-retries. 
  - Restart to a random point and see if you get back to the old solution (if so, it really was the best).
  - _MaxWalkSat_ (MWS) routinely performs dozens of retries.
- Explore a population, not just one thing. 
  - That is, run many times with different starting positions (where as restart-retry only needs memory for one solution, population-based methods exploit cheap memory).
- Add a momentum factor to sail through the local maxima:
  - _Neural  nets_ use such a factor as they adjust their weights
  - _Particle swam optimizers_ (PSO) 
    <img src="../etc/img/pso101.gif" width=400 align=right> 
    - PSO runs (say) 30 "particles"
    - Each particle mutates a solution in a direction determined by 
      - its prior velocity
      - a pull back towards the best solution ever seen by this particle
      - a pull towards the best solution ever seen by any particle
    - So when it finds a better best, it just sails on by 
      - but it might circle back to them
      - kind of like a restart-retry and a populuation and a momentum approach all rolled into one.
    - Which means it may not find one solution-- but a set of interesting (but slightly different) solutions
- Add some random jiggle to the search.
  - e.g. _simulated annealling_
  - For example, 
    given a current solution  `s` 
    that is  an array of numeric value with mins and maximums of `lo,hi`
    and some score `e=f(s)` (known as the "energy") 
    -  Simulated annealers perturb `p`% of those values to generate a new  solution `sn` with a score of `en` .
    - At a probability `2.7183^(e-en)/t)`  determined  by a temperature  value `t`
      - This algorithm replaces the current solution `s` with `sn`
    - But as `t` "cools", the algorithm becomes a hill climber that only moves to better solutions. 

### Minimizing Evaluations

It is  good practice to avoid too many calls to the model evaluation function _f_ 

In many cases, - evaluating a candidate using the _f_ function is very slow
  (e.g. we are running an expensive computation, or asking a human their opinion, or we have to [rebuild a new version of the software to test some configuration options](https://arxiv.org/pdf/1801.02175.pdf)).
- e.g.  "buy a new car, drive it for 100,000 miles with _this_ strategy, check the wear and tear on the tires".
- If humans want to audit/debug the conclusions from an optimizer, then they would prefer to explore fewer options.

Hence, clever optimizers strive the minimize the  budget required to find solutions.


_Sequential  model optimizers_ run a  data miner in parallel with the optimizer. Such optimizer assumes that:

- jiggling (i.e. Candidate generation) is very fast

- in this domain, data miners can build models very quickly

Under those assumptions, then the best way to build a model is to reflect on what has been seen so far (using a data miner)
in order to select what to do next.

1. First, we quickly generate a large number of _xs_ candidates (say, 512).
    - This is usually <u>**VERY FAST**</u>.
2. Using some evaluation function _f_, we  evaluated some small subset _xs[:n]_) to generate _n_ sets of _ys_ results 
   -  _ys[i] = f( xs[i] )_ for _i &lt; n_
   - This step can be <u>**VERY SLOW**</u> if _f_ is very slow to execute. 
   - So here, we keep _n_ small (e.g. _n &le; 30_).
3. Next, using  a data miner (e.g. least squares regression, decision trees, whatever), we build a model M from _xs[:n],ys[:n]_. 
   - This step can be <u>**VERY FAST**</u> since we are learning a  small model from just a few examples.
   - In step (v), we will need to know the mean and variance of the predictions from this model. One way to do that is to 
     - Build a committee of learners `M1,M2,M3,...`; each time using 90% of the data, selected at random;
     - Generate predictions across each member of the committee
     - Report the mean and variance of those predictions
   - Another way is to use a "Gaussian process model" (GPM) which is like regression, but it offers a mean and standard deviation
     on every prediction
     - GPMs have scale up problems (more than 12 attribtues can be a bother).
4. Using that model make approximate guesses _ys[n:]_ about the remaining candidates _xs[n:]_
   -  _ys[i] = M( xs[i] )_ for _i &ge; n_.
   - This step can be <u>**VERY FAST**</u> since we are just calling a very small model `M`.
5. Pick 
   <img src="../etc/img/gp_opt.png" width=500 align=right>
   the  strangest guess (e.g. the largest  outlier, has most variance) for guess _g &in; i &ge; n_. 
   - For example, in the picture at right, we have build a curve from _n=5_ observations.
   - The red line shows where the curve plus variance is greatest.
     <br clear=all>
6. Evaluate the strangest guess
   -  _ys[n+1] = f( xs[g] )_.
   - This is a <u>**SLOW**</u> step, but since we are only evaluating one example, its usually not particularly slow.
      
6. Then _n=n+1_ and we loop back to step 3.

Note that the above uses a data miner inside an optimizer. As mentioned before, data mining and optimization are linked.


## Software Optimizers

Here's a very simple optimizer that explores:

- _model1_ : which  we use to find what `x` values lead to better `y` values. In this example "better" means "smaller".
- _model2_ : which we use to guess better values for the `b` setting within the model. It turns out that _b=2_ is
  the right value, but the optimizer does not know that until it plays around a little.

```python
e=2.718281828459045

def model1(x, b=2):
  "just some function that we want to minimize"
  return e**(-(x-b)**2) + 0.8 * e**(-(x+b)**2)

def model2(b):
   "trying to guess what b best fits the data to the model"
   data=[ # data generated using b=2 (but the optimizer does not know that)
          (-4.5, 0.01) ,(  -4, 0.04) ,(-3.5, 0.14) ,(  -3, 0.37) ,(-2.5, 0.66) 
         ,(  -2, 0.80) ,(-1.5, 0.66) ,( -1,  0.37) ,(-0.5, 0.15) ,(   0, 0.08) 
         ,( 0.5, 0.18) ,(   1, 0.46) ,( 1.5, 0.82) ,(   2, 1.00) ,( 2.5, 0.82) 
         ,(   3, 0.46) ,( 3.5, 0.17) ,(   4, 0.05) ,( 4.5, 0.01) ]
   err=0
   for x,actual in data:
     predict = model1(x,b)
     err    += abs(predict - actual)
   return err
```

<img src="../etc/img/zcurve.png" width=300 align=right> To `jiggle`,
we sample from a standard normal bell-shaped distribution (also
called the unit normal or the Z-curve).  Such a distribution has a
 mean of `mu=0` and a standard deviation of `sd=1`.
<br clear=both>

```python
import math random
r = random.random

def z():
  return math.sqrt(-2*math.log(r()))*math.cos(2*math.pi*r())
```

Next, we use a `Num` class that knows how to accept initial values for `mu,sd`. 
With that class, we can `jiggle` by pull values across the normal bell curve.

```python
class Num:
  def __init__(i,inits=[],mu=0, sd=1):
    # all the usual initializations
    i.mu, i.sd = mu.sd
    [i + x for x in inits]
  # all the other methods
  # ...
  # finally:
  def jiggle(i,n):
    "pull a random number from this distribution"
    return [ i.mu + i.sd * z() for _ in range(n) ]

def optimize(f       = model1,
             epsilon = 0.0000001,
             budget  = 10**4,
             samples = 100
             best    = 10,
             mu      = 0,
             sd      = 100):
  dist = Num(mu=mu, sd=sd)
  while True:
    xs = dist.jiggle(samples)      # jiggle
    ys = [ f(x) for x in xs ]      # score
    budget -= samples              # track how many times we called the model
    ys  = sorted(ys)[:best]        # select "best" smallest values
    dist = Num( ys )               # get set for more jiggling
    if budget  < 0      : break    # taking too long. exit
    if dist.sd < epsilon: break    # close enough. exit
  return di current solutionst.mu
```

Note:

- The `select` step in the above (we keep the `best` smallest values). 
  - This is used to train a new distribution, which sets us up for more `jiggling`, and so on.
- The `budget` variable. 
  - While the above `model1` and `model2` are very fast to run,
in the general case, running the model to evaluate a candidate solution is usually very expensive.
Hence, clever optimizers strive the minimize the  budget required to find solutions.
     - See below: sequential model optimization.
- The `epsilon` variable. 
  - In domains where near-enough is good-enough, or when there is an inherently
  large variance in any conclusion, `epsilon` is large so  optimization can stop early.
  - Note <img src="../etc/img/epsilon.png" width=400 align=right> 
    that  [epsilon domination algorithms](https://www.iitk.ac.in/kangal/papers/k2003002.pdf)
    can be used to reduce the internal search space of an optimizer.
    - If a new solution falls within `epsilon` of an old solution, then it is _redundant_.
    - So don't reason about _all_. Rather, just reason sample around a little. And steer clear of  choices that lead to redundant conclusions.
      - Ignore redundant solutions.
      - Also, if you can,  [deprecate the choices that lead to that solution](https://arxiv.org/pdf/1902.01838.pdf).


## Simulated Annealing

In the following simulated annealer, `sb` is the best solution seen so far (with energy `eb`). Also,
this code assumes we want to minimize the scores.

```python
import math,random
r = random.random

def saMutate(s,lo,hi,p,b,f):
  sn=s[:]
  for  i,x in enumerate(sn):
    if p < r(): 
      sn[i] = lo[i] + (hi[i] - lo[i]) * r()
  return sn, f(sn), b + 1

def sa(s0,              # some intial guess; e.g. all rands
       f,               # how we score a solution
       lo,hi,           # attribute i has ranage lo[i]..hi[i] 
       budget=1000,     # how many solutions we will explore
       mutate=saMutate, # how we mutate solutions 
       p=0.2,           # odds of mutate one attribute
       cooling=2):      # controls if we dont jump to worse things
  #--------------------------------------------------------
  s = sb = s0   # s,sb = solution,best
  e = eb = f(s) # e,eb = energy, bestEnergy
  b = 1
  while b < budget:
    sn, en, b = mutate(s,lo,hi,p,b,f)   # next solution
    if en < eb:  # if next better than best
      sb,eb = s,e = sn,en 
    elif en < e: # if next better than last
      s,e = sn,en 
    else:  # maybe jump to a worse solution
      t = b/budget
      if math.exp((e - en)/t) < r()**cooling: 
        s,e = sn,en
  return sb,eb
```
Initially, `t` is large so this algorithm will often jump to sub-optimal solutions. But as things "cool", this algorithm becomes a 
hill climber that just steps up to the next solution. In the following, just to confuse you, we score things by 1-f (so _better_ means _larger_): 

<img src="../etc/img/Hill_Climbing_with_Simulated_Annealing.gif" width=600 > 



## GA

Simulated annealing assumed we were mutating one solution.

- a useful assumption for a 1951 computer

Genetic algorithms assume we are stochastic ally mutating _populations_ of solutions

- some we could do, once computers had more memory.


Why use a population?

-  It let us exploit
parallel processing power achieving a computationally
quick overall search (BTW, rarely done...) 
- It let us  
normalize decision variables (as well as objective
and constraint functions) within an evolving population using the
population-best minimum and maximum values (x = (x-min)/(max-min))
-  It generates   multiple optimal
solutions, thereby facilitating the solution of multi-modal and
multi-objective optimization problems, 

![](/etc/img/houses2.png)

Why stochastic mutate?

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


