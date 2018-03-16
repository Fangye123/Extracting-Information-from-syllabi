![](logo.GIF)  
---  
  
|

* * *

Schedule | Instructors | [Laboratory](lab/cs340_lab.html) | Textbooks |
Syllabus | Online Resources | Tutoring | Requirements | Grading | Policies

##

* * *

Overview

Welcome to CS340, the logical successor to CS240. As you learned in CS240,
computer architecture is concerned with the structural organization and
hardware design of computer systems. The purpose of this course is to build
upon the knowledge and skills that you learned in CS240. We will do this using
a microprocessor trainer (the 68KMB). It will serve as an advanced example of
a computer architecture and also provide an environment for exploring advanced
assembly language programming. The environment, as the name 68KMB suggests, is
a 68000 based system (providing continuity with CS240).

For the first part of this course, we will extend beyond the basic assembly
language instructions and programming techniques that were learned in CS240.
For instance, concepts such as I/O (memory mapped vs. isolated I/O,
unconditional vs. program-conditional I/O), data acquisition (using DACs and
ADCs, sensors, and actuators), interrupts, direct memory access, exceptions
and traps will all be explored. For the second part of the course, we will
study advanced topics in the field of computer architecture. Probable topics
include reduced instruction set computers (RISCS), instruction-level
parallelism and superscalar processors, parallel processing, multiprocessors
and multicomputers, and memory systems.

The [laboratory](lab/cs340_lab.html) will follow closely the subjects taught
in lecture during the first part of the semester.

##

* * *

Prerequisites

> The only prerequisite is CS240. Please see instructor _immediately_ if you
have not taken CS240!

##

* * *

Schedule

> Lecture meets 1:30 - 2:40 P.M., Monday and Friday, in Room 173 of the
Science Center.

>

> Laboratory meets 2:15 - 5:15 P.M., Wednesday, in Room E125 of the Science
Center.

##

* * *

Instructors

|

**Lecturer:** |

[Jennifer Stephan](http://www.wellesley.edu/CS/jstephan.html) (please call me
Jennifer)  
---|---  
  
**Office:** |

E104 Science Center  
  
**Phone:** |

x3152  
  
**Email:** |

[jstephan@wellesley.edu](mailto:jstephan@wellesley.edu)  
  
**Office Hours:** |

Wednesday 1-2:45 and by appointment  
  
|

(Note - Jennifer works part time and is in only on MWF)  
  
###

**Lab Instructor:** |

