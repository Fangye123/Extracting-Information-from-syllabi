##  **Software Engineering II**  
**CS 362 Course Syllabus**  
**Summer 2002**  

* * *

### CS 362 FAQ:

Check the [ CS 362 FAQ](faq.html) for answers to frequently asked questions.

* * *

### **Table of Contents**

  * Course Information
  * Course Description and Learning Objectives
  * Grading Criteria
  * Course Policies
  * Calendar
  * Detailed Course Schedule
  * Other Links

* * *

### Course Information

Instructor: |  Vasanth Williams  
|  Office: |  Dear 115 |  Office Hours: |  M 12-1   T 11-12 W 11-12  |  Email:
|  [williava@cs.orst.edu](mailto:williava@cs.orst.edu) |  OSU Class Hours: |
M/T/W/R 10:00 - 10:50 |  OSU Classroom: |  Milam 213. |  Prerequisite: |  CS
361. |  Credit: |  4 credit hours |  Text: |  Software Engineering, 6th Ed.,
Ian Sommerville, Addison Wesley, NY, NY, 2001. |  URL: |
http://www.cs.orst.edu/~williava/362S02/syllabus.html  
---|---  
  
* * *

### Course Description and Learning Objectives

Software Engineering is (1) the application of a systematic, disciplined,
quantifiable approach to the development, operation, and maintenance of
software, and (2) the study of such approaches. In CS 361, the prerequisite to
this course, you studied software lifecycle models, and focused on activities
in the "front end" of the waterfall lifecycle: requirements analysis,
requirements specification, and design. In this course, we will focus on
activities in the "back end" of the lifecycle, including implementation,
software verification and validation, and software evolution and maintenance.
We will consider both principles of, and tools and methodologies for
performing, these tasks.

On completion of the course, students will be able to demonstrate the ability
to:

  * Describe advantages of, and cost-benefit tradeoffs inherent in, the use of automated tools for building software and automating configuration management, such as Make and CVS, and use such tools in a realistic setting. 
  * Describe several techniques for validating and measuring the quality of software. 
  * Apply testing techniques including black-box and white-box techniques, automate testing activities, and perform regression testing. 
  * Use a debugger and other applicable techniques to locate faults. 
  * Describe several typical maintenance processes associated with correcting and enhancing software systems. 
  * Actively participate in a software inspection. 
  * Work effectively in teams.

* * *

### Grading Criteria

  * Midterm - 25 % 
  * Final Exam - 35 % 
  * Assignments - 40 %

I will assign readings from the course textbook, and additional readings from
other sources. Exams will address all material covered in class, assigned in
readings, or covered in assignments. The Midterm will be held in-class, and
thus will be limited to 1 hour and 20 minutes. The Final Exam will be held
during the assigned time and will use the entire time period allotted. I do
not grant exemptions from exams.

For further information see [Grades](./grades.txt).

* * *

### Course Policies

Attendance:      I will cover some material in class that is not covered in
the text; your assignments and test questions may be based on that material.
In particular, many of the details necessary to complete assignments will be
presented in class. Thus, it is to your benefit to attend class. Because late
arrivals are distracting, I also ask that you arrive to class on time.

Class preparation and participation:      I expect you to be prepared for
class, participate in discussions, and answer questions.

Assignments:      Assignments are due at the beginning of class on the due
date, unless otherwise specified. I don't accept late assignments. Assignments
include readings: you are responsible for ensuring that you have understood
the assigned reading material.

Adding the Course:      Due to the need to establish groups and begin working
on group projects, when the period for adding the course without the
instructor's approval expires (usually after the first week of classes), I do
**not** grant permission to add this course.

Collaboration versus Dishonesty:      I do not tolerate dishonesty. If I catch
you cheating, I will immediately assign you a failing grade for the course. On
the other hand, I encourage you to work with each other to understand course
material. Then, after you understand the material, go complete the assignment
on your own. An exception to this is group projects, of which we shall do
several. On group projects I expect and encourage collaboration between group
members, and I usually require only a single set of deliverables from the
group as a whole. If you are not sure, in specific cases, whether
collaboration is acceptable, or the degree to which it is acceptable, please
ask.

