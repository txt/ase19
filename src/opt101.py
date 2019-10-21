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

import math,random
r = random.random

class Num:
  def __init__(i,inits=[],mu=0, sd=1):
    i.n       = 0
    i.mu, i.m2     = 0, 0
    i.lo, i.hi     = 10 ** 32, -10 ** 32
    [i + x for x in inits]
    i.mu, i.sd = mu, sd
    [i + x for x in inits]
  # all the other methods
  # ...
  # finally:
  def __add__(i,x):
    i.n += 1
    
  def jiggle(i,n):
    "pull a random number from this distribution"
    z= lambda : math.sqrt(-2*math.log(r()))*math.cos(2*math.pi*r())
    return [ i.mu + i.sd * z() for _ in range(n) ]

def optimize(f       = model1,
             epsilon = 0.0000001,
             budget  = 10**4,
             samples = 100,
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
  return dist.mu

if __name__ == "__main__":
   print(optimize())
