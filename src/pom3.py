#!/usr/bin/env python3
# vim: nospell:sta:et:sw=2:ts=2:sts=2

from limits import Float,Int,Limits
import random,math
r=random.random

MAX_VALUE = 1500

class pom3(Limits):
    def x(p3): return [
      Float('$Culture'    ,              .1 ,    0.9),
      Float('$Criticality',             0.82,   1.2),
      Int('_Criticality Modifier',      2,     10  ),
      Float('$Initial Known',           0.4,    0.7),
      Int('_Inter-Dependency',          1,    100  ),
      Int('_Dynamism',                  1,     50  ),
      Int('_Size',                      0,      4  ),
      Int('_Plan',                      0,      5  ),
      Int('_Team Size',                 1,     44  )]

    def y(p3): return [
           '<Cost', '?Score', '<Completion', '<Idle' ]

    def evaluate(p3, inputs):

        # # # # # # # # # # #
        # 0) Initialization #
        # # # # # # # # # # #

        POM3_DECISIONS = pom3_decisions(inputs)
        numberOfShuffles = random.randint(2,6)

        # # # # # # # # # # # # # # #
        # 1) Generate Requirements  #
        # # # # # # # # # # # # # # #

        POM3_REQUIREMENTS = pom3_requirements(POM3_DECISIONS)

        # # # # # # # # # # #
        # 2) Generate Teams #
        # # # # # # # # # # #

        POM3_TEAMS = pom3_teams(POM3_REQUIREMENTS, POM3_DECISIONS)

        # # # # # # # #
        # 3) Shuffle  #
        # # # # # # # #


        for shufflingIteration in range(numberOfShuffles):

            for team in POM3_TEAMS.teams:
                team.updateBudget(numberOfShuffles)
                team.collectAvailableTasks(POM3_REQUIREMENTS)
                team.applySortingStrategy()
                team.executeAvailableTasks()
                team.discoverNewTasks()
                team.updateTasks()

        # # # # # # # # # # # # #
        # 4) Objective Scoring  #
        # # # # # # # # # # # # #

        cost_sum,value_sum,god_cost_sum,god_value_sum,completion_sum,available_sum,total_tasks = 0.0, 0.0, 0.0, 0.0, 0,0,0
        for team in POM3_TEAMS.teams:
            cost_sum += team.cost_total
            value_sum += team.value_total
            available_sum += team.numAvailableTasks
            completion_sum += team.numCompletedTasks
            for task in team.tasks:
                if task.val.visible:
                    total_tasks += 1

            for task in team.tasks:
                if task.val.done == True:
                    god_cost_sum += task.val.cost
                    god_value_sum += task.val.value

        if cost_sum == 0: our_frontier = 0.0
        else: our_frontier =     value_sum /     cost_sum

        if god_cost_sum == 0: god_frontier = 0.0
        else: god_frontier = god_value_sum / god_cost_sum

        if god_frontier == 0.0: score = 0.0
        else: score        =  our_frontier / god_frontier

        if completion_sum == 0: cost = 0
        else: cost = cost_sum/completion_sum

        if available_sum == 0: idle = 0
        else: idle = 1 - completion_sum/float(available_sum)

        if total_tasks == 0: completion = 0
        else: completion = completion_sum/float(total_tasks)



        return [cost, score, completion, idle]


class Requirement(object):

    def __init__(self, c, v):
        #cost of the task
        self.cost = c

        #value of the task (priority)
        self.value = v

        #if the task is done or not
        self.done = False

        #if the task is visible (invisible tasks technically have not been planned at all by project leaders)
        self.visible = False

    def __repr__(self): return "Done? " + str(self.done) + ".  (Cost: " + str(self.cost) + ", Value: " + str(self.value) + ")"


class requirements_node(object):
    def __init__(self, v, k, p=None, c=[], l=0):
        self.val = v
        self.key = k
        self.parent = p
        self.children = c
        self.level = l
        self.dependencies = []

    def add_child(self, v, k, l):
        self.children.append(requirements_node(v, k, self, [], l))

    def __repr__(self):
        if self.parent:
            return (" "*self.level + "{Key: " + self.key + ", Val: " + str(self.val) + ", ParentKey = " + self.parent.key + " Dep: " + str(self.dependencies) + "}")
        else:
            return (" "*self.level + "{Key: " + self.key + ", Val: " + str(self.val) + ", ParentKey = None" + " Dep: " + str(self.dependencies) + "}")

    def show(self):
        print(self)
        for child in self.children:
            child.show()

    def iterative_search(self, k):
        for child in self.children:
            if child.key == k: return child
            else:
                result = child.iterative_search(k)
                if result: return result

    def max_depth(self):
        max = 0
        for child in self.children:
            if child.level > max: max = child.level
            m = child.max_depth()
            if m > max: max = m
        return max

    def traverse(self):
        list = []
        for child in self.children:
            list.append(child)
            to_add = child.traverse()
            for i in to_add:
                list.append(i)
        return list



