[ **CSCI  2270 Computer Science 2: Data Structures**  
Spring 2002  
Karl Winklmann ](handout01.html)

|    |

  

<http://www.cprogramming.com/>  
<http://cppreference.com/>  
<http://www.cplusplus.com/ref/>  
<http://www.google.com/>[  
<http://www.yahoo.com/>[  

[Syllabus and schedule](handout01.html#Schedule and syllabus)  
[This week's notes](notes15.html)  
[Table of contents](contents.html)  
  
  
---|---|---  
  
# General course information

Monday, January 14, 2002

* * *

[Next page](assign01.html)

* * *

This page is on the web at <http://www.cs.colorado.edu/~karl/2270.spring02/>.

On this page: Purpose of course | Staff | Textbooks | Schedule and syllabus |
Grading policies | Collaboration

* * *

## Purpose of course

This course will cover three subjects:

### Data structures

Methods for organizing data in computer memory. How to choose the best ones
depending on properties of the data and requirements for access and updates.

### C++

Building data structures out of C++ arrays and pointers. Using classes and
objects to stay organized and create reusable software.

### Productivity tools

An integrated editing-compiling-debugging environment and project management
software. We will use such tools in a Unix environment.

## Staff

There are [pictures](pictures.html).

### Instructor

Karl Winklmann, ECOT 725, [karl@cs.colorado.edu](mailto:karl@cs.colorado.edu),
phone 303-492-6380. Office hours MWF 11-11:50 and by appointment. To make an
appointment call or send email.

### Teaching Assistants

A separate page with information about the recitations and such is at
[http://csel.cs.colorado.edu/~simek/csci2270/](http://csel.cs.colorado.edu/~simek/csci2270).

    
    
    R021 02:00pm-03:15pm T ECCR 1B56   Ryan T. King
    R022 03:30pm-04:45pm T ECCR 1B56   Seth Pensack-Rinehart
    R023 05:00pm-06:15pm T ECCR 1B56   Sean Murphy
    
    R031 09:30am-10:45am T ECCR 1B56   David Ellis
    R032 11:00am-12:15pm T ECCR 1B56   Patrick Simek
    R033 12:30pm-01:45pm T ECCR 1B56   Jayson Ryckman
    

## Textbooks

### Required:

Michael Main and Walter Savitch, Data Structures and Other Objects Using C++,
Second Edition, Addision Wesley, ISBN 0-202-70297-5.

### Recommended:

Mike Loukides and Andy Oram, Programming with GNU Software, O'Reilly and
Associates, Inc., ISBN 1-56592-112-7.

## Schedule and syllabus

The timing of the lecture topics may shift somewhat depending on how quickly
we cover some of the material. [Note added later: There have been some minor
adjustments since this page was first posted.] Due dates for assignments and
dates of exams won't change.

* * *  
  
---  
  |  _  Week of ..._ |  _  Class_ |  _  Recitations_ |  _  Assignments_  
  
* * *  
  
_1._ |  January  14-18  |  [ Overview.  
Objects and classes. ](notes01.html) |  Logistics. Basic Unix and `emacs`.  |
[ Assignment 1 ](assign01.html) handed out ("CombinationLock", using classes
and objects).  
_2._ |  January  23-25  |  [ Objects and classes, continued. ](notes02.html) |
More Unix, submission of assignments.  |  _Assignment  1 due Friday, Jan 25\.
_  
_3._ |  Jan  28-30, Feb 1  |  [ Container classes. ](notes03.html) |
Permissions, `RCS`, and `emacs`.  |  [ Assignment 2 ](assign02.html) handed
out ("PhoneBook", using container classes).  
_4._ |  February  4-8  |  [ Dynamic arrays. ](notes04.html) |  Interactive
debugging with `gdb`.  |  _Assignment  2 due Friday, Feb 8._  
_5._ |  February  11-15  |  [ Pointers and linked lists. ](notes05.html) |
TBD  |  [ Assignment 3 ](assign03.html) handed out ("CatalogBrowser", using
linked lists).  
_6._ |  February  18-22  |  [ Stacks and trees. ](notes06.html) |  TBD  |
_Assignment  3 due Friday, Feb 22\. _  
_7._ |  Feb  25-27, Mar 1  |  [ Trees, continued. Recursion. ](notes07.html) |
_Tuesday, Feb  26: [ Lab exam 1 ](labexam1.html) (on linked lists). _ |  [
Assignment 4 ](assign04.html) handed out ("ArithmeticExpressions", using
stacks, trees, recursion).  
_8._ |  March  4-8  |  [ Recursion, continued.  
Templates. ](notes08.html) |  TBD  |  _Assignment  4 due Friday, Mar 8\. _  
_9._ |  March  11-15  |  _Monday, March  11: [ Midterm Exam. ](midterm.html) _  
[ Search trees. ](notes09.html) |  TBD |  [ Take-home exam 1 ](takehome1.html)
handed out ("MakeIndex", using trees).  
_10._ |  March  18-22  |  [ Priority queues.  
Heapsort.  
Limits on sorting. ](notes10.html) |  TBD  |  _Take-home exam  1 due Monday
(!), March 18\. _  
  
March 25-29 Spring Break  
  
_11._ |  April  1-5  |  [ Fast sorting.  
Algorithm design paradigms. ](notes11.html) |  _Tuesday, April  2: [ Lab exam
2 ](labexam2sample.html) (on trees). _ |  [ Take-home exam 2 ](takehome2.html)
handed out ("SmartSort", using sorting techniques).  
_12._ |  April  8-12  |  [ A case study: SkipLists. ](notes12.html) |  TBD  |
_Take-home exam  2 due Monday (!), April 8\. _ (Postponed to Tuesday.)  
[ Assignment 5 ](assign05.html) handed out ("SkipList Demo").  
_13._ |  April  15-19  |  [ Hash tables. ](notes13.html) |  Tuesday, April 16:
[ Lab exam 3 ](labexam3.html) (cancelled).  |  
_14._ |  April  22-26  |  [ Balanced trees.  
Graphs. ](notes14.html) |  TBD  |  _Assignment  5 due Friday, April 26\. _  
_15._ |  Apr  29, May 1-3  |  [ Review. Demos. ](notes15.html) |  TBD  |  
  |  Thursday, May 9  |  _Thursday, May  9, 7:30-10:00 AM  
[ Final Exam ](final.html) _  
  
* * *  
  
## Grading policies

### Due dates and late policy

_Assignments are always due at midnight. You loose  20% of the points for each
day of being late._ (You lose the whole 20% at the stroke of midnight.) A
weekend counts as one day.

### Assignments

[Note added later: The term "Do-It-Yourself" assignment was later replaced by
"Take-home exam," which seemed clearer.]

There are a total of seven programming assignments. Two of them, Assignments A
and B, are of the "Do-It-Yourself" kind: You must do them by yourself. The
other five, Assignments 1, 2, 3, 4, and 5, are of the "Learn-With-Others"
variety: On these assignments you are encouraged to collaborate.

### Lab exams

There will be three "lab exams," where you will be asked to do some
programming in your recitation by yourself and turn in your work
electronically at the end of the recitation.

### In-class exams

There will be one midterm and a final. These are held in the classroom.

### Points and grades

The seven assignments (1, 2, 3, 4, 5, A, and B) are worth 65 points each. The
three lab exams and the midterm are worth 100 points each. The final is worth
200 points. Thus there is a total of 1055 points. [ _Note added later: Lab
exam  3 was cancelled and its 100 points were added to Assignment 5, making
Assignment 5 worth 165 points._]

Getting 900 or more points guarantees you an A, getting 800 or more points
guarantees you at least a B, getting 700 or more points guarantees you at
least a C, getting 600 or more points guarantees you at least a D, getting
less than 600 points may get you an F.

+/- grades will be given to raise some grades. The extent to which this is
done may differ among recitations since their lab exams may turn out to be of
slightly different levels of difficulty (which we try to avoid but which can
happen).

## Collaboration

_You are very much encouraged to collaborate on the "Learn-With-Others"
assignments (Assignments  1, 2, 3, 4, and 5). The two "Do-It-Yourself"
assignments (Assignments A and B) you have to do by yourself._

The recommended mode of collaboration on the "Learn-With-Others" assignments
(Assignments 1, 2, 3, 4, and 5) is to write your own program but feel free to
discuss any and all aspects of your program with anyone else, including
details of the code. Naturally, simply copying someone else's code does not
teach you anything except how to use the copy command, which is not a strong
foundation for an illustrious career in the software field. Also be aware that
these "Learn-With-Others" assignments only add up to a fraction of your total
grade. Use them to learn how to do the work so that you can show your
programming competence on the "Do-It-Yourself" assignments and on lab exams.

[A [clarification](news.html#collaboration) of this policy was posted later.]

_On the "Do-It-Yourself" assignments (Assignments  A and B) no collaboration
of any kind is acceptable._ Treat them like take-home exams that you are
supposed to do by yourself. If you get caught violating this rule you get an F
in the course just as you would if caught copying on an exam.

Obviously the rules of academic honesty as published in the catalog apply
(except for the "Learn-With-Others" assignments as described above). The rules
spelled out above apply to Sections 020 and 030 of CSCI 2270 (taught MWF
1-1:50PM in ECCR 200). Section 010 (taught MWF 11-11:50AM in ECCR 245) has a
different instructor, different assignments, and probably different rules.

* * *

[Next page](assign01.html) | Back to top

* * *

(C) 2002 Karl Winklmann

9:31 AM, Saturday, May 11, 2002

