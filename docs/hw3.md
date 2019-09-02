<a name=top>&nbsp;<p> </a>
[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 

## Homework 3

Here's the new work (in red)

<img src="http://yuml.me/diagram/plain;dir:lr/class/[Tbl|oid|read(file); dump();]++rows-1..*[Row|oid; cells:list; cooked:list; dom = 0],[Tbl]++cols-1..*[Col|oid; col; txt ], [Col]^-[Num| hi = -10^32 ; lo = 10^32 ; m2 = 0; mu = 0; n = 0; sd = 0; |Num1()],[Col]-[note: one Sym or Num for each column in the rows{bg:orange}], [Col]^-[Sym|n=0;mode;most; cnt: Dict|SymEnt(){bg:red}],[Sym]-[note:entropy is analagous to standard deviation{bg:orange}],[Abcd|rx;data;a;b;c;d;yes=0;no=0;known;{bg:red}],[Abcd]-[note: reports performance results when a classifeis tested{bg:orange}]">

Create new classes 
[Sym](http://menzies.us/fun/sym) and 
[Abcd](http://menzies.us/fun/abcd).

- `Sym` is like `Num`, but it keeps a count `cnt` of symbols in a row. 
   - The most frequently seen symbol is the `mode`.
   - `Sym` can report the `entropy` of the symbols  in a column. Given `n` entries n a column
     with symbols occuring at frequency `n1,n2,...`
     then the entropy `e` of a column is:
     - p<sub>i</sub> = n<sub>i</sub>/n
     - e = - &sum;<sub>i</sub> p<sub>i</sub>log<sub>2</sub>(p<sub>1</sub>)
     - Entropy is like standard deviation, but for symbols:
       - the lower the standard deviation, the less variety in the numbers
       - the lower the entropy, the less variety in the symbols
