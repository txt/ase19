<a name=top>&nbsp;<p> </a>
[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 


# Overview

This book is about using better software engineering to build better AI software.
 AI is a very broad topic, discussed in
 [so](REFS.md#norvig-2009)
 [very](REFS.md#grus--2019)
 [many](REFS.md#duda-2000)
 [other](REFS.md#witten-2016)
 books. So what makes this book so different?

## Ethically-aligned Design

<img align=right width=400 src="../etc/img/discuss.jpg">

Firstly,   by "better" AI software,
we mean "ethically-aligned".
We assert that the design goals for SE-for-AI must be
prioritize for human well-being.

- It is ethical to improve
the profits of your company since that money becomes wages which
becomes groceries which becomes dinner so everyone and their kids
can sleep better at night.
- It is also ethical to change the design
of AI software in order to ensure   that (say) the software is not
unduly discriminatory towards a particular social group (e.g. some
groups characterized by age, race, or gender).

As discussed below,
AI tools offer us more
choices. This means that they
also offer us more ethical choices.
Better yet, AI also gives us methods
for automatically tracking down  what choices are useful
we want within a very large space of possibilities.
That is, once we tell AI that we want our systems to achieve ethical goals then:

- <em> AI tools lets us be more ethical than ever before.</em>
- But only if we first accept the merits
  and methods of an ethical approach.

So we suggest to you that when you start a new AI project:

- Your  first question should **not** be (e.g.) "what data miners should I apply to this data?".
- Rather, it should be  "what are the ethical requirements of this development? And how can we best support those requirements?".


## Industrial Focus

The second way this book is unique is that
the authors of this book have spent decades applying many
AI tools (mostly  for software engineering applications). We share
some of that case study experience in this book. For example,
recently we
[reversed engineered from multiple AI applications](REFS.md#amershi-2019)
a nine-step
industrial AI pipeline. This book devoted nine chapters to that pipeline:

<img src="../etc/img/9steps.png" width=900>

## Data Miners + Optimizers + Theorem Provers

Thirdly,  we look
 at AI tools which,  recently, have had a major   impact on software
 engineering. Specifically, we will talk much about data mining
 algorithms; some about optimizers; and a little about theorem
 provers.

The point of all these algorithms is _choice_. Given some data (or model generating data)
and some goals then there are many ways we use that data to achieve some, or all of those goals.
To say that another way, we have many choices on how we put the world together:

<img align=center src="../etc/img/dots1.png" width=500>

Some of those ways are quite silly:

<center>
<img align=center src="../etc/img/dots2.png" width=500>
</center>


- Optimizers can better control the data  miners.
    Several research has  improved data mining performance via optimizers that tune the control parameters of the data miner (See [Agrawal 2018a](REFS.md#agrawal-2018a),
   [Fu'18](REFS.md#fu-206), and [Tantithamthavorn et al.](REFS.md#Tan-2016a)).
- Data miners can better control the optimizers.
     For example,
[Majumder et al.](REFS.md#majumder-2018) used k-means clustering to divide up a complex text mining problem, then apply optimizers within each cluster. They report that this method speeds up their processing by up to three orders of magnitude.
- Data miners can act as optimizers.
     For example, [Chen et al.](REFS.md#chen-2018a)
show that their recursive descent bi-clustering algorithm (which is a data mining technique) out-performs traditional evolutionary algorithms for the purposes of optimizing SE models.
- Data miners and optimizers can be mashed up to (say) explore complex problems where one
  defines interesting regions where the other can reason faster, and better.
    For example, [Abdessalem et al.](REFS.md#abdollahi-2016) generate test cases for autonomous cars via a cyclic approach where an optimizer reflects on the output of data miners that reflect on the output of an optimizer (and so on).
- Theorem provers can be data generators for data miners or
  optimizers.
     When models come with many constraints, we can use theorem provers to [generate valid examples](REFS.md#chen-2018a);
- Optimizers can  improve theorem provers:
 Theorem provers deliver solutions in an order dictated  by their internal design. This means, when
     there are very many ways to solve constraints, theorem provers can take a while  to generate solutions that we prefer. In
  this case, a useful trick is to first , run theorem provers (a little) to get a sample of solutions; then  second
      run mutators and optimizers to [combine that sample in interesting ways](REFS.md#chen-2019).

When combined,
these
 AI tools
are  a rich tapestry within which software engineers can weave
around to
 achieve a variety of goals.


