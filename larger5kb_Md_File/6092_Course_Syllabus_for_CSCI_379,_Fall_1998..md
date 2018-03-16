##  Course Syllabus  
CSCI 379: Computer Algorithms  
Fall 1998

Instructor:  |  Dr. Stephen Smith, Assistant Professor of Computer Science.  
---|---  
Class:  |  Thursday, 6:20 pm-8:55 pm, 27 August 1998-3 December 1998.  
Location:  |  Rosenstock room 218.  
Final Exam:  |  Self-scheduled during the examination period:  
Friday, 11 December 1998-Tuesday, 15 December 1998.  
Office Hours:  |  In Rosenstock room 328 (x3729, (301)-696-3729):  
Monday and Wednesday, 10:30 am-11:30 am;  
Monday and Thursday, 9 pm-9:20 pm;  
Thursday, 3 pm-4 pm;  
or by appointment.  
Email address:  |  [sjsmith@hood.edu](mailto:sjsmith@hood.edu)  
Web address:  |  <http://yakko.hood.edu/~sjsmith/>  
  
###  Course Description:

Discussion of the application of analysis techniques and design strategies to
non-numeric algorithms which act on data structures and to the selection of
methods for data manipulation. Students in this course will review
mathematical tools used to describe portions of algorithms and to analyze the
performance characteristics of algorithms. In the future, when presented with
an algorithmic or data storage problem, the student should either be able to
use an already-invented data structure or algorithm, adapt a data structure or
algorithm to the problem at hand, or use the principles learned in this course
to create a new data structure or algorithm.

###  Prerequisites:

  * CSCI 287 (Data Structures), MATH 207 (Discrete Mathematics), **and**  
(MATH 200 (Applied Calculus) or MATH 201 (Calculus 1)); or

  * permission of the instructor. 

###  Honor Code:

  * All work **must** have the Honor Pledge ("I have neither given nor received unauthorized aid on this assignment.") written and signed on it. 
  * **Homework assignments, programs, and tests are meant to be your own work. You may only ask me for assistance on these items.** (You may ask Lab Workers for assistance with electromechanical problems at any time.) 
  * You **may not** share code. This means that you may not give or receive in any form -- oral, written, electronic, or otherwise -- from anyone -- another student, a written source such as a textbook or journal, the Net, or otherwise -- statements pertaining to the assignment, no matter how short or small, in Pascal, in C, in C++, in shell code, in any other programming language, or in pseudocode. Exceptions: You may use any code that I give you in class, out of class, or in the textbook used in this course. You may certainly ask me for exceptions for a small piece of code, provided that its source is clearly cited. 

###  Required Text:

_Introduction to Algorithms_ , Cormen, Leiserson, and Rivest, The MIT Press,
McGraw-Hill, 1992. (Most Recent Printing)

###  Assignments:

  * _Reading Assignments_ :  
You will be expected to keep up with the readings by reading material before
the class at which it will be discussed. You do not serve yourself by being
exposed to these ideas for the first time in lecture. However, I don't expect
that you will understand everything that you have read. Keep notes in the
margins or in a notebook to remind you to ask them during lectures later.

  * _Programming Assignments:_  
Four programming assignments will require implementations in Pascal, C, or C++
(at your option.) I recommend Borland C++, version 4.51 or greater. Those
wishing to use a program language other than C or C++ must get permission from
the instructor. Please do not use any strange features of Visual C++.  
Programs will be due at the beginning of class. Details of program submissions
will be provided with each programming assignment, but will likely include
source files, test cases, and program listings.  
  
_Pointers:_  
Almost any serious programming project requires the use of pointers (or
arrays, which are simply pointers in disguise). **Pointers require
perfection.** Pointers can be a powerful tool for good, or a powerful tool for
evil--the final result is up to us. I really do dock 10 points off a
programming project for a mistake involving pointers.  
  
Common pointer mistakes:

    * Dereferencing NULL. 
    * Allowing a pointer to point to memory that has been deallocated, and then dereferencing that pointer. 
    * Not initializing a pointer, and then dereferencing that pointer. 
    * Memory leaks (allocating memory and never deallocating it.) 
    * Deallocating the same memory twice. 
    * Accessing an array index that is out of range.    
Pointer protective measures:

    * Always initialize pointers to NULL as soon as a structure is allocated. 
    * Check that pointers assigned to the return value of new or malloc() are non-NULL (with set_new_handler() or assert() if you like.) 
    * Check array indices before using them. 
    * **Think!** Does this function work in all cases? Do I check for NULL pointers? Are all the pointers guaranteed to point either at NULL or at a structure when the function is over? When deallocating, are all pointers to this structure pointed elsewhere?    
_"But it works on my computer!"_  
Many errors, especially pointer errors, are intermittent-whether they occur or
not is dependent on what happens to be in memory at a particular time. The
only way to prevent such errors is to be careful.  
  
_True story:_  
I actually introduced such a mistake into my Ph.D. implementation. In Fall
1997, the mistake delayed the release of a commercial product.

  * _Homework Assignments:_  
Roughly five homework assignments based on the text are planned for the
semester. Please do not hand in homework assignments and programming
assignments in the same envelope!

  * _Tests:_  
An in-class midterm exam and an in-class final exam are planned. They will be
similar in form and content to the types of questions on the homework
assignments. They will contain questions that concentrate on the most recent
half of the course, but will assume mastery of material in previous periods.
These tests are intended to assess your mastery of the key concepts and
relationships investigated each half of the course.

###  A realistic assessment of course requirements:

This course requires a substantial amount of work using computers. You are
encouraged to use the College's lab facilities, but you may use your own
computer and software resources if they are the same as we use in class. You
must learn to budget your time to allow for lab assignments, and you need to
develop a sense for when you are stuck and need help.

