##  Course Syllabus  
CSCI 330: File Organization and Processing  
Spring 1999

Instructor:  |  Dr. Stephen Smith, Assistant Professor of Computer Science.  
  
  
---|---  
Class:  |  Monday, 6:20 pm-8:55 pm, 25 January 1999-10 May 1999.  
  
  
Location:  |  Rosenstock room 223.  
  
  
Final Exam  
for graduating  
students:  
  
|  Self-scheduled between Thursday, 13 May 1999 and Saturday, 15 May 1999.  
  
  
Final Exam  
for returning  
students:  
  
|  Self-scheduled between Thursday, 13 May 1999 and Monday, 17 May 1999.  
  
  
Office Hours:  |  In Rosenstock room 328 (x3729, (301)-696-3729):  
Monday, Tuesday, and Wednesday, 5:45 pm-6:15 pm;  
Monday, Tuesday, and Wednesday, 9 pm-9:30 pm;  
or by appointment (most importantly!).  
  
  
Email address:  |  [sjsmith@hood.edu](mailto:sjsmith@hood.edu)  
  
  
Web address:  |  <http://yakko.hood.edu/~sjsmith/>  
  
###  Course Description (from the catalog):

Further study of data structures and an introduction to techiques of
structuring data on secondary storage devices. Topics include structure and
organization of files and file systems, indexing, external sorting and
merging, B-trees, hashing, and systems programming.

###  Prerequisites:

  * CSCI 287 (Data Structures); or 
  * permission of the instructor. 
Note that since Discrete Mathematics (MATH 205 or MATH 207) is a co-requisite
of CSCI 287, it is an implicit prerequisite for this course. Students who have
not successfully completed MATH 205 or MATH 207 should do so before attempting
CSCI 330.

###  Doing Your Own Work:

  * **Programs, homework assignments, and tests are meant to be your own work. You may only ask me for assistance on these items.** (You may ask Lab Workers for assistance with electromechanical problems at any time.) 
  * You **may not** share code. This means that you may not give or receive in any form -- oral, written, electronic, or otherwise -- from anyone -- another student, a written source such as a textbook or journal, the Net, or otherwise -- statements pertaining to the assignment, no matter how short or small, in Pascal, in C, in C++, in shell code, in any other programming language, or in pseudocode. Exceptions: You may use any code that I give you in class, out of class, or in the textbook used in this course. You may certainly ask me for exceptions for a small piece of code, provided that its source is clearly cited. 
  * All work **must** have the Honor Pledge ("I have neither given nor received unauthorized aid on this assignment.") written and signed on it. 

###  A realistic assessment of course requirements:

This course requires a substantial amount of work using computers. You are
encouraged to use the College's lab facilities, but you may use your own
computer and software resources if they are the same as we use in class. You
must learn to budget your time to allow for lab assignments, and you need to
develop a sense for when you are stuck and need help.

###  Required Text:

_File Structures: An Object-Oriented Approach with C++_. Folk, Michael J.;
Zoellick, Bill; and Riccardi, Greg. Addison-Wesley, Reading, Massachusetts,
1998. ISBN 0-201-87401-6.

###  Resource Text:

_Data Structures and Other Objects using C++_. Main, Michael and Savitch,
Walter. Addison-Wesley, Reading, Massachusetts, 1997. ISBN 0-8053-7470-1.

###  World Wide Web:

