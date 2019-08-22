<a name=top>&nbsp;<p> </a>
[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 


## Homework 1

Due 4pm Thursday.

This one's not hard. More to practice how groups worth together.

Form groups  (pairs for 591, singletons for 791).

Create a github repo (in public github) and make a directory `hw/1`.

Each group pick your favorite programming language. Something with
high-level scripting facilities i (python, ruby, javascript, java,
coffeescript, whatever). Note that if you use Python, you can get
coding help from lecturer/tutor. Otherwise, you are on your own.

- Pick something that you are _productive_ together.

Write a class called `Col` with subclass `Num`, `Sym`, and `Some`

In `Num`, write code that read a number one at a time, and incrementally
update mean and standard deviation.  For pseudocode on how to do
that, see [Num](http://menzies.us/fun/num).

- Hint: you'll only need down to code line 35.

Test your code:

- build a list of 100 random numbers
- add the list, one at a time to a `Num`
   - every ten numbers, cache the mean and standard deviation
- now delete those numbers, one at a time, from that `Num`. 
   - every ten numbers check that you are getting the same thing as the cache

Submit your code

- place it in `hw/1`
- Place a link to that code in http://tinv.cc/ase19give

That's all!

