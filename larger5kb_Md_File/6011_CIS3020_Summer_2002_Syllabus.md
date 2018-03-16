Introduction to Computer Science  
Summer, 2002  

#  CIS3020 Syllabus

* * *

## Course Overview

This course introduces fundamental concepts of computer science and the art of
programming from an OO (object-oriented) perspective. Problem-solving skills
and the principles of software engineering will be stressed: you will learn
how to analyze a problem, formulate a solution, express that solution in a
programming language, and test the resulting software. We will harness the
powers of **A PIE** \-- Abstraction, Polymorphism, Inheritance, and
Encapsulation -- to write elegant, easily maintained, and efficient programs.

We will devote a significant quantity of time to visually modeling software
constructs using both the UML (Unified Modeling Language) and DaRN! (Dave's
Runtime Notation!). These models will facilitate an understanding of
relationships between classes, how objects interact to solve problems, and
scoping related issues.

Other topics include an introduction to assembly level machine organization,
machine level representation of data, an overview of programming paradigms,
virtual machines, introduction to language translation, declarations and
types, using a simple graphics API, abstraction mechanisms, fundamental
programming constructs, algorithms, recursion, and fundamental data
structures. In short, this course lays the foundations upon which your future
computer science studies will be built.

### Warning

This is **not** "the Java course" -- that would be CGS 2414: Programming with
Java. While we will use Java as our exemplar programming language, it is only
as a means to an end, not the end in and of itself. Accordingly, our coverage
of Java technologies will be incomplete; we will cover only those aspects
necessary to illustrate the broader principles that are the true focus of this
course.

Students are hereby advised that this is a challenging course intended for
computer science majors -- regardless of your actual major, you are expected
to approach the course as if you were a CS major. Prior programming
experience, while not required, is strongly recommended. The most common
comment made by students who drop/fail CIS 3020 is, "you should make the Java
course a prerequisite!"

## Instructional Staff

Instructor  

* * *  
  
---  
Name | E-mail | Office | Office Hours | Phone  
Dave Small | dts@cise.ufl.edu | CSE E422 | MWF 5th (2:00-3:15pm) | 392-6839  
  
Teaching assistants  

* * *  
  
Amitoj Likhari | alikhari@cise.ufl.edu | CSE E426 | MWF 4th (12:30-1:45pm) |  
Milan Lazovic | mlazovic@cise.ufl.edu | CSE E426 | M 5th (2:00-3:15pm), R
2-3rd (9:30-12:15pm) |  
Zhuomin Gao | zgao@cise.ufl.edu | CSE E426 | MF 2nd (9:30-10:45), W 6th
(3:30-4:45pm) |  
  
  

##  Administrivia

