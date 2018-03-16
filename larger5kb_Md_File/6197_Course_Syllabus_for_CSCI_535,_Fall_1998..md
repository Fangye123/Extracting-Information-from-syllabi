##  Course Syllabus  
CSCI 535: Object-Oriented Programming (OOP)  
Fall 1998

Instructor:  |  Dr. Stephen Smith, Assistant Professor of Computer Science.  
---|---  
Class:  |  Monday, 6:20 pm-8:55 pm, 24 August 1998-14 December 1998.  
Location:  |  Rosenstock room 123.  
Final Exam:  |  During the last class period:  
Monday, 14 December 1998, 6:20 pm-8:55 pm.  
Office Hours:  |  In Rosenstock room 328 (x3729, (301)-696-3729):  
Monday and Wednesday, 10:30 am-11:30 am;  
Monday and Thursday, 9 pm-9:20 pm;  
Thursday, 3 pm-4 pm;  
or by appointment.  
Email address:  |  [sjsmith@hood.edu](mailto:sjsmith@hood.edu)  
Web address:  |  <http://yakko.hood.edu/~sjsmith/>  
  
###  Course Description:

Intensive study of object-oriented programming using C++ for students already
familiar with C++. C++ relationships to C, abstract data types, object
instantiation, inheritance, polymorphism, member access control, templates,
overloaded operators, exception handling, use of C++ headers, and class
libraries will be studied. Use of software engineering environment tools for
object-oriented program implementation, testing, and maintenance will be
practiced. Emphasis upon programming for future reusability distinguishes this
course from a simple survey of language features of C++.

###  Prerequisites:

  * CSCI 504 (Algorithms and Programming II); or 
  * permission of the instructor. 
CSCI 535 assumes familiarity with some features of C++.

###  Doing Your Own Work:

  * **Homework assignments, programs, and tests are meant to be your own work. You may only ask me for assistance on these items.** (You may ask Lab Workers for assistance with electromechanical problems at any time.) 
  * You **may not** share code. This means that you may not give or receive in any form -- oral, written, electronic, or otherwise -- from anyone -- another student, a written source such as a textbook or journal, the Net, or otherwise -- statements pertaining to the assignment, no matter how short or small, in Pascal, in C, in C++, in shell code, in any other programming language, or in pseudocode. Exceptions: You may use any code that I give you in class, out of class, or in the textbook used in this course. You may certainly ask me for exceptions for a small piece of code, provided that its source is clearly cited. 

###  A realistic assessment of course requirements:

This course requires a substantial amount of work using computers. You are
encouraged to use the College's lab facilities, but you may use your own
computer and software resources if they are the same as we use in class. You
must learn to budget your time to allow for lab assignments, and you need to
develop a sense for when you are stuck and need help.

###  Required Text:

_C++: How to Program (Second Edition)_ , Deitel & Deitel, Prentice-Hall,
1998\.

###  World Wide Web:

The World Wide Web page for this course
(<http://yakko.hood.edu/~sjsmith/csci535/>) has a link to this syllabus, and
will (with any luck) be updated with links to lecture notes as the semester
progresses.

###  Smoking:

I am very allergic to tobacco smoke (it gives me headaches and nausea). If I
see you on campus, and you are smoking, I will avoid you; don't take it
personally. Try not to smoke just before coming to class, and especially try
not to smoke just before coming to see me in my office.

###  Assignments:

  * _Reading Assignments_ :  
You will be expected to keep up with the readings by reading material before
the class at which it will be discussed. However, I don't expect that you will
understand everything that you have read. You do not serve yourself by being
exposed to these ideas for the first time in lecture. Keep notes in the
margins or in a notebook to remind you to ask them during lectures later.

  * _Programming Assignments:_  
Roughly five programming assignments will require implementations in C++. I
recommend Borland C++, version 4.51 or greater, or Borland C++ Builder. Please
try not to use any strange features of Visual C++.  
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

###  No Communes:

Do not under any circumstances submit any assignment through communes (Hood's
campus mail system). Slip it under my door, put it in the box on my door, or
place it in my departmental mailbox (in Rosenstock room 330) by hand.

###  Final grades by email:

Students who provide me with an email address will receive their final grade
by email at the end of the semester.

###  Attendance:

Attendance is important. I will certainly make reasonable accommodations for
students who have conflicts with scheduled classes. Remember that absence from
class does not excuse you from assigned work.

###  Grading Policy:

  * Assignments are due on the dates specified in each assignment. You will be penalized 10 points for each class meeting an assignment is delayed, including the class at which the assignment is due. (If I excuse the lateness on some assignment you turn in, but mistakenly assess a late penalty, it's nothing personal: I just forgot. Remind me of your excuse and I'll correct the penalty.) No assignments will be accepted after Monday, 14 December 1998, at 9:20 pm. 
  * I reserve the right to require written documentation for any excused absences or lateness. Students with disabilities are responsible for notifying the professor. All assignments are in English, and academic standards are applied equally to all students without regard to written, oral, or semantic capabilities in English (see pages 228-229 in either the 1997-1998 or the 1998-1999 Catalog). 
  * I will award partial credit for work done even if the result is incorrect; you must show all your intermediate work and clearly label your answer. I will deduct points for answers that do not make any sense at all; you should always check your work, even work done using the computer. 

###  Distribution of Weights in Grading:

(Numbers of graded assignments in each category may vary from this planned
amount.)  Homework Assignments  |  (5)  |  20%  
---|---|---  
Programming Projects  |  (5)  |  40%  
Exams  |  (2)  |  40%  
Class participation is important and will be considered in borderline cases.

###  Standard Disclaimer:

I reserve the right to change this syllabus.

###  Expectations:

  * Classes start on time and you should arrive on time. 
  * Ask questions in class and office hours. Please feel free to speak up if you did not understand something that was said. (If you don't understand something, I can only help you if I know that you don't understand it!) 
  * If you have a problem meeting some of the requirements for the class (for example, you are flying out of the country two days before the final exam), please let me know as soon as you become aware of the problem. The sooner I know, the more likely it is that I will be able to arrange a solution. 

###  Acknowledgments:

I have drawn heavily on the work of John Boon in preparing for this course.

###  Very Tentative Schedule for Class Meetings:

#  |  Date  |  Topics  |  Assignment  
---|---|---|---  
1  |  08/24  |  Syllabus; Review of C++ Basics  |  Chapters 1-4  
2  |  08/31  |  More Review of C++ Basics; Review of Classes  |  Chapters 5-6  
|  09/07  |  No class; Labor Day  |  
3  |  09/14  |  Classes: Constants, Friends, `this` |  Chapter 7.1-7.5  
4  |  09/21  |  Classes: `new, delete, static`;  
Data Abstraction and Information Hiding;  
Container Classes and Iterators;  
Proxy Classes  |  Chapter 7.6-7.10  
5  |  09/28  |  Operator Overloading  |  Chapter 8  
6  |  10/05  |  Inheritance  |  Chapter 9.1-9.6  
7  |  10/12  |  Midterm review and catch-up  |  All of the above  
8  |  10/19  |  Midterm  |  All of the above  
9  |  10/26  |  Inheritance continued  |  Chapter 9.7-9.15  
10  |  11/02  |  Virtual functions and polymorphism  |  Chapter 10  
11  |  11/09  |  Templates  |  Chapter 12  
12  |  11/16  |  Exception handling  |  Chapter 13  
13  |  11/23  |  C++ Stream Input/Output  |  Chapter 11  
14  |  11/30  |  File Processing  |  Chapter 14  
15  |  12/07  |  Final review and catch-up  |  All of the above  
16  |  12/14  |  Final  |  All of the above  
  
* * *

_Mon Aug 31 10:01:32 EDT 1998_