[Jean Herbst](http://www.wellesley.edu/CS/jherbst.html) (please call me Jean)  
---|---  
  
**Office:** |

131 Science Center  
  
**Phone:** |

x3162  
  
**Email:** |

[jherbst@wellesley.edu](mailto:jherbst@wellesley.edu)  
  
**Office Hours:** |

Monday 2:30 - 4:30 and by appointment  
  
|

(Note - Jean works part time and is in only on MW)  
  
* * *

**Textbooks and Other Course Materials**

**Required:** |

_The 68000 Microprocessor by I. Scott MacKenzie_

_68KMB Lab Manual by I. Scott MacKenzie_  
---|---  
  
**Optional:** |

_Computer Organization and Architecture by William Stallings, 5th edition_  
  
MacKenzie's and Stallings' textbooks can be purchased from the bookstore.
Alternatively, copies are also on reserve in the Science Center Library. (Note
- The 4th edition of the Stallings' text is on reserve and is sufficient.)
Because these texts are so expensive, please consider using the reserved
copies. Hopefully the small number of students in the course will make this
feasible. Also on reserve is the Motorola Programmer's Reference Manual that
we used in CS240. It might prove to be helpful, but is not at all necessary
for the course. The lab manual will be distributed to you during the first
laboratory section (free of charge).

###

* * *

**Syllabus**



For the first part of the course we will follow the MacKenzie textbook closely
(chapters 0 through 9). To begin the course we will spend a little time
reviewing the foundations for the course. Most of the material will be
familiar from CS240, but some will be new. We will then move on to learn about
the 68000 microprocessor (not the entire family of microprocessors, as was
studied in CS240). We will learn about its addressing modes, hardware and
entire set of instructions. Although some of what we learn will be familiar,
having studied the 68x000 family of processors, most of it will be new. We
will build upon our base of knowledge and explore the processor much more
thoroughly and in greater detail than we did for the family of
microprocessors. As a result, topics that were omitted entirely and details
that were "glossed over" in CS240 will be explored rigorously. For example,
(as stated earlier) concepts such as I/O (memory mapped vs. isolated I/O,
unconditional vs. program-conditional I/O), data acquisition (using DACs and
ADCs, sensors, and actuators), interrupts, direct memory access, exceptions
and traps will all be a focus.

For the second part of the course we will shift gears and study advanced
topics in the field of computer architecture. The exact topics and order of
topics will be determined. We will likely study chapters 5 (external memory),
12 (RISCS), 13 (instruction-level parallelism and superscalar processors) and
16 (parallel processing) of the Stallings' text. Additionally, we will study
selected special topics by reading important (classic and contemporary) papers
in computer architecture.

Click [here](schedule.html) to see a detailed schedule.

###

* * *

**Online Resources**

> There is a folder on FirstClass called CS340-S0-1 for this course. . All
class materials and handouts will be there. Those handouts that have been
handwritten or that aren't available in electronic form (for example, copies
of articles) can be picked up during office hours. You can use the folder to
post questions that you have about the lectures and assignments. We will read
the folder regularly; however, if you see a student's question to which you
know the answer, please go ahead and post the answer.

###

* * *

**Tutoring**

> There is no tutor for this course.

* * *

**Course Requirements**

> * Homework/Programming Assignments: There will be approximately ten
homeworks or programming assignments during the semester (see
[schedule](schedule.html) for due dates). The assignments will often require
the use of a 68KMB system. The department owns three 68KMBs and they "live" in
the Computer Science laboratory (Science Center E125). The laboratory will be
left unlocked for the semester, enabling you to access the systems at all
hours of the day (and night). However, there may be more than three students
in this course and thus there is a potential for conflict in using the
systems. For this reason, please do not wait until the last evening before an
assignment is due to work on it! Not having been able to use a machine the
night before the assignment is due is an unacceptable excuse for not having
completed the assignment. Please remember this and plan accordingly. Usually,
assignments will be due at the beginning of class on Fridays.  
>

> * Laboratory: The [ laboratory](lab/cs340_lab.html) is an integral part of
the course and attendance is mandatory. There will be a report required for
each laboratory section summarizing and synthesizing your findings. There will
be no distinct assignments for the laboratory. Rather, each homework
assignment will involve problems and topics pertinent to the current
laboratory. Thus, it is to your advantage to have at least begun the
assignment by the time laboratory meets. You should not expect, however, to be
able to complete the entire assignment before laboratory. It will sometimes
also be the case that the lab exercises will help you to finish the
assignment.  
>

> * Final Presentation: Each student is required to chose one article from the
research literature as her focus. You must master the article and then lead
the class on a discussion of it. Your "presentation" will take an entire
lecture and be held during class time at the end of the semester. All students
must read the article and contribute to the discussion. I will help you to
select the article from among a collection of more than 50 appropriate
articles. To this end, you must schedule a meeting with me before **March
16**. Your paper selection is due to me in writing by **March 30**.  
>

> * Exams: There are no exams in this course.  
>

> * Readings: There will be regular reading assignments that should be
completed when assigned (see [schedule](schedule.html) ).

### **

* * *

Grading**

> * Laboratory: 25%  
>

> * Homework/Programming Assignments: 45%  
>

> * Final Presentation: 20 %  
>

> * Class Participation: 10%  
>

### **

* * *

Policies**

> **Collaboration Policy**

>

> Collaboration on the course material is acceptable and encouraged provided
that each student submits her own individual assignments and indicates clearly
any other students with whom she works.

>

> #### **Late Policy**

>

> I don't like late assignments, but I am human. Should you need to request an
extension, it is paramount to communicate with me immediately. Class
extensions on an assignment will be announced in class and on FirstClass, so
please check the bulletin regularly! Formal solutions will be distributed soon
after the due date.

>

> #### **Students with Disabilities**

>

> I strongly encourage students with disabilities to visit me soon to discuss
appropriate accommodations that might be helpful to them.

>

>  

