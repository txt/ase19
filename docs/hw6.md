<a name=top>&nbsp;<p> </a>
[home](http://tiny.cc/ase19#top) | 
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu 
<br> [<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br> 
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | 
[src](http://menzies.us/fun) | 
[submit](http://tiny.cc/ase19give) | 
[chat](https://ase19.slack.com/) 

## Homework 6

Now that you know how to do supervised discretization on one attribute:

- do it for all
- sort the attributes by how well they seperate the class variable
- find the best attribute on that sort
- divide the data on the ranges of that attribute.
- Recurse on each division.

For example, on the diabetes data set, we get:
```
$plas = -inf .. 120 *
|   $mass = -inf .. 26 
|   |   $plas = -inf .. 105 * : tested_negative (80)
|   |   $plas = 105 .. inf  : tested_negative (38)
|   $mass = 26 .. inf *
|   |   $age = -inf .. 28 *
|   |   |   $mass = -inf .. 30.8  : tested_negative (58)
|   |   |   $mass = 30.8 .. inf *
|   |   |   |   $pres = -inf .. 80 *
|   |   |   |   |   $pedi = -inf .. 0.471 * : tested_negative (56)
|   |   |   |   |   $pedi = 0.471 .. inf  : tested_negative (37)
|   |   |   |   $pres = 80 .. inf  : tested_negative (10)
|   |   $age = 28 .. inf 
|   |   |   $plas = -inf .. 89  : tested_negative (32)
|   |   |   $plas = 89 .. inf *
|   |   |   |   $preg = -inf .. 6 *
|   |   |   |   |   $pres = -inf .. 88 * : tested_negative (59)
|   |   |   |   |   $pres = 88 .. inf  : tested_negative (9)
|   |   |   |   $preg = 6 .. inf  : tested_positive (40)
$plas = 120 .. inf 
|   $plas = -inf .. 154 *
|   |   $mass = -inf .. 26.1  : tested_negative (29)
|   |   $mass = 26.1 .. inf *
|   |   |   $age = -inf .. 24  : tested_negative (39)
|   |   |   $age = 24 .. inf *
|   |   |   |   $pedi = -inf .. 0.512 *
|   |   |   |   |   $mass = -inf .. 39 *
|   |   |   |   |   |   $age = -inf .. 40 * : tested_negative (50)
|   |   |   |   |   |   $age = 40 .. inf  : tested_positive (33)
|   |   |   |   |   $mass = 39 .. inf  : tested_positive (15)
|   |   |   |   $pedi = 0.512 .. inf 
|   |   |   |   |   $age = -inf .. 29  : tested_negative (18)
|   |   |   |   |   $age = 29 .. inf * : tested_positive (43)
|   $plas = 154 .. inf 
|   |   $pedi = -inf .. 0.326  : tested_positive (44)
|   |   $pedi = 0.326 .. inf *
|   |   |   $pres = -inf .. 76 * : tested_positive (47)
|   |   |   $pres = 76 .. inf  : tested_positive (31)
```

and on the auto.csv data set I get: 

```
$displacement = -inf .. 151 *
|   $horsepower = -inf .. 70 
|   |   cylinders = 4 *
|   |   |   $model = -inf .. 76  : 29.2 (23)
|   |   |   $model = 76 .. inf *
|   |   |   |   $displacement = -inf .. 91 * : 37.39 (28)
|   |   |   |   $displacement = 91 .. inf  : 33.45 (19)
|   |   cylinders = 5  : 36.4 (1)
|   $horsepower = 70 .. inf *
|   |   cylinders = 3  : 20.55 (4)
|   |   cylinders = 4 *
|   |   |   $model = -inf .. 78 *
|   |   |   |   $weight = -inf .. 2219  : 28.25 (20)
|   |   |   |   $weight = 2219 .. inf *
|   |   |   |   |   $weight = -inf .. 2300  : 25.48 (18)
|   |   |   |   |   $weight = 2300 .. inf *
|   |   |   |   |   |   $weight = -inf .. 2855 * : 23.61 (36)
|   |   |   |   |   |   $weight = 2855 .. inf  : 20.29 (7)
|   |   |   $model = 78 .. inf 
|   |   |   |   $weight = -inf .. 2434  : 34.36 (17)
|   |   |   |   $weight = 2434 .. inf * : 28.56 (27)
|   |   cylinders = 5  : 20.3 (1)
|   |   cylinders = 6  : 25.63 (3)
$displacement = 151 .. inf 
|   cylinders = 4  : 25.73 (4)
|   cylinders = 5  : 25.4 (1)
|   cylinders = 6 
|   |   origin = 1 *
|   |   |   $model = -inf .. 78 *
|   |   |   |   $displacement = -inf .. 200  : 20.81 (13)
|   |   |   |   $displacement = 200 .. inf *
|   |   |   |   |   $displacement = -inf .. 232 * : 19.12 (25)
|   |   |   |   |   $displacement = 232 .. inf  : 17.32 (22)
|   |   |   $model = 78 .. inf  : 23.25 (14)
|   |   origin = 2  : 16.57 (3)
|   |   origin = 3  : 24.28 (4)
|   cylinders = 8 *
|   |   $model = -inf .. 76 *
|   |   |   $weight = -inf .. 3609  : 16.0 (10)
|   |   |   $weight = 3609 .. inf *
|   |   |   |   $weight = -inf .. 4341 * : 14.26 (36)
|   |   |   |   $weight = 4341 .. inf  : 12.89 (32)
|   |   $model = 76 .. inf  : 18.21 (25)
```