class requirements_tree(object):
    def __init__(self):
        self.tree = []
    def add_root(self, v, k):
        self.tree.append(requirements_node(v, k, None, [], 0))
    def get_root(self, k):
        for root in self.tree:
            if root.key == k: return root
    def find_node(self, k):
        for root in self.tree:
            if root.key == k: return root
            else:
                result = root.iterative_search(k)
                if result: return result

    def get_level(self, root, level):
        list = []
        if (root.level < level):
            for child in root.children:
                list.append(self.get_level(child, level))
        elif (root.level == level):
            list.append(root.key)
        return list

    def traverse(self):
        list = []
        for root in self.tree:
            list.append(root)
            to_add = root.traverse()
            for i in to_add:
                list.append(i)
        return list

    def show(self):
        for root in self.tree:
            root.show()

class Team(object):
    def __init__(self, decisions):

        self.decisions = decisions

        self.team_size = decisions.team_size
        self.plan = decisions.plan
        self.size = decisions.size
        self.visible = 1-decisions.initial_known
        self.known = 0
        self.cost_total = 0.0
        self.value_total = 0.0
        self.numAvailableTasks = 0
        self.numCompletedTasks = 0
        self.budget = 0
        self.tasks = []

    def calcTotalCost(self):
        total = 0
        for task in self.tasks:
            total+= task.val.cost
        return total

    def setPolicy(self, policyInt):
        self.plan = policyInt

    def markTasksVisible(self):
        if (self.visible > 1.0): self.visible = 1.0
        for i in range((int)(self.visible*len(self.tasks))):
            self.tasks[i].val.visible = True



    def updateBudget(team, numShuffles):
        totalCost = team.calcTotalCost()
        team.budget += (totalCost/numShuffles)

    def collectAvailableTasks(team, requirements):
        team.availableTasks = []
        for task in team.tasks:
            if task.val.visible == True:
                #if no dependencies and no children on this task, then add to availableTasks list
                if countNotDones(requirements.heap.find_node(task.key).children) == 0:
                    if task.val.done == False:
                        team.availableTasks.append(task)
        team.numAvailableTasks += len(team.availableTasks)


    def applySortingStrategy(team):

        #method 0: Cost Ascending
        #method 1: Cost Descending
        #method 2: Value Ascending
        #method 3: Value Descending
        #method 4: Cost/Value Ascending
        #method 5: Cost/Value Descending

        if team.plan == 0:   team.availableTasks.sort(key=lambda cv: cv.val.cost)
        elif team.plan == 1: team.availableTasks.sort(key=lambda cv: cv.val.cost, reverse=True)
        elif team.plan == 2: team.availableTasks.sort(key=lambda cv: cv.val.value)
        elif team.plan == 3: team.availableTasks.sort(key=lambda cv: cv.val.value, reverse=True)
        elif team.plan == 4: team.availableTasks.sort(key=lambda cv: cv.val.cost/cv.val.value)
        elif team.plan == 5: team.availableTasks.sort(key=lambda cv: cv.val.cost/cv.val.value, reverse=True)

    def executeAvailableTasks(team):
        for task in team.availableTasks:
            if (team.budget - task.val.cost) >= 0:
                team.budget -= task.val.cost
                team.cost_total  += task.val.cost
                team.value_total += task.val.value
                task.val.done = True
                team.numCompletedTasks += 1

    def discoverNewTasks(team):
        team.visible += nextTime(team.decisions.dynamism/10.0)
        team.markTasksVisible()

    def updateTasks(team):
        #Adjust values
        for task in team.tasks:
            change = (random.uniform(0, team.decisions.dynamism) - team.decisions.dynamism/2)*team.decisions.culture/100.0
            task.val.value += (MAX_VALUE * max(0,change))

def nextTime(rateParameter): return -math.log(1.0 - random.random()) / rateParameter
def countNotDones(list):
    cnt = 0
    for i in list:
        if i.val.done == False: cnt+= 1
    return cnt


