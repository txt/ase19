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

### Set up

Form groups  (pairs for 591, singletons for 791).

Create a github repo (in public github) and make a directory `hw/1`.

Each group pick your favorite programming language. Something with
high-level scripting facilities i (python, ruby, javascript, java,
coffeescript, whatever). Note that if you use Python, you can get
coding help from lecturer/tutor. Otherwise, you are on your own.

- Pick something that you are _productive_ together.

### What to Hand in

- Place your code  in the `hw/1` directory.
- Place a text file `hw/1/out.txt` in that same directory, showing a transcript of it work.
- Place a link to that code in http://tinv.cc/ase19give

### What to do

Write a class called `Col` with subclass `Num`, `Sym`, and `Some`

In `Num`, write code that read a number one at a time, and incrementally
update mean and standard deviation.  For pseudocode on how to do
that, see 
[Num](http://menzies.us/fun/num).

-  you'll only need down to code line 35.

Test your code:

- build a list of 100 random numbers
- add the list, one at a time to a `Num`
   - every ten numbers, cache the mean and standard deviation
   - i.e. that cache is two lists of means and standard deviations seen at "_i_" = 10,20,30, etc
- now delete those numbers, one at a time, from that `Num`. 
   - every ten numbers check that you are getting the same thing as the cache
- For a sample of that code, in another language, see 
  [\_num](https://github.com/timm/fun/blob/master/src/numok.fun#L15-L31)

Caution:

- There is a known bug in the `NumLess` function of 
   [Num](http://menzies.us/fun/num). Those sums go wrong when the sample is small and sum is small (due to
   some deep issues with the representation of reals... we won't be able to fix that).
- So when deleting the numbers, run from 100 down to 10 then stop.

