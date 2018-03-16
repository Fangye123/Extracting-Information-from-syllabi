**SYLLABUS  
**

**ICS 51 - Introductory Computer Organization  
Instructor Luis Miguel Campos  
Information and Computer Science Department  
University of California, Irvine  
**

  
**COURSE OVERVIEW  
**

This course is a first introduction to computer system architecture as would
be seen by a system designer. This course describes basic elements used in
putting together computer systems such as logic elements, functional units and
memory subsystems and the control for these subsystems that makes it possible
for the application programmer to use the machine. We will learn how computing
elements can be used for problem solving at various levels of abstractions. A
level can be thought of as a grouping of similar elements, with some generic
relationships between different levels. This grouping of things at a level and
its abstraction to a higher level is estabilishes a hierarchical relationship
between elements. This relationship aids understanding as well as breaks down
the system design tasks into manageable chunks. In our study of structures for
computation, we will employ six levels:

  * application 
  * assembly language 
  * operating system 
  * conventional machine 
  * microprogramming 
  * digital logic 

At the top level, we have functions and information structures that relate to
some application (e.g., airline reservations); at the lowest level, we have
flipflops, gates, and other hardware. Notice that of the six levels, five of
them are machine dependent, orienting the course towards concrete hardware
elements such as the choice of a microprocessor. However, a key subject of
this class is that logical properties, not physical realization, are
important. In that sense, hardware and software are logically equivalent. And
we will see this theme recur several times in our lectures.

  
  
  
**INSTRUCTIONAL OBJECTIVES**  

The purpose of this course is to learn computer structures and design so you
can use the computer as a tool in solving science and engineering problems.
After this course, you should be able to:

1\.

    Describe the function, structure and technology of basic computer components; 
2\.

    Explain computer operation at the instruction-set, register-transfer, and logic levels; 
3\.

    Write a simple microprogram; 
4\.

    Name and explain the basic functions of an operating system; 
5\.

    Describe how networks are organized and how they operate; 
6\.

    Program in an assembly language; 
7\.

    Perform some simple analyses of a real architecture. 

The objective of the lectures is to introduce and help you understand new
concepts. The lab has two objectives: illustrate the concepts introduced in
lectures and introduce you to assembly language programming. Since ICS 51
deals with hardware features and assembly language relates more closely to
hardware characteristics than does higher-level languages, they are both
covered in this course.

  
  
  
  
**COURSE REQUIREMENTS**  

The course is composed of four components: lectures, homeworks, labs, and
exams. The homeworks are based on lecture material and textbook readings. The
labs will focus on Pentium assembly language programming. Examinations will be
based on lectures, homeworks, and the lab.  

The lab will require additional lectures above and beyond those given during
the class period. These lectures will be covered using a combination of main
lab lectures and lab discussion sections. Lab discussions and exercises will
begin after the first lecture. Outside these times, your lab hour is to be
used for solving your lab assignments, where a 51 tutor will be available to
assist you.  

**ADMINISTRATIVE MATTERS**

`  
`**`Instructor`**` :  
Luis Miguel Campos  
CS 408/A  
Office Hours: by appointment.  
Email: `[`lcampos@ics.uci.edu`](mailto:lcampos@ics.uci.edu)  

**`Teaching Assistants`**` :  
TBA  
Office Hours: TBA  
Office: TBA  
Email: TBA`  

**`Teaching Assistants`**` :  
TBA  
Office Hours: TBA  
Office: TBA  
Email: TBA`  

**`Teaching Assistants`**` :  
TBA  
Office Hours: TBA  
Office: TBA  
Email: TBA`  

**`Teaching Assistants`**` :  
TBA  
Office Hours: TBA  
Office: TBA  
Email: TBA`  



    
    
    **Class Lecture: Tue, Thu** 14:00-15:20, RH 101 
    **Labs : Fri** 8:00-10:50 and 10:00-12:50, CS 183 
    **Labs : Fri** 11:00-13:50, CS 189 
    **Labs : Tue/Thu** 14:00-16:50, CS 189 
    **Discussions:** **Mon, Wed, Fri** , 17:00-17:50, ELH 100 
    

**Midterm Exam:** Thursday October 26th, in class, closed book.

**Final Exam:** TBA

  
  
**Text:** Tanenbaum, Structured Computer Organization, Prentice-Hall.  
  
  
**CLASS HOME PAGE:** `
http://www.ics.uci.edu/~lcampos/teaching/fall00/ics51.html`

**GRADING**  
  

Your grade in ICS 51 will depend on your performance in many areas: exams
(based mostly on class lectures but also the lab), homeworks (based on class
lectures), and labs. You will have two exams, 3-4 homework assignments, and 3
lab assignments. These will be weighted as follows (tentative):

> Homework - 0%  
>  Lab - 35%  
>  Midterm exam - 30%  
>  Final exam - 35%  
>

Note that individual homework assignments may carry different weights
depending on the degree of difficulty; likewise for the labs.

  
  
We try to grade material as quickly as possible, but in a large class grading
is not instantaneous. The policy is to have one person grade an entire
assignment, or in the case of exams, an entire problem. This assures us that
your problem will be graded fairly, as compared with the work of others in the
class.

  
  
All graded material--exams, homeworks, and labs--will be returned via the
Distribution Center. If you wish to have something regraded, you MUST write a
cover sheet and have it attached to the assignment. Explain why you believe
the problem (or problems) was misgraded. The Distribution Center will forward
your material to us. Note however that we will only consider regrades for a
period of **two weeks** following the date the material was returned to the
Distribution Center.

  
  
  
  
**OTHER**  
  

**Prerequisite:** ICS 22 and Math 6B (or equivalents).

  
  
**Adds and Drops:** Drops will be permitted only up to the end of the sixth
week. Please drop the add or drop cards in the class.

  
  
**Incompletes:** You will be excused from completing the required work only
after presentation of a medical certificate from the Student Health Center.

  
  
**HONOR STUDENTS:** Honor students will be given extra homework and/or lab
work to qualify them for the honor's credit.

**LECTURE SCHEDULE**  
  
  

The lectures will address general topics in computer organization. While the
body of the lecture material is drawn from the text, and the material for
laboratory discussions from the supplemental text, occasionally you may find
that some of the lecture material is not taken from the text, and more
importantly, that some of the lecture material is not even discussed in the
text. Consequently, the text should be viewed as supporting the lectures by
way of an example. Try to keep this in mind when reading the text, and when
attending lecture. This will require you to take careful notes during lecture,
as well as ask questions.

**Tentative Lecture Schedule**

    
    
    1         0. Welcome
    2	  1. Historical overview of computer architecture
    3-4       2. Computer hardware elements: CPU, memory, peripherals
    5-6       3. Gate-level view of components. 
    7         4. Interconnection elements: buses and interface logic.
    8         5. Microprograms
    9            Midterm
    10-11-12  5. Microprograms (cont)
    13-14  	  6. Instruction sets and addressing modes
    15	  7. Virtual memory
    

  

* * *

_Luis Miguel Campos_  
_2000-08-08_

