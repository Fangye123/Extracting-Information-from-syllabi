# Introduction to DataBase Management Systems

## Bob Matthews

## Department of Mathematics and Computer Science

## January, 2001

## Working Draft

* * *

## Administrivia

  * **Meeting times:** 3 - 3:50 MTThF Thompson 322
  * **Final Exam:** Thursday, May 11, 4:00 PM **required**
  * **Instructor:**
    * Bob Matthews (email matthews@ups.edu)
    * Thompson 502
    * Extension 3561
  * **Office hours (tentative):**
    * 2:00 MTThF
    * Or by appointment.

If you catch me free at any time, please feel free to drop in. Messages sent
via email are welcome, and can be used to ask a question or to set up an
appointment.

  * **Textbook**
    * **Required:** **Required:** Date, C. J. **An Introduction to Database Systems** (Seventh Edition). Addison-Wesley, 2000 We will cover chapters 1 - 11, 13, 24, 25 For detailed reading, check the current week's schedule. We will dip into the reading supplement from time to time.
    * **Required:** Sunderraman, Rajshekhar, **Oracle Programming: A Primer** , Addison-Wesley, 1999. We will try and cover the entire book (assuming that I can still get the JDBC to work).
    * **Required** :  Oracle tutorials on database tools (report writer, forms, menus) available on-line
    * **Strongly Recommended:**   Talks in the Thompson Hall Lecture Series on January 25 and February 15 (these will be talks on GIS, and will directly relate to the course material)
    * **Course Notes:** Course notes from last year will be available on Plato.

All books are currently available at the Bookstore. Additional references can
frequently be found at **Boarders** or at **amazon.com**.

* * *

## Weekly reading and lecture schedule

  * [This Week](thisweek.html)
  * [Next Week](nextweek.html)
  * [Previous Weeks](previousweeks.html)

* * *