The World Wide Web page for this course
(<http://yakko.hood.edu/~sjsmith/csci330/>) has a link to this syllabus, and
will be updated with links to lecture notes and programming assignments as the
semester progresses.

###  Smoking:

I am very allergic to tobacco smoke (it gives me headaches and nausea). If I
see you on campus, and you are smoking, I will avoid you; don't take it
personally. Try not to smoke just before coming to class, and especially try
not to smoke just before coming to see me in my office.

###  Leave of absence:

I am taking a leave of absence from Hood during the 1999-2000 academic year.
As a result, you should not expect to be granted an incomplete grade for this
course.

###  Assignments:

  * _Reading Assignments_ :  
You will be expected to keep up with the readings by reading material before
the class at which it will be discussed. You do not serve yourself by being
exposed to these ideas for the first time in lecture. However, I don't expect
that you will understand everything that you have read. Keep notes in the
margins or in a notebook to remind you to ask them during lectures later.  
  

  * _Programming Assignments:_  
Roughly five programming assignments will require implementations in C++. I
recommend Borland C++, version 4.51 or greater, or Borland C++ Builder. Please
try not to use any strange features of Visual C++.

Programs will be due at the beginning of class. Details of program submissions
will be provided with each programming assignment, but will likely include
source files, test cases, and program listings.  
  

  * _Pointers:_  
Almost any serious programming project requires the use of pointers (or
arrays, which are simply pointers in disguise). Pointers require perfection.
Pointers can be a powerful tool for good, or a powerful tool for evil--the
final result is up to us. I really do dock 10 points off a programming project
for a mistake involving pointers.

Common pointer mistakes:

    * Dereferencing NULL. 
    * Allowing a pointer to point to memory that has been deallocated, and then dereferencing that pointer. 
    * Not initializing a pointer, and then dereferencing that pointer. 
    * Memory leaks (allocating memory and never deallocating it.) 
    * Deallocating the same memory twice. 
    * Accessing an array index that is out of range.    
Pointer protective measures:

    * Always initialize pointers to NULL as soon as a structure is allocated. 
    * Check that pointers assigned to the return value of `new` are non-NULL (with `set_new_handler()` or `assert()` if you like.) 
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
Homework assignments taken from or based on the text are planned for the
semester. Please do not hand in homework assignments and programming
assignments in the same envelope! (It will delay your grade.)  
  

  * _Tests:_  
An in-class midterm exam and an self-scheduled in-class final exam are
planned. They will be similar in form and content to the types of questions on
the homework assignments. They will contain questions that concentrate on the
most recent half of the course, but will assume mastery of material in
previous periods. (Thus, **the final is comprehensive**.) These tests are
intended to assess your mastery of the key concepts and relationships
investigated each half of the course.  
  

###  No Communes:

Do not under any circumstances submit any assignment through communes (Hood's
campus mail system). Slip it under my door, put it in the box on my door, or
place it in my departmental mailbox (in Rosenstock room 330) by hand.

###  Final grades by email:

Students who provide me with an email address may receive their final grade by
email at the end of the semester (although I haven't been doing well with this
lately).

###  Attendance:

Attendance is important. I will certainly make reasonable accommodations for
students who have conflicts with scheduled classes. Remember that absence from
class does not excuse you from assigned work.

###  Grading Policy:

  * Assignments are due on the dates specified in each assignment. You will be penalized 10 points for each class meeting an assignment is delayed, including the class at which the assignment is due. (If I excuse the lateness on some assignment you turn in, but mistakenly assess a late penalty, it's nothing personal: I just forgot. Remind me of your excuse and I'll correct the penalty.) No assignments will be accepted after Monday, 10 May 1999, at 9:30 pm.   
  

  * It is entirely possible that some programming projects will only be accepted on time. If so, I will clearly state this on each programming project write-up.   
  

  * I reserve the right to require written documentation for any excused absences or lateness. Students with disabilities are responsible for notifying the professor. All assignments are in English, and academic standards are applied equally to all students without regard to written, oral, or semantic capabilities in English.   
  

  * I will award partial credit for work done even if the result is incorrect; you must show all your intermediate work and clearly label your answer. I will deduct points for answers that do not make any sense at all; you should always check your work, even work done using the computer. 

###  Distribution of Weights in Grading:

(Numbers of graded assignments in each category may vary from this planned
amount.)  Homework Assignments  |  (8)  |  20%  
---|---|---  
Programming Projects  |  (4)  |  40%  
Exams  |  (2)  |  40%  
Class participation is important and will be considered in borderline cases.

###  Standard Disclaimer:

I reserve the right to change this syllabus.

###  Expectations:

  * Classes start on time and you should arrive on time. 
  * Ask questions in class and office hours. Please feel free to speak up if you did not understand something that was said. (If you don't understand something, I can only help you if I know that you don't understand it!) 
  * If you have a problem meeting some of the requirements for the class (for example, you are flying out of the country two days before the final exam), please let me know as soon as you become aware of the problem. The sooner I know, the more likely it is that I will be able to arrange a solution. 

###  Acknowledgments:

I have drawn heavily on the work of Jeff Martens in preparing for this course.

###  Very Tentative Schedule for Class Meetings:

M&S is Main & Savitch. FZR is Folk, Zoellick, and Riccardi.  #  |  Date  |
Topics  |  Assignment  
---|---|---|---  
1  |  01/25  |  Abstract Data Types  |  M &S, pp. 30-31, 102, 208  
2  |  02/01  |  OOD (Object-Oriented Design)  |  M&S, Chapter 1  
3  |  02/08  |  OOP (Object-Oriented Programming),  
C++ Input and Output,  
`assert.h` |  M&S, pp. 72-75;  
M&S, Chapter 14;  
FZR, Appendices C and D  
4  |  02/15  |  Mathematics Review and  
Introduction to File Structures  |  FZR, Chapters 1 and 2  
5  |  02/22  |  Fundamental File Structure Concepts  |  FZR, Chapters 3-5  
6  |  03/01  |  Organizing Files for Performance  |  FZR, Chapter 6  
7  |  03/08  |  Midterm review and catch-up  |  All of the above  
|  03/15  |  No class; Spring Break  |  
8  |  03/22  |  Midterm;  
Dr. Smith out of town  |  All of the above  
9  |  03/29  |  Indexing  |  FZR, Chapter 7  
10  |  04/05  |  Cosequential Processing and  
the Sorting of Large Files  |  FZR, Chapter 8  
11  |  04/12  |  Multilevel Indexing and B-Trees  |  FZR, Chapter 9  
12  |  04/19  |  Indexed Sequential File Access and  
Prefix B+-Trees  |  FZR, Chapter 10  
13  |  04/26  |  Hashing  |  FZR, Chapter 11  
14  |  05/03  |  Extensible Hashing  |  FZR, Chapter 12  
15  |  05/10  |  Final review and catch-up  |  All of the above  
|  Thursday  
05/13  
to Saturday  
05/15  |  Self-Scheduled Final  
(graduating and returning students)  |  All of the above  
|  Monday  
05/17  |  Self-Scheduled Final  
(returning students only)  |  All of the above  
  
* * *

_Mon Feb 15 14:32:06 EST 1999_

