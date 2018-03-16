![](FIGS/msurev1.gif) |

# EE 921 Advanced Topics in Digital Circuits and Systems

## Performance Instrumentation and Visualization for Concurrent Computer
Systems

College of Engineering  
Department of Electrical Engineering  
Spring Semester, 1997

* * *

# Syllabus

## Instructor

[Dr. Diane Rover](http://web.egr.msu.edu/~rover)  
Office: 155 Engineering Building  
Phone : (517) 353-7735  
Fax : (517) 353-1980  
Email: rover@egr.msu.edu  
Instructor Assistant: [Mr. Abdul Waheed](http://web.egr.msu.edu/~waheed)
Email: waheed@egr.msu.edu  

##  Course

  * **Course Web Page:**  
http://web.egr.msu.edu/VISTA/EE921

  * **Lecture Meeting Place/Time:**   
MW 11:30 a.m. - 12:50 p.m., room ??? EB

  * **Office Hours:**   
Monday, 10:30-11:30 a.m.  
Thursday, 2-3 p.m.  
Other times by appointment  

  * **Credits:**   
3

  * **Enrollment:**   
Open to Electrical Engineering and Computer Science graduate students.

  * **Suggested prerequisite:**   
CPS 820

  * **Grading:**   
Grading will be based on homework/laboratory exercises, individual and/or
group projects and presentations, written report(s), and several scheduled
quizzes throughout the term.

  * **Textbooks:**   
_Debugging and Performance Tuning for Parallel Computing Systems_ , ed. by
Simmons, Hayes, Brown, and Reed, IEEE Computer Society Press, 1996.  
[_Designing and Building Parallel Programs_ , Ian Foster, Addison-Wesley,
1995. ](http://www.mcs.anl.gov:80/dbpp/)  
Other reference material will be on reserve in the Engineering Library,
available electronically, or distributed by the instructor.

## Overview

This course was first offered in 1992 and was well-received by students in
both Electrical Engineering and Computer Science. The course incorporates
current tools and emerging computing models and environments. After taking the
course, students are well-positioned to apply performance tools in their own
studies.

The course provides an overview of performance analysis of parallel and
distributed computing systems; an in-depth study of contemporary tools for
monitoring, visualizing, and analyzing system performance as well as
particular resources within a system; and hands-on use of selected computer-
based tools. These topics continue to grow in relevance for users of high-
performance computing systems as well as for those involved in research and
development of hardware and software subsystems.

The course consists of lectures by the instructor, survey/discussion of
current literature, presentations by students, evaluation/testing of software
tools, group investigation of open problems, and possibly invited
presentations. Special projects undertaken in the course may include: use and
demonstration of a tool; development of computer-based performance analysis
learning modules (PALMs); design of a collaborative performance analysis tool;
and integration of several tools. A potential PALMs unit in the course will
introduce students to an educational paradigm called "active learning."
Through activities in the course, students will be able to focus their
attention based on interests in hardware or software. An interactive classroom
is planned.

## Objectives

Since the last offering of this course, the area of software tools and
environments has undergone a number of changes. The use of high-end parallel
systems is targeted to selected applications that require teraflops of
performance. Consequently, the size of the high-end parallel system market has
diminished. On the other hand, distributed systems with state-of-the-art
microprocessor architectures are delivering preferred price/performance
options for a broad range of applications. Therefore, software tool developers
are now shifting their focus toward this expanding area. Tool development as
well as performance measurement, analysis, prediction, and modeling are
actively being researched to address the latest generation of high performance
computing systems. This course gives students hands-on experience in this
dynamic field.

This course is designed around several objectives that will enhance the
student learning experience as well as performance in the course, and help in
future research and/or employment in this field of growing interest. The
objectives include:

  * **Broad awareness of contemporary parallel/distributed computing concepts and issues and hands-on experience using a parallel or distributed system.**  

  * **Hands-on experience with selected tools in a specific environment.**  
Everyone in the class is expected to learn about message-passing parallel
computing using the PVM message-passing library on a network of workstations.
Due to the popularity of PVM and many tools available for it, PVM is a
powerful environment for learning parallel programming and solving real
applications in different areas of science and engineering.

  * **Understanding of and experience with instrumentation systems.**  

  * **Understanding of and experience with performance visualization/analysis tools.**  
Students will complete a project using/developing a tool and give a
presentation based on the research literature about a tool or environment.

  * **Understanding and development of Performance Analysis Learning Modules (PALMs).**  
Students will select either Mathematica, Matlab, MS Project, or Excel as a
tool for demonstrating the solution to a performance evaluation problem.

  

**Overall Goals:**  
Take advantage of the _opportunity_ to learn and meet your responsibilities.

  1. Understand parallel/distributed systems 
    * Master fundamental concepts 
    * Develop skills for solving problems 
    * Appreciate advanced concepts and real-world issues 
    * Think critically about topics to gain insights 
  2. Understand how to apply modern tools and techniques 
    * Develop proficiency using the software tools
  3. Improve skills for working effectively with others 
    * Describe what you know to others 
    * Ask others to share their knowledge and insights with you (and listen to them) 
  4. Improve writing and speaking skills 
  5. Actively reflect on your learning in the course and the overall functioning of the course 
  6. Actively process the team/group work 
  7. Apply the concepts, principles, methods, etc. 
**Minimum Requirements:**

  1. Attend all classes (if you must miss a class, make arrangements as needed). 
  2. Read all assigned material. 
  3. Actively participate in class discussions. 
  4. Satisfactorily complete all graded work. 
  5. Participate fully in project groups (do your fair share of the work). 
  6. Submit all assignments with due dates on time and at an acceptable level of quality. 
  7. Complete and submit a course evaluation. 
  8. Follow University policy on integrity of scholarship and grades. 
  9. If you have special learning needs, please contact the instructor to make suitable arrangements. 
  
Note: email is an effective way to communicate with me.  
  

## Grading

**Grading Policy:** Final grades will be determined by your total score on
quizzes, homework, project, and presentation.  |

* **Quizzes (3)**|  150 Pts.|  25% | 
* **Project**|  240 Pts.| 40% | 
* **Homework/Lab**|  150 Pts.| 25% | 
* **Presentation**|  60 Pts.| 10% | 
* **TOTAL**|  600 Pts.| 100%   
The following grading procedure will be used. Grades are based on Dr. Rover's
Guaranteed Grading scale:  
  
| Range (%)| Grade | 88-100| 4.0 | 82-87| 3.5 | 74-81| 3.0 | 68-73| 2.5 |
60-67| 2.0 | 54-59| 1.5 | 46-53| 1.0 | 0-45| 0.0  
  
**Integrity & Ethics:** The policy of the University on integrity of
scholarship and grades (pages 49-50, Academic Programs, 1993) will be
followed. Implicit in graded work is that it represents the student's own
work, unless it has been explicitly designated as collaborative (group/team)
work.  
  

## Tentative Topics and Schedule (updated regularly on the Topics/Schedule web
page)

## Topics

### 1 Overview of Parallel and Distributed Systems

### 1.1 System Architectures

  * #### Parallel and Distributed Computer Models

  * #### Networks for Parallel and Distributed Systems

### 1.2 Software Environments

  * #### Parallel Programming Models

  * #### Parallel Languages and Compilers

  * #### Communication

  * #### Runtime Libraries

### 1.3 Areas of Current Research

  * VLSI and Microprocessor Design 
  * Embedded Distributed Architectures 
  * Parallel I/O 
  * Networking Technologies and Protocol Design 
  * Resource Management 
  * Real-Time Distributed Systems 
  * Integrated (and Usable!) Software Tools and Environments 
  
  
  

### 2 Overview of Performance Evaluation Methodologies

### 2.1 Complexity in Evaluating Concurrent Systems

### 2.2 Analytical Methods

### 2.3 Simulation-Based Techniques

### 2.4 Measurement-Based Techniques

  * Software Instrumentation 
  * Hardware Instrumentation 
  * Hybrid Instrumentation 

### 2.5 Hybrid, Rapid Prototyping Techniques

  * What is Meant by Rapid Prototyping? 
  * Example: Configurable Computing Machines 
  * Rapid Prototyping of Environments for Performance Studies 

### 2.6 Areas of Current Research

  
  
  

### 3 Measurement-Based Tool Environments

### 3.1 Standard Tool Technology (Middleware)

### 3.2 Instrumentation and Data Collection

### 3.3 Instrumentation Data Consumers (Tools) and Examples

### 3.4 Open Questions and Areas of Current Research

  
  
  

### 4 Instrumentation Systems

### 4.1 Historical Perspective

### 4.2 Specification, Design, and Synthesis

### 4.3 Modeling and Evaluation

### 4.4 Testing and Deployment

### 4.5 Selected Case Studies

### 4.6 Open Questions and Areas of Current Research

  * Global Event Ordering and Time-Stamps 
  * Information Sharing in a Heterogeneous Computing Environment 
  * Perturbation Modeling and Compensation 
  * Development of Extensible, Configurable, and Retargettables ISs 
  
  
  

### 5 Performance Analysis, Tuning, and Visualization

### 5.1 State-of-the-Art in Performance Visualization Methodologies

### 5.2 Tuning

### 5.3 Debugging

### 5.4 Steering

### 5.5 Case Studies of Contemporary Tools

  
  

## Schedule

|

* **Week 1**|  1/8/97| Course introduction | 
* **Week 2**|  1/13/97|  Overview of systems and performance evaluation; PVM and its tools; Project introduction  | 
* **Week 3**|  1/20/97|  | 
* **Week 4**|  1/27/97|  | 
* **Week 5**|  2/3/97| ______ | 
* **Week 6**|  2/10/97| Environments and instrumentation systems; Tool overview|  **QUIZ 1** | 
* **Week 7**|  2/17/97|  | 
* **Week 8**|  2/24/97| Project proposal (middle of term) | 
* **Spring Break**|  3/3/97|  | 
* **Week 9**|  3/10/97| ______ | 
* **Week 10**|  3/17/97|  Performance analysis tools and case studies|  **QUIZ 2** | 
* **Week 11**|  3/24/97|  | 
* **Week 12**|  3/31/97| Project progress report; Student presentations | 
* **Week 13**|  4/7/97|  | 
* **Week 14**|  4/14/97|  | 
* **Week 15**|  4/21/97|  Project demonstrations and discussions|  **QUIZ 3**   

* * *

[![](/img/buttons/return.gif) Return to EE921 Home Page](index.html)

* * *

[Diane T. Rover](mailto:rover@egr.msu.edu)