## Assignments

  * [Exercise #1](Exercise01.html) (Due Thursday, Feb. 1)
  * [Exercise #2](Exercise02.html) (Due Friday, Feb. 2)
  * [Exercise #3](Exercise03.html) (Due Friday, Feb. 23, in class)
  * [Exercise #4](Exercise04.html) (Due Tuesday, March 20)
  * [Remaining Exercises](remaining.htm) (Due Various)

* * *

## Exam reviews

  * [Exam 1 Review](Exam1Review.html)
  * [Exam 2 Review](Exam2Review.html)
  * [Exam 3 Review](Exam3Review.html)
    * [exam_#3_question_II](exam_%233_question_ii.htm)
  * [FinalReview.htm](FinalReview.htm)

##

* * *

Group Projects

  * [Group Project Document](group.html)

* * *

## Evaluation

  * Three hour exams + a comprehensive final: 50% (The final exam will have the weight of two hour exams)
  * Written and programming exercises: 30%
  * Group project: 20%

* * *

## Notes:

### Grading Policies

Programming exercises will be graded on style and documentation as well as
correctness. Programs and control scripts must include header documentation as
well as adequate internal documentation unless otherwise specified. Late
assignments will generally not be accepted, will incur an increasing penalty
when accepted, and will certainly not be accepted after the graded exercise is
returned to the class unless I have asked you to correct and resubmit the
exercise. Late exercises must be submitted in hard-copy form with listings of
the assignment source and of test runs. Programs marked for correction and re
submission must be turned in within a week of the day that the assignment was
returned to the class. If a program or control script meets requirements,
works OK, is readable, and at least minimally documented (header documentation
and some internal documentation at important points, it earns between 70% and
80% of the points possible. If a program or control script is well structured,
meets all tests (tests are driven from the statement of the assignment, and
the specific tests I will use on your program will be taken from the problem
description in the assignment write-up, but the specific tests will not
generally be provided in advance), and is well documented, it will earn
between 80% and 95% of the total possible points. To earn 100% of the total
possible points, the program or control script must meet all of the above and
do something exceptional beyond the statement of the program.

A minimum grade of 50% on exams and 50% on homework assignments is a necessary
(but not necessarily sufficient) condition for a passing grade. All
assignments turned in must represent individual effort: work done by a
committee cannot be accepted except where a group effort is a clearly stated
part of the assignment. All students in Computer Science classes at the
University of Puget Sound are responsible for the material contained in the
document on academic honesty published by the Department of Mathematics and
Computer Science and included in the Academic Handbook The final exam will
have the weight of two hour exams.

## Important notes:

  * While courses generally change from semester to semester, this semester CSci 455 is very much a course in transition this term. This is because 
    * I want to include more about internet applications
    * I want to talk a bit more than usual about object and semantic data models.
    * I want to include a section on GIS (Doug Edwards/Barry Goldstein)
    * I want to include at least a bit about Microsoft SQL Server (but the primary system we will use, and the system on which you will mostly be tested, is Oracle Developer 2000).

* * *

The final exam for this class will be Thursday, May 10, at 4:00 PM. It will be
a comprehensive, two hour in-class examination.

* * *

Should you find yourself in difficulty at any point in the semester, please
make arrangements to meet with me as quickly as possible.

* * *

## Course Syllabus

**COMPUTER SCIENCE 455** **DATABASE MANAGEMENT SYSTEMS**

### I. Introduction

  * **A.** Catalog Description The design and implementation of database management systems with emphasis on the relational and object-oriented models for data. Topics will include data models, design methods and tools for design, SQL, database tools, and implementation issues, and will include substantial work with a commercial main-frame relational database management system and associated tools. A group term project will be a significant part of the course. _Prerequisites_ : CSci 261, (MA 132 or MA 257).
  * **B.** Purpose CSci 455 is the capstone course in the Computer Science/Business curriculum. Its purpose is to present the basics of database management systems and the role these systems play in the modern business world. Students study the four basic data models for database management systems (with emphasis on the relational and object oriented models), database design, and implementation techniques, and gain substantial experience with a commercial main-frame relational database system and associated tools. A writing-intensive group project will be a significant part of the course. The course is also designed as an elective course in the Computer Science/Mathematics curriculum.
  * **C.** Prerequisites CSci 261, (MA 132 or MA 257). A grade of C- is required in the prerequisite courses.

### II. Required Topics

  * **A.** PROGRAMMING TECHNIQUES **(this is slowly being phased out of the course)**
    * Review of file organizations.
    * File techniques. 
      * Access methods in relative files.
      * The structure of indexed files.
      * The role of a file management system (e.g.., RMS)
      * B-trees
      * Implementing relational operations using indexed files
  * **B.** Database Techniques. 
    * Data models for Database Management Systems 
      * Hierarchical
      * Network/CODASYL
      * Relational
      * Object oriented models
      * Semantic models **(new!)**
    * Structured Query Language (SQL) 
      * Data definition
      * Data manipulation
    * The relational calculus and the relational algebra
    * The data dictionary
    * Other database systems/languages **(may not emphasize this term)**
      * Ingres/QUEL
      * Postgres (an object oriented database system)
      * Knowledge base systems
  * **C.** Software Engineering Techniques. 
    * The database design process. 
      * Entity-relationship diagrams (top-down design)
      * Forms-based design (bottom-up design)
      * Resolution of top-down and bottom-up design
      * Data-flow diagrams
      * Data normalization
    * Database development tools 
      * Forms development
      * Report Writers
      * Applications development
      * Embedded database languages
    * The software engineering process in the design and implementation of information systems.
  * **D**. Other New Features 
    * Geographic Information Systems (we may have one available to play with)
    * Microsoft SQL Server (available)
    * Internet applications (Oracle/JDBC + Microsoft ?)

Class exercises will include practice with actual database management systems.
The University of Puget Sound has a commercial copy of the Oracle relational
database management system which **is / may be** used for the majority of
database exercises in the class. In addition, software developed at the
University of Puget Sound will be used for exercises in the relational algebra
and relational calculus. Postgres may be used for exercises in object-oriented
database systems. The term project **(if used)** will involve a substantial
effort in the specification, design and implementation of a information system
using Oracle. The information system will include data entry/enquiry forms,
possibly embedded SQL code in C and Java programs, and the use of Developer
2000.

* * *

## Schedule

**Note:** Please note that, except for scheduled University events and exam
dates, the schedule of topics, readings, and assignments is **tentative**.
Please refer to the current weekly schedule posted above. It may be necessary
to change an exam date: if that happens, I will give you at least a week's
notice and make alternate arrangements for students unable to take the exam on
the rescheduled date. Please inform me of any conflict between the dates
entered here and those in the catalog and course schedule. In the event of any
conflicts, the catalog and course schedule have the final say. **Please
note:** It is not possible to change the date or time of the final
examination. **All** students in the class **must** take the exam at the date
and time given in the final exam schedule. The course is in roughly four
parts:

  * Introduction to Database systems, Oracle, and SQL
  * Database design
  * Database tools
  * More theory and future directions (most of the new material will go here)

The tentative schedule of readings and examinations is as follows. Several of
the readings overlap, particularly in the reference material to which we will
return several times during the semester.

* * *

## CSci 455 Lecture Schedule

## Spring 2001

* * *

### Notes:

  * This should be considered very much a document in development. While I will try as much as possible to stick to the posted exam dates, the schedule of lectures and homework may change as the term progresses. Updates, and detailed weekly plans, will be posted on the [ CSci 455 home page](http://www.math.ups.edu/~matthews/CS455/home.html).
  * Please note that reading assignments for an individual lecture should be completed before the lecture. Readings may include handouts to be provided, and may also include readings in books on reserve.

* * *

### Exam Schedule:

I will try very hard to adhere to the following exam schedule. If it becomes
necessary to change the date of an exam (except, of course, the final exam
over which I have no control), I will give the class advance notice, and work
to make arrangements for students who can not take the exam on the changed
date.

The date and time of the final exam is fixed by the Registrar. Should the date
and time I have for this exam conflict with the announced schedule, the
Registrar's schedule will apply.

  * Exam 1: Friday, Feb. 16
  * Exam 2: Friday, Mar. 23
  * Exam 3: Tuesday, April 24 (Please **note** that this is in the last full week of classes.)
  * The Final Exam for this class will be on Thursday, May 10, 4:00 PM

* * *

### Weekly Schedules:

Unless otherwise specified, readings refer to **Date**

Spring 2001 Schedule

Important Note: University dates are taken from the [Master
Calendar](http://www.ups.edu/dean/cal00-01.html) and from the schedule of [
final exams](http://www.ups.edu/registrar/sp01exam.htm). If there is a
disagreement between the dates below and those dates, the master calendar and
Spring 2001 schedule documents are the correct dates. Please let me know if
you spot any schedule disagreements.

The official schedules are available on the UPS web site,
<http://www.ups.edu>.

The following is a start-of-semester draft only, and is subject to change as
the semester moves on. I will, however, try very hard to stick to the
published exam dates. If it becomes necessary to change an exam date, I will
give you at least a week's notice.



  * Week 1: Monday, Jan. 15 
    * Topics: 
      * History and basic terms
      * A brief survey of data models
    * Reading: Date, Chapters 1, 2
    * Other Notes: 
      * Monday is Martin Luther King Day (no classes)
  * Week 2: Monday, Jan. 22 
    * Topics: 
      * The relational model
      * An introduction to Oracle
      * An introduction to SQL
    * Reading:  
      * Date, Chapters 3, 4
      * Sunderraman Chapters 1,2
      * EASYALG handout
    * Other Notes:
  * Week 3: Monday, Jan. 29 
    * Topics: 
      * SQL
      * An introduction to database design using entity-relationship diagrams
    * Reading: Date Chapters 4, 13
    * Other Notes:
  * Week 4:  Monday, Feb. 5 
    * Topics:Introduction to Oracle tools 
      * Report Writer
      * Forms Generator
    * Reading: 
      * Oracle Report Writer Tutorial
      * Oracle Forms Designer Tutorial
    * Other Notes: First hour exam will be next week
  * Week 5:  Monday, Feb. 12 
    * Topics: 
      * Advanced SQL (Views, Exists, etc.)
      * An introduction to the group project
    * Reading: Date Chapters 4, 9
    * Other Notes: 
      * **First Hour Exam Friday, Feb. 16**
      * Monday, Feb. 12 is the last day to withdraw with an automatic "W"
  * Week 6:  Monday, Feb. 19 
    * Topics: 
      * PL/SQL,
      * Data Dictionary
    * Reading: Date Chapters 4, 5, 9; Sunderraman Chapters 3, 4
    * Other Notes:
  * Week 7:  Monday, Feb. 26 
    * Topics: 
      * Bottom-up Database design
      * Data Normalization
    * Reading: Date 5, 10, 11
    * Other Notes: 
      * No class Friday (conference)
  * Week 8:  Monday, March 5 
    * Topics:Database Design:  Combining top-down and bottom-up design methods
    * Reading: Date 13
    * Other Notes: 
      * The second hour exam will be after Spring Break
      * Friday March 9 is Mid-Term (not an exam - just the date)
  * Week 9:  Monday, March 12 ( **Spring Break - no classes** )
  * Week 10:  Monday, March 19 
    * Topics: SQL Server
    * Reading: To be added
    * Other Notes: **Second hour exam Friday, March 23**
  * Week 11:  Monday, March 26 
    * Topics: Database theory:  RelAlg, RelCalc
    * Reading: Date 6 - 8 and handouts
    * Other Notes:
  * Week 12:  Monday, April 2 
    * Topics: Database theory:  Object-oriented and semantic data models
    * Reading: Date 24, 25 and handouts
    * Other Notes:
  * Week 13:  Monday, April 9 
    * Topics: Oracle tools:  Menu
    * Reading: on-line Oracle tutorial
    * Other Notes:
  * Week 14:  Monday, April 16 
    * Topics: Oracle tools:  JDBC 
      * Possibly also Microsoft tools
    * Reading: Sunderraman Chapter 5
    * Other Notes: The third hour exam will be next week
  * Week 15:  Monday, April 23 
    * Topics: Applications:  GIS and Decision Support
    * Reading: Date 24, 25
    * Other Notes: **Third Hour Exam Tuesday, April 24** (please note that this is during the last full week of class)
  * Week 16:  Monday, April 30 
    * Topics: Group presentations
    * Reading:
    * Other Notes:
  * Week 17:  Monday, May 7:  Final Exams Week 
    * **Final Exam Thursday, May 10, 4:00 PM**

* * *

Return to [my home page](http://www.math.ups.edu/~matthews/matthews.html)