class pom3_teams:
    def __init__(p3t, requirements, decisions):
        p3t.teams = []
        p3t.decisions = decisions

        # Build Each Team
        total_size = 0
        while (total_size < requirements.count):

            #specific sized teams
            p3t.teams.append(Team(decisions))
            total_size += decisions.team_size

        # Assign Initial Tasks to Each Team
        begin = 0
        for team in p3t.teams:
            percent = (float)(team.team_size) / (float)(total_size)
            end = (int)(begin+math.ceil(percent*len(requirements.tasks))-1)
            for k in range(begin, end):
                team.tasks.append(requirements.tasks[k])
            begin = end
        if ((end) < len(requirements.tasks)):
            for i in range(len(requirements.tasks) - (end)):
                p3t.teams[len(p3t.teams)-1].tasks.append(requirements.tasks[begin+i])

        # Mark Initial Visibility of Tasks for Each Team
        for team in p3t.teams:
            team.markTasksVisible()

        # Apply Effect of Boehm-Turner Personnel Scales to Task Costs
        scales_alpha = [0.45, 0.50, 0.55, 0.60, 0.65]
        scales_beta  = [0.40, 0.30, 0.20, 0.10, 0.00]
        scales_gamma = [0.15, 0.20, 0.25, 0.30, 0.35]
        for team in p3t.teams:

            numAlphas = scales_alpha[decisions.size]*team.team_size
            numBetas = scales_beta[decisions.size]*team.team_size
            numGammas = scales_gamma[decisions.size]*team.team_size
            #print numAlphas, numBetas, numGammas
            team.alpha = numAlphas
            team.beta = numBetas
            team.gamma = numGammas
            team.power = team.alpha + 1.22*team.beta + 1.6*team.gamma

            for task in team.tasks:
                task.val.cost += task.val.cost * ((numAlphas + 1.22*numBetas + 1.6*numGammas)/100.0)

                # and apply effect of criticality while we're at it
                task.val.cost = task.val.cost * (team.decisions.criticality_modifier ** team.decisions.criticality) # cost' = cost * X^criticality

        #Print Out of Teams & Requirements
        """
        for i,team in enumerate(p3t.teams):
            print "___________________TEAM #" + str(i) + "______________________"
            for e,task in enumerate(team.tasks):
                print "> TASK #" + str(e) + ": " + str(task)
        """



def random_cost(): return random.randint(1, 100)
def random_value(): return random.randint(1, 100)

class pom3_requirements:
    def __init__(requirements, decisions):
        requirements.heap = requirements_tree()
        requirements.count = int(2.5*[3,10,30,100,300][decisions.size])
        requirements.decisions = decisions

        for i in range(requirements.count):
            requirements.heap.add_root(Requirement((decisions.size+1)*random_cost(), random_value()), 'Base Req #' + str('%.3d'%(i+1)))

            parent = requirements.heap.tree[i]
            requirements.recursive_adder(parent, 1)


        #Add dependencies
        for i in range(requirements.count):
            rand = random.randint(1,1000)
            if (rand <= 15):
                #pick a requirement at this level, of the next base tree
                level = 0
                if ((i+1) < len(requirements.heap.tree)):
                    req_node = requirements.heap.tree[i+1]
                    adderDie = random.randint(1,100)
                    if adderDie <= decisions.interdependency: requirements.add_dependency(requirements.heap.tree[i], req_node)
            requirements.recursive_dep_adder(requirements.heap.tree[i], i, 1)


        #linearize the list
        requirements.tasks = requirements.heap.traverse()

    def add_children(self, num, parent, level):
        for c in range(num):
            parent.add_child(Requirement(random_cost(), random_value()), "+"*level + 'Child-' + parent.key[0] + parent.key[len(parent.key)-3] + parent.key[len(parent.key)-2] + parent.key[len(parent.key)-1] + ' #' + str('%.3d'%(c+1)), level)
            self.recursive_adder(parent.children[c], level+1)

    def add_dependency(self, dep_node, req_node):
        #Add a dependency from this node to another node at the same level of the next root
        #We store the key of the requirement_node in the list of the dependent_node's dependencies
        dep_node.dependencies.append(req_node)

    def recursive_adder(self, parent, level):
        #Random exponential chance that we add child node:
        rand = random.randint(1,1000)
        odds = [15, 30, 60, 120, 240]

        for numChildren,chance in enumerate(odds):
            if (rand <= chance):
                self.add_children(5-numChildren, parent, level)
                break

    def recursive_dep_adder(self, parent, rootIndex, level):

        if (len(parent.children) > 0 and ((rootIndex+1) < len(self.heap.tree))):
            if (level <= self.heap.tree[rootIndex+1].max_depth()):
                rand = random.randint(1,1000)
                odds = [15, 30, 60, 120, 240, 500]

                if level > 5: oddsInd = 5
                else: oddsInd = level

                if (rand <= odds[oddsInd]):
                    #pick a random child at this level of this root
                    rand = random.randint(0,len(parent.children)-1)
                    randChild= parent.children[rand]

                    #pick a random node at the level of the next root
                    levelNodes = self.heap.get_level(self.heap.tree[rootIndex+1], level)
                    rand = random.randint(0, len(levelNodes)-1)

                    #add the dependency from randChild to levelNodes[rand]
                    adderDie = random.randint(1,100)
                    if adderDie <= self.decisions.interdependency: self.add_dependency(randChild, levelNodes[rand])
                for child in parent.children:
                    self.recursive_dep_adder(child, rootIndex, level+1)

class pom3_decisions:
    def __init__(p3d, X):
      p3d.culture = X[0]
      p3d.criticality = X[1]
      p3d.criticality_modifier = X[2]
      p3d.initial_known = X[3]
      p3d.interdependency = X[4]
      p3d.dynamism = X[5]
      p3d.size = int(X[6])
      p3d.plan = int(X[7])
      p3d.team_size = X[8]

def sample(m=pom3,repeats=1000):
  i = pom3()
  print(i.names())
  for _ in range(repeats):
    g = i.guess()
    print(g + i.evaluate(g)) #i.guess()))

if __name__ == "__main__":
   sample(10)