**Homepage:** [http://www.cise.ufl.edu/~dts/cis3020/](./index.html)

**Prerequisites:** MAC 3311 or MAC 3223

**Required textbook:** An Intoduction to Programming and Object Oriented
Design Using Java

by Nino and Hosch (Wiley, 2000)

ISBN 0-471-35489-9

**Supplemental books** (not required): for some recommendations, see [ Dave's
Java Resources](http://www.cise.ufl.edu/~dts/resources/java_resources.html)

### Exam schedule (tentative)

**Exam 1:** Week 4 -- Mon 6/3

**Exam 2:** Week 8 -- Mon 7/8

**Final exam:** Week 12 -- Wed 8/7

##  Philosophy and policy

One will learn to program only by programming. It is not enough to attend
lectures, study the notes, and read a book -- _one must practice._ To help you
assimilate the material, we will provide opportunities to apply the concepts:
in addition to ungraded homework assignments, a portion of the lecture time
will be devoted to in-class exercises and discussion. You are expected to be
prepared for and participate in all in-class activities as well as complete
all homework assignments. You are also expected to supplement those formal
exercises with self directed study and to seek assistance in a timely manner.

###  Testing

We will monitor your progress by testing you through out the semester. There
will be three 1 period exams (including the final exam) and weekly QSs (quiz
sessions -- note: QS will be pronounced "cues"). The quizzes will be held in a
small computer lab in the basement of the CSE building and most will require
you to produce a well engineered and working piece of software. Because the
seating in the lab is limited, during the first week of class you will
register for a two period block during which you will take your quiz each
week.

###  Attendance

You are expected to attend all class meetings (which includes the weekly quiz
sessions). You are responsible for all materials covered and announcements
made in the class meetings. Should you miss class, it is your responsibility
to determine what you missed _from your fellow students_ \-- lectures will not
be repeated. The TAs and I will be glad to help you resolve any question you
may have, but only if you have first studied the material you acquired from
another student.

###  Make-ups

As a rule: _there are no make-ups._ In certain unusual cases approved by the
instructor -- e.g., jury duty, military service, documented illness, etc. --
accomodations will be made (e.g., in the case of a missed exam, letting the
final exam grade count twice). It is the student's responsibility to
immediately contact the instructor and supply documentation in a timely
manner.

###  Good faith effort

As previously noted, this is a challenging course. A _good faith effort_ to
succeed is officially defined as attempting all quizzes and bonus exercises,
as well as regularly (at least once per week) seeking help from the CIS 3020
instructional staff (instructor and support TAs) \-- there will be **no**
exceptions to this definition.

_Supportive letters and petition endorsements will **only** be written for
students who have made a good faith effort._ If your life would be adversely
affected by a poor grade or a "drop" -- e.g., you are on academic probation,
required to carry a certain number of hours because of a visa, have
scholarship requirements, etc. -- ensure that you make a good faith effort to
succeed.

###  Accomodations of students with disabilities

Students requesting classroom accomodation must first register with the Dean
of Students Office. The Dean of Students Office will provide documentation to
the student who must then provide this documentation to the instructor when
requesting accomodations. _Students who will be requesting accomodations must
notifiy the instructor during the first week of class_ that they shall be
making the request and provide the documentation in a timely manner.

##  Final grades

Your final grade will be based on the number of _grade points_ you have at the
end of the semester using the standard scale (100-90 = A, 89-87 = B+, 86-80 =
B, 79-77 = C+, 76-70 = C, 69-67 = D+, 66-60 = D, 59-0 = E). During the
semester you will accumulate _earned points_ in categories weighted as
follows:

22% |  mid term exam 1  
---|---  
22% |  mid term exam 2  
32% |  final exam  
24% |  quiz sessions  
up to 5% |  bonus exercises  
  
Notice that there is a distinction between _grade points_ and _earned points_
\-- _grade points_ will be computed from your _earned points_ and _final exam
score_ using the following algorithm:

    
    
    if (( _earned points_  < 87) or ( _earned points_  < _final exam score_ ))
    then _grade points_ := _earned points_
    else _grade points_ := maximum( _final exam score_ , 86.99 )     
    

In plain English that means: if you want to earn _higher_ than a B, you must
not only do well in the course over-all, but you must also do well on the
final exam. To earn an A, you must earn at least 90 points and score at least
a 90% on the final exam. To earn a B+, you must earn at least 87 points and
score at least an 87% on the final exam. This policy ensures that only those
students who have a sustained record of excellence will be awarded the highest
grades.

IFF you have made a good faith effort to succeed (as previously defined), but
have accumulated less than 60 _earned points_ , you will none the less receive
a D in the course -- in such cases you will automatically receive sufficient
bonus points to raise your grade from an E to a D. There will be **no** other
adjustments made to grades -- it is your responsibility to _earn_ the grade
you desire.

## Academic dishonesty

ACADEMIC DISHONESTY WILL NOT BE TOLERATED. Unless otherwise explicitly stated,
assignments are individual projects. You are expected to do your own work;
individuals who misrepresent work as being their own, submit fabricated data,
or otherwise engage in anti-intellectual behavior will be dealt with severely
and reported to the Office for Student Judicial Affairs. You may freely use
any code presented in the textbook, provided by your instructor, or authored
by yourself. You are prohibited from using code from any other source without
written permission from the instructor. Remember, sharing your work with
another student is a violation of the honor code. For more information consult
the Academic Honesty Guidelines section of the University of Florida's Student
Guide at <http://oss.ufl.edu/STG/>

## Comments

My goal is simple: to help you learn -- both inside and outside the classroom.
If you have questions, there is no excuse for not getting help. The TAs,
consultants, and I all hold office hours just for the purpose of helping you,
either one-on-one or in small groups. No matter how busy we may look, during
office hours, you have priority over everything else. If you have a problem or
question, come by and we'll talk about it -- don't put it off.

## Modifications

This document is subject to revision as needed. All modifications will be
noted in this section.

  * _200205.26_ \- TA office hours and contact information updated. 

  

* * *

This website is an original work, Copyright  (C) 2002 by Dave Small. All
rights reserved.

