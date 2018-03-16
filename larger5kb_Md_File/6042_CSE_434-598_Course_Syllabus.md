## CSE 434/598: Computer Networks

## Section A

## Fall 2000

* * *

### Course Information

**

Time & Location:

**

**Line Number** |  **

Class** |  **

Days** |  **

Time** |  **

Location**  
---|---|---|---|---  
  
79482 |

434 |

MWF |

9:40-10:30 |

PEBW 157  
  
64319 |

598 |

MWF |

9:40-10:30 |

PEBW 157  
  
**



Description:** Physical layer basics; network protocol algorithms; error
handling; flow control; multihop routing; network reliability, timing,
security; data compression; cryptography fundamentals. See
<http://www.eas.asu.edu/~csedept/academic/courses.html>

**

Prerequisites:** CSE 330 (or equivalent) _Note: a background in probability
and statistics will be very helpful._

**

Objectives:**

  * The emphasis of this course is on the Internet. 
  * Students will understand the issues associated with layered network architectures and be familiar with layer functions in the TCP/IP and OSI Reference Models. 
  * Students will be familiar with services provided by the application layer. 
  * Students will understand issues and design of transport protocols, including TCP.
  * Students will understand the issues and design of various network protocols, including IP and IPv6. 
  * Students will be able to evaluate various routing algorithms. 
  * Students will be able to evaluate error control and flow control techniques. 
  * Students will become familiar with basic queueing theory and its application to performance issues in multiple access protocols. 
  * Students will understand physical layer basics, including signaling, transmission, multiplexing, and switching. 

**

Course Homepage:** <http://www.eas.asu.edu/~cse434>

**

Text:** _Computer Networking: A Top-Down Approach Featuring the Internet_ by
James F. Kurose and Keith W. Ross (Addison Wesley Longman, Inc.) 2000. ISBN
0-201-47711-4

* * *

### Instructor Information

**

Instructor:** Dr. Barb Gannod

**

Office Location:** GWC 378

**

Office Phone:** 965-1757

**

Email Address:** [bgannod@asu.edu](mailto:bgannod@asu.edu)

**

Web Address:** <http://www.public.asu.edu/~bgannod>

**

Office Hours:**

    
    
             Monday         8:30-9:30  AM
             Wednesday      8:30-9:30  AM
             Friday       	8:30-9:30  AM
    
             (or by appointment)

* * *

### Teaching Assistant Information

**

TA's name:** Ting Liu

**

Office Location:** GWC 230

**

Office Phone:** (please use ONLY during office hours)

**

Email Address:** [tliu@asu.edu](mailto:tliu@asu.edu#tliu@asu.edu)

**

Office Hours:**

    
    
             Monday      	3:00 - 4:30 PM
             Wednesday     	3:00 - 4:30 PM

* * *

### Grading

### The grades reported to the University are based on the following scale:

**CSE 434/598**  
---  
**

Percentage  ** |  **

Grade  **  
  
90-100% |

A  
  
80-89% |

B  
  
70-79% |

C  
  
60-69% |

D  
  
Below 60% |

E  
  
**

Grades are based on the following components

**



**Component** |  **

CSE 434 Percentage** |  **

CSE 598 Percentage**  
---|---|---  
  
Exam#1 (Oct. 2) |

15% |

15%  
  
Exam#2 (Nov. 20) |

15% |

15%  
  
Final Exam (Dec 11 -- 7:40 AM) |

20% |

20%  
  
Homework |

15% |

10%  
  
Quizzes |

15% |

15%  
  
Projects |

20% |

15%  
  
Term Paper (due Dec. 1) |

\--- |

10%  
  
**

Exams**

All of the exams will be closed book exams. Students may use ONE SIDE of an
8.5 x 11 sheet of paper as a "cheat sheet" for the exams. Missing an exam is
grounds for receiving an E in the class.

**

Homework**

Several written homework assignments will be given throughout the semester.
These assignments will cover the reading and the class material. To be
eligible for credit, each assignment solution must fulfill the published
requirements and must be completed by the published due date. Homework is due
at the beginning of class. Late assignments will NOT be accepted unless
appropriate arrangements have been made with the instructor.

**

Quizzes**

Quizzes will NOT be announced. Any quiz that is missed will receive a score of
zero -- no exceptions. NO MAKE UPS WILL BE GIVEN. The lowest quiz score will
be dropped at the end of the semester.

**

Projects**

Various computer-related projects will be assigned during the semester. These
projects will give practical experience with the concepts learned in the
reading and class discussions. Any student who completes only one half (or
less) of the projects will receive a grade of E FOR THE COURSE. Students can
work in any campus computing or on their home computers.

**

Term Paper**

Those students enrolled in CSE 598 must complete a term paper that will be due
at the end of the semester. A project proposal will be due at the end of
February. More details will be given in class.

* * *

### Notes

  * If a student does not attend class for the entire first week of the course, the instructor WILL drop the student from CSE 434/598 on the basis of non-attendance. 

  * The instructor reserves the right to modify course policies, course calendar, assignment values and due dates, as circumstances require. 
  * Any extenuating circumstances that have an impact on your participation in the course should be discussed with your instructor as soon as those circumstances are known. 
  * Make-ups for graded activities (except quizzes) _may_ be arranged if a student's absence is caused by documented illness or personal emergency. A written explanation (including supporting documentation) must be submitted to your instructor; if the explanation is acceptable, an alternative to the graded activity will be arranged. When possible, make-up arrangements must be completed prior to the scheduled activity. 
  * The Department of Computer Science and Engineering expects all students to adhere to ASU's policy on Academic Dishonesty. These policies can be found in the Code of Student Conduct: 

<http://www.asu.edu/aad/manuals/sta/sta104-01.html>

In particular, any materials submitted for evaluation (homework, quizzes,
exams, and projects) must be your own work. You are encouraged to discuss the
assignment specifications with your instructor, your teaching assistant, and
your fellow students. However, anything you submit for grading must be unique
and should NOT be a duplicate of another student's submitted work. Any student
who violates the Student Academic Integrity Policies will, as a minimum,
receive a course grade of E.

* * *

## Tentative Schedule

This course will cover parts of Chapters 1-7, and will emphasize wired LANs.

  1. Introduction (Chapter 1)
    1. Overview of the Internet
    2. "Inside" the network
    3. Network architecture models
  2. Application Layer (Chapter 2)
    1. Overview of Application Layer Protocols
    2. HTTP
    3. FTP
    4. Email
    5. DNS
    6. Socket Programming
  3. Transport Layer (Chapter 3)
    1. UDP
    2. Stop-and-wait protocols
    3. Sliding window protocols
    4. TCP
    5. Congestion Control
  4. Network Layer (Chapter 4)
    1. Routing Algorithms
    2. IP (v4)
    3. Internet Routing
    4. IP (v6)
  5. Link Layer (5.1-5.8)
    1. Error detection and correction
    2. Multiple access protocols
    3. ARP
    4. Ethernet
    5. PPP
  6. OSI Physical Layer (supplemental material)
    1. Analog and Digital signaling
    2. Analog and Digital transmission
    3. Data Rates
  7. Network Security (Chapter 7 as time permits)
    1. Cryptography
    2. Authentication
    3. Secure Email