See also the [ Departmental policy on academic dishonesty
](http://www.cs.orst.edu/acad/policies/dishonesty.html).

**Detailed Schedule**

  **Class** | **Day/Date** | **Topic** | **Handout** | **Assignment**  
---|---|---|---|---  
1 | Mon 6/24 | This course. | Syllabus, Information sheet, Team Evaluation
sheet. Available in handout page | Assignment 1 (5 pts) due by next class.  
2 | Tue 6/25 | Software Process Models | Assignment 2 instructions, Aristotle
set-up instructions handed out in class and available on course handouts page.
Class slides can be found in the text book website, www.software-engin.com |
Assignment 2 (10 pts) due Thursday 6/27  
3 | Wed 6/26 | System Build Procedures and Make | Dejavu documentation handed
out in class, and available on course handouts page. Document on Make and
Dejavu source code made available in handouts area. | None.  
4 | Thurs 6/27 | Makefile.  | Assignment 3 instructions and Sample Make file |
Read Sommerville Chapter 29 for Monday, . Assignment 3 (40 pts): due Wednesday
next week.  
5 |  Mon 7/1 |  Configuration Management |  None |  None  
6 |  Tue 7/2 |  Configuration Management and CVS |  None |

Read the "Introduction to  CVS" at
http://[www.cvshome.org/docs/](http://www.cvshome.org/docs/) blandy.html  
  
7 |  Wed 7/3 |  CVS and Assignment 4 |  Assignment 4 instructions handed out;
available on course handouts page. |  Assignment 4 (40 pts): due Thursday 7/11  
8 |  Thurs 7/4 |  4th July (Holiday) |  None |  None  
9 |  Mon 7/8 | CVS, Testing and Validation and Black-Box testing |  None. |
Read Sommerville pages 420-425 and chapter 20.  
10 |  Tues 7/9 | Black-Box Testing | Sample requirements for sqrt function and
portion of testplan handed out and available on course handouts page |  None  
11 |  Wed 7/10 |  Black-Box Testing and assignment 5 |  Assignment 5
instructions handed out and available on course handouts page. |  Assignment 5
(50 pts): due Wednesday 7/17  
12 |  Thurs 7/11 |  WhiteBox Testing |  None |  None  
13 |  Mon 7/15 | White-Box testing, Control Flow graphs and Assignment 6
(partial) | Assignment 6 instructions handed out and available on course
handouts page and test coverage information handed out. |

Assignment 6 (50 pts) due by Tue  7/23.                      Study pages 1-15
of Rothermel/Harrold paper available at Rothermel's Paper site, and skim the
remainder for Tue 7/16  
  
14 |  Tue 7/16 |

 Paper about Dejavu: "A Safe, Efficient Regression Test Set Selection
Technique", G. Rothermel and M. J. Harrold, available at [Rothermel's paper
site](http://www.cs.orst.edu/~grother/papersall.html) (1997, paper number 2).
And Assignment 6 discussion.

|  None |  None  
15 |  Wed 7/17 |  Review for Midterm. |  None | None  
16 |  Thur 7/18 |  Midterm | None | None  
17 |  Mon 7/22 | Fault localization and debugging | None | None  
18 |  Tues 7/23 | Assignment 7 and Dataflow testing. | Assignment 7
instructions handed out and available on course handouts page. DejaVu bug
reports handed out and available on course handouts page. | Assignment 7 (30
pts): due Monday 7/29  
19 | Wed 7/24 | Dataflow testing. | Ostrand and Balcer "Category Partition
Method" paper handed out. This is not available electronically | Read Ostrand
and Balcer paper for Monday 7/30.  
20 | Thur 7/25 | Career directions in testing: Practice. Example: testing at
HP Presentation by a practicing software test engineer. | None | None  
21 | Mon 07/29 | Category-partition method and Assignment 8 | Assignment 8
handed out and available on course handouts page. "Torpedo" command
specification handed out and available on course handouts page. | Assignment 8
(40 pts): due Thursday 08/01.Read Sommerville: Section 3.6 page 63, Section
26.1 pages 582-7, and Chapter 27 pages 602-20, for Tuesday 7/30.  
22 | Tues 07/30 | Software maintenance | None | None  
23 | Wed 07/31 |

Career directions in testing: Research. Example: test prioritization by Dr.
Gregg Rothermel  

| None | None  
24 | Thur 08/01 |  Software inspections and Assignment 9.  | Assignment 9
handed out and available on course handouts page. | Assignment 9 (50 pts): due
Friday 8/8; Read Sommerville Section 19.2  
25 | Mon 08/05 |  Exchange materials for inspections and decide on inspection
meeting time  | None | None  
26 | Tues 08/06 | Inspections | None | None  
27 | Wed 08/07 | Inspections | None | None  
28 | Thur 08/08 | Inspections | None | None  
29 | Mon 08/12 |  Assignment 10, Evaluations, Review, Discussion of Final  |
Assignment 10 handed out and available on course handouts page. | Assignment
10 (Team Evaluation): due prior to Final Exam.  
30 | Tues 08/13 | Final Exam  | None | None  
  
* * *

### Calendar

**Date** |  **Notes** |  Monday 06/24 |  First day of classes |  Thursday
07/18 |  Midterm Exam in class. |  Friday  08/16 | End of term including Final
exam |  Tuesday 08/13 |  Final Exam.  
---|---  
  
* * *

### Other Links

[Grades](./grades.txt) |  [Course Handouts](./notes.html) |  [Aristotle
Information](http://www.cs.orst.edu/~grother/aristotle-local.html) |  [Project
Groups](./groups.html) |  [Unix Help](http://www.cs.orst.edu/facil/) |
[Top](./syllabus.html)  
---|---|---|---|---|---

