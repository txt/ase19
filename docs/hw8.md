- Step1: build  a domination function.
 
  - Modify your table class so it knows about goals we want to minimize and maximize. Anything column marked
 with "<,>"  gets a wright of -1,1 and denotes goals you want to minimize,maximze.

Add a function that returns true if one set of goals is better than another. BEst way to do this is reflect on the delta in the value
of each goal, raised to a pwoer:

```python
def dominates(i,j,goals): # i and j are rows.
    z = 0.00001
    s1, s2, n = z,z,z+len(goals)
    for goal in goals:
      a,b = i.cells[goal.pos], j.cells[goal.pos]
      a,b = goal.norm(a), goal.norm(b)
      s1 -= 10**(goal.w * (a-b)/n)
      s2 -= 10**(goal.w * (b-a)/n)
    return s1/n < s2/n

```


