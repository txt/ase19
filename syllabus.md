
<a name=top>&nsbp;<p> </a>
[home](http://tiny.cc/ase19#top) |
[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tim&commat;menzies.us
<br>
[<img width=900 src="https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png">](http://tiny.cc/ase19)<br>
[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) |
[src](http://menzies.us/fun) |
[submit](http://tiny.cc/ase19give) |
[chat](https://ase19.slack.com/)





# Syllabus

Spring 2018  
CSC 495 Special Topics in CS (11297)  
EB3, 2201  
Tues, Thus, 4:30 to 5:45pm   


## Catalog description:


General principles of programming languages. Parsing technology
such as  tokenization, parse trees, syntactic analysis, semantic
analysis, regular expressions. Higher-level concepts such as state
machines, type theory, lambda calculus, functions, closures and
objects, predicates, resolution theorem proving. Projects in building
programs using different paradigms.
Extra topics include domain-specific languages and various
languages used in industry and research; e.g. Python, Julia, Clojure,
Prolog, Elixr, Haskell, etc.


## General description:


Given a commercial software problem, how can we best select a
programming language for that problem? Further, given the ever-changing
nature of computer programming languages, what can we learn now
that will help us in the future to better understand future programming
languages? To answer these questions, this subject takes a pragmatic
and a theoretical approach,  from a modeling perspective.


Lectures will cover:

- Python programming
   - all exercises will be done in Python
- Parsing (basic)
   - technology including
     tokenization, BNF, parse trees, syntactic analysis, semantic analysis,
     regular expressions, macros
- Styles
   - From the Lopes text on programming styles
   - good-old-times, forth, monolith, cookbook, pipeline, reflective, spreadsheet, actors, map-reduce....
- Paradigms:
   - classical single-style languages such as LISP (functional), Smalltak (OO),  and Prolog (logical).  
   - theory of programming (lambda calculus, logic programming, finite-state machines, closures,
     predicates, etc
- Idioms (used in domain-specific languages)
   - From the Fowler text on DSL.
   - BNF, closure, decision table, dependency network, state machine, production rules....

As to the modeling perspective, students will use these tools to
build interpreters of domain-specific languages that are understandable
and maintainable by non-programmers.


## Staff

### Lecturer 

<img width=200 align=right  src="http://menzies.us/img/smalltimm.png">

+ Tim Menzies (Prof)
+ Office Hours: Tuesday, 2:00-4:00 and by request
+ Location of Office Hours: EB2 room 3298 
+ Github name: timm
+ Slack name: timm
+ E-Mail: tim.menzies@gmail.com 
  + Only use this email for private matters. All other class communication should be via the class Slack group [http://plm18.slack.com](http://plm18.slack.com).
+ Phone: 304-376-2859
       + **Do not use** this number, except in the most dire of 
          circumstances (best way to contact me is via email).

### Teaching assistant

<img width=200 align=right  src="http://ai4se.net/img/Patrick.png">

+ Tianpei (Patrick) Xia 
+ Office Hours: Wed 5pm to 7pm
+ Location of Office Hours: EB2 3240
+ Email: txia4@ncsu.edu
+ Github name: arennax
+ Slack name: patrick_xia 

<br clear=all>

## Details

### Group Mailing List

During term time, all communication will be via
the Slack group https://plm18.slack.com.
. Students are strongly encouraged to contribute their questions and answers to that shared resource.
+ Note that, for communication of a more private nature, contact the lecturer on the email shown above.


### Prerequisite

Note that this is a
**programming-intensive** subject. A programming
background is required in a contemporary language
such as Java or C/C++ or Python. Hence, the
prerequisite for this class is CSC326, Software
Engineering. Significant software industry
experience may be substituted, at the instructor's
discretion.  Students in this class will work in
Python, but no background knowledge of that language
will be assumed.

### Suggested texts

[Exercises in Programming Style](https://www.amazon.com/Exercises-Programming-Style-Cristina-Videira/dp/1482227371)     
by Cristina Videira Lopes    
Chapman and Hall/CRC; 1 edition (June 4, 2014)    
ISBN-10: 1482227371

- [code available on-line](https://github.com/crista/exercises-in-programming-style)
- [Introductory slides](http://gotocon.com/dl/goto-aar-2013/slides/CristinaVideiraLopes_ExercisesInStyle.pdf)


Domain-Specific Languages   
by Martin Fowler   
Addison-Wesley Professional; 1 edition (October 3, 2010)   
ISBN-10: 0321712943 

- [Catalog of DSL patterns](https://martinfowler.com/dslCatalog/)

Thinks Python   
by Allen Downey   
O'Reilly Media; 2 edition (December 28, 2015)   
ISBN-10: 1491939362

- [PDF version](http://greenteapress.com/thinkpython2/thinkpython2.pdf)
- [HTML version](http://greenteapress.com/thinkpython2/html/index.html)
- [Code samples](https://github.com/AllenDowney/ThinkPython2/tree/master/code)


### Expected Workload 

This is tools-based subject
and it is required that students learn and use those
tools (Python, repositories, etc).  Students MUST be
prepared to dedicate AT LEAST 5-8 working hours a
week to this class. 
Laboratory instruction is not included
in this subject (but the first three weeks will be
spent on some in-depth programming tutorials). Note
that the workload for masters and Ph.D. students
will be different (see above).

Sometimes, the lecturer/tutor will require you to attend a review session during their consultation  time. There, students may be asked to review
code, concepts, or comment on the structure of the course. Those sessions are mandatory and failure to attend will result in marks being deducted.

### Grading 

The following grade scale will be used: 

+ A+  (97-100), A (93-96), A-(90-92)
+ B+ (87-89), B (83-86), B-(80-82)
+ C+ (77-79), C (73-76), C-(70-72)
+ D+ (67-69), D (63-66), D-(60-62)
+ F (below 60).

Grades will be added together using:

+ Homeworks: 10 marks
+ Mid-term (Thursday March1, 6pm) : 20  marks
+ Final Exam (Tuesday, May8, 1pm to 3pm): 20 marks
+ Project: 50 marks. Details TBD.
      

### Project

Projects will be done in groups of three.
For a task specified by the lecturer, students will implement a perfect language that uses
the perfect mix of parser, style, paradigm, and idiom to generate a domain-specific
language that non CS-programmers can understand and use.


### Homework

Homeworks will be done individually. 

Homeworks must be submitted on the due date, otherwise will lose 1 mark late per day.

Until the end of February, homeworks may be resubmitted, after rework, to get obtain higher marks.

Pause.

So, yes, you must submit SOMETHING each week or lose marks. But if you submit and don't get the grade,
you CAN resubmit (at least, up to end of Feb). 

### Attendance

Attendance is extremely important for your learning
experience in this class. Once you reach three
unexcused absences, each additional absence will
reduce your attendance grade by 10%.

Except for officially allowed reasons, your presence in the class if required from day one. 
Late-comers will have to work in their own solo groups (to avoid disruptions to existing groups).

Note that absences for weddings (your own, or someone else's, is not an officially allowed reason).

Exceptions: this subject  will support students who are absent for any of the following
officially allowed reasons:

- Anticipated Absences (cleared with the instructor before the absence).
Examples of anticipated situations include
    - representing an official university function, e.g., participating in a professional meeting, as part of a judging team, or athletic team;
    - required court attendance as certified by the Clerk of Court;
    - religious observances as verified by the Division of Academic and Student Affairs (DASA).
    - Required military duty as certified by the student's commanding officer.
- Unanticipated Absences.  Excuses must be reported to the instructor not more than one week after the return to class.  Examples of unanticipated absences are:
      -  Short-term illness or injury affecting the ability to attend or to be productive academically while in class, or that could jeopardize the health of the individual or the health of the classmates attending.  Students must notify instructors prior to the class absence, if possible, that they are temporarily unable to attend class or complete assignments on time.
      -  Death or serious illnesses in the family when documented appropriately.  An attempt to verify deaths or serious illness will be made by the Division of Academic and Student Affairs.

That support will include changing the schedule of deliverables and/or (in extreme
case) different grading arrangements.


### Academic Integrity

Cheating will be punished to the full extent permitted. Cheating
includes plagerism of other people's work. All students will be working
on public code repositories and **informed reuse** is encouraged where
someone else's product is:

+ Imported and clearly acknowledged (as to where it came from);
+ The imported project is understood, and
+ The imported project is significantly extended.

Students are encouraged to read each others code and report **uninformed reuse**
to the lecturer. The issue will be explored and, if uncovered,
cheating will be reported to the university
and marks will be deducted if the person who is doing the reuse:

+ Does not acknowledge the source of the product;
+ Does not exhibit comprehension of the product when asked about it;
+ Does not significantly extend the product.

All students are expected to maintain traditional
standards of academic integrity by giving proper
credit for all work.  All suspected cases of
academic dishonesty will be aggressively pursued.
You should be aware of the University policy on
academic integrity found in the Code of Student
Conduct.
 
The  exams will be done individually.  Academic integrity is important.  Do not work together on the exams: cheating on either will be punished to the full extent permitted.  

### Disabilities

Reasonable accommodations will be made for students
with verifiable disabilities. In order to take
advantage of available accommodations, students must
register with Disability Services for Students at
1900 Student Health Center, Campus Box 7509,
919-515-7653. For more information on NC State's
policy on working with students with disabilities,
please see the Academic Accommodations for Students
with Disabilities Regulation(REG 02.20.01).

Students are responsible for reviewing the PRRs
which pertain to their course rights and
responsibilities. These include:
http://policies.ncsu.edu/policy/pol-04-25-05 (Equal
Opportunity and Non-Discrimination Policy
Statement), http://oied.ncsu.edu/oied/policies.php
(Office for Institutional Equity and
Diversity),http://policies.ncsu.edu/policy/pol-11-35-01
(Code of Student Conduct), and
http://policies.ncsu.edu/regulation/reg-02-50-03
(Grades and Grade Point Average).

### Non-Discrimination Policy

NC State University provides equality of opportunity
in education and employment for all students and
employees. Accordingly, NC State affirms its
commitment to maintain a work environment for all
employees and an academic environment for all
students that is free from all forms of
discrimination. Discrimination based on race, color,
religion, creed, sex, national origin, age,
disability, veteran status, or sexual orientation is
a violation of state and federal law and/or NC State
University policy and will not be
tolerated. Harassment of any person (either in the
form of quid pro quo or creation of a hostile
environment) based on race, color, religion, creed,
sex, national origin, age, disability, veteran
status, or sexual orientation also is a violation of
state and federal law and/or NC State University
policy and will not be tolerated.

+ Note that, as a lecturer, I am legally required to
  **report** all such acts to the campus policy.

Retaliation
against any person who complains about
discrimination is also prohibited. NC State's
policies and regulations covering discrimination,
harassment, and retaliation may be accessed at
http://policies.ncsu.edu/policy/pol-04-25-05 or
http://www.ncsu.edu/equal_op/. Any person who feels
that he or she has been the subject of prohibited
discrimination, harassment, or retaliation should
contact the Office for Equal Opportunity (OEO) at
919-515-3148.

### Other Information

Non-scheduled class time for field trips or
out-of-class activities are NOT required for this
class. No such trips are currently planned. However,
if they do happen then students are required to
purchase liability insurance. For more information,
see http://www2.acs.ncsu.edu/insurance/