###  World Wide Web:

The World Wide Web page for this course
(<http://yakko.hood.edu/~sjsmith/csci379/>) has a link to this syllabus, and
will (with any luck) be updated with links to lecture notes as the semester
progresses.

###  Smoking:

I am very allergic to tobacco smoke (it gives me headaches and nausea). If I
see you on campus, and you are smoking, I will avoid you; don't take it
personally. Try not to smoke just before coming to class, and especially try
not to smoke just before coming to see me in my office.

###  No Communes:

Do not under any circumstances submit any assignment through communes (Hood's
campus mail system). Slip it under my door, put it in the box on my door, or
place it in my departmental mailbox (in Rosenstock room 330) by hand.

###  Final grades by email:

Students who provide me with an email address will receive their final grade
by email at the end of the semester.

###  Attendance:

Attendance is mandatory. Excessive absences will be reported to the
Registrar's office in accordance with College academic policies. If you are
not able to come to class, you need to contact the Dean of Students or myself.
Remember that absence from class does not excuse you from assigned work.

###  Grading Policy:

  * Assignments are due on the dates specified in each assignment. You will be penalized 10 points for each class meeting an assignment is delayed, including the class at which the assignment is due. (If I excuse the lateness on some assignment you turn in, but mistakenly assess a late penalty, it's nothing personal: I just forgot. Remind me of your excuse and I'll correct the penalty.) No assignments will be accepted after Thursday, 3 December 1998, at 9:20 pm. 
  * I reserve the right to require written documentation for any excused absences or lateness. Students with disabilities are responsible for notifying the professor. All assignments are in English, and academic standards are applied equally to all students without regard to written, oral, or semantic capabilities in English. 
  * I will award partial credit for work done even if the result is incorrect; you must show all your intermediate work and clearly label your answer. I will deduct points for answers that do not make any sense at all; you should always check your work, even work done using the computer. 

###  Distribution of Weights in Grading:

(Numbers of graded assignments in each category may vary from this planned
amount.)  Homework Assignments  |  (5)  |  30%  
---|---|---  
Programming Projects  |  (4)  |  30%  
Exams  |  (2)  |  40%  
Class participation is important and will be considered in borderline cases.

###  Standard Disclaimer:

I reserve the right to change this syllabus.

###  Expectations:

  * Classes start on time and you should arrive on time. 
  * Ask questions in class and office hours. Please feel free to speak up if you did not understand something that was said. (If you don't understand something, I can only help you if I know that you don't understand it!) 
  * If you have a problem meeting some of the requirements for the class (for example, you are flying out of the country two days before the final exam period), please let me know as soon as you become aware of the problem. The sooner I know, the more likely it is that I will be able to arrange a solution. 

###  Acknowledgments:

I have drawn heavily on the work of Dave Mount in preparing for this course.
All lecture notes will carry an appropriate copyright notice. This syllabus is
drawn from Dave Mount's _CMSC 451: Algorithm Design_ lecture notes. Copyright,
David M. Mount, 1995, Dept. of Computer Science, University of Maryland,
College Park, MD 20742. These lecture notes were prepared by David Mount for
the course CMSC 451, Design of Computer Algorithms, at the University of
Maryland, College Park. Much of the material presented here has been adapted
from the course text, _Introduction to Algorithms_ , by T. H. Cormen, C. E.
Leiserson, and R. L. Rivest, McGraw-Hill and MIT Press, 1995\. Permission to
use, copy, modify, and distribute these notes for educational purposes and
without fee is hereby granted, provided that this copyright notice appear in
all copies.

###  Very Tentative Schedule for Class Meetings:  
("Section N.0" refers to the Introduction to Chapter N)

#  |  Date  |  Topics  |  Assignment  
---|---|---|---  
1  |  08/27  |  Syllabus; Introduction to Algorithms;  
Closest-Pair Problem; Asymptotics;  
Divide-and-Conquer  |  Chapters 1-4;  
Section 35.4  
2  |  09/03  |  Recurrences; Sorting;  
Counting Sort; Radix Sort  |  Chapters 7-10  
3  |  09/10  |  Graph Algorithms;  
Breadth-First and Depth-First Search  |  Sections 5.4-5.5;  
Sections 23.1-23.3  
4  |  09/17  |  DAGs and Topological Sort;  
Articulation Points  |  Sections 23.3-23.4  
5  |  09/24  |  Minimum Spanning Trees  |  Chapter 24  
6  |  10/01  |  Shortest Paths;  
Applications of Graph Algorithms  |  Chapter 25;  
Section 37.2  
|  10/08  |  No class; Midterm Break  |  
7  |  10/15  |  All Pairs Shortest Paths;  
Midterm review  |  Sections 26.0-26.2;  
All of the above  
8  |  10/22  |  Midterm;  
The 0-1 Knapsack Problem  |  All of the above;  
Section 16.0;  
Section 17.2  
9  |  10/29  |  Longest Common Subsequence;  
NP-Completeness: Languages and NP  |  Section 16.3;  
Sections 36.0-36.2  
10  |  11/05  |  NP-Completeness: Reductions;  
Satisfiability and Independent Set  |  Sections 36.3-36.5  
11  |  11/12  |  Clique, Vertex Cover, Dominating Set;  
Subset Sum  |  Sections 36.0-36.5  
12  |  11/19  |  Approximation Algorithms;  
k-Center Approximation;  
TSP Approximation  |  Sections 37.0-37.2  
|  11/26  |  No class; Thanksgiving  |  
13  |  12/03  |  Set-Cover Approximation;  
Final review  |  Sections 37.0-37.3;  
All of the above  
  
* * *

_Thu Aug 27 16:54:32 EDT 1998_

