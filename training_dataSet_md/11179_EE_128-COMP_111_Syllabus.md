## EE 128/COMP 111 Spring 2002

# Operating Systems: Syllabus

Daniel E. Bromberg, Adjunct Professor  |  bromberg@eecs.tufts.edu  
---|---  
John Hart, Teaching Assistant  |  jhart@eecs.tufts.edu  
  
* * *

### Course overview

Operating Systems form the core of all contemporary software environments,
from supercomputers to handheld digital assistants. An operating system, a
low-level software entity, forms the link between a computer's physical parts
(the hardware) and abstract systems and applications (the software) -- such as
compiling C programs and reading e-mail.

This course intends to present and explain all the major concepts that
underlie a correct, reliable, and versatile multi-tasking OS. The emphasis
will be on modern personal computers and single-processor workstations and
servers, the types of computers you encounter daily in school and work. There
will be some coverage of multiprocessor and embedded systems as well. While we
will not trudge through all the details of a particular OS or write an OS from
scratch, we will frequently tie the concepts to real-world examples, including
actual source code, technical articles, and layman news articles. You will get
overviews through bi-weekly lectures, and get direct practice through frequent
written homework assignments, monthly tests, weekly question & answer section
meetings, and most importantly, 5 hands-on programming-intensive laboratory
assignments. Assignments will involve parallel tracks of C and Java
programming. C will be used early on to showcase direct interaction with the
Unix kernel C API, and Java will be used extensively and throughout to
practice general concepts such as networking and multi-threading in a
standardized, OS-independent environment.

### Rationale

As any book on Operating Systems will explain, there are many reasons to learn
in depth about operating systems even if you will never become one of the few
OS engineers in industry. Knowing how a system works makes you a better user
and systems administrator. You will be able to configure, install, and fix
software without relying on technical support or a techie friend, and make
better informed technology purchasing decisions.

Mastering OS concepts will also help you become more versatile engineer and
programmer. The top engineers always understand several levels above and below
the level they're working on. Exposure to the innards of an OS forces you to
master complexity and modular design; learn how robust algorithms can be
implemented in highly parallel, resource-competetive environments; and analyze
and balance the engineering tradeoffs inherent in any complex system.

### Goals

We will try to take away the natural reticence to "looking under the hood" and
de-mystify what's really going on when you save a file, load a web page, or
watch helplessly as your computer crashes with the Blue Screen of Death.
Furthermore, we hope to breed excitement, enthusiasm, and savvy about systems
for exploration in your future career or as a hobby. In the process, we will
help you become more seasoned programmers and software designers by expanding
your vocabulary of languages, APIs, protocols, and design patterns.

### Required Text

![](cover-tiny.jpg) |  _Applied Operating System Concepts_  
Abraham Silberschatz, Peter Galvin, Greg Gagne  
HardCover - 840 pages  
John Wiley  & Sons, Inc. (2000)  
ISBN: 0-471-36508-4  
  
---|---  
  
### Course plan

#### Module 0

To motivate the material, we will look at a very brief historical evoluation
of OSes, the major current players, and their capabilities.

#### Module 1

We will begin the main track by touring the Unix shell user environment as it
provides a relatively direct view of the facilities directly provided by the
operating system. We will implement usable command substitutes to demonstrate
system programming. At the same time, we will introduce Java, the Java Virtual
Machine (JVM), and basic object-oriented constructs.

#### Module 2

Once the capabilities of the Unix OS have been demonstrated, we will look
deeper into the actual implementations within the kernel. After outlining the
system call interface (the entry point into the kernel) we will spend
substantial time studying the process model: scheduling, priority,
creation/tear-down, hierarchy, and threading. Working knowledge of Java will
be assumed and will be used to practice these constructs. Device I/O will be
introduced as necessary.

#### Module 3

Now that the heartbeat of the system has been established, we will examine how
the system balances the demands of intercommunication amongst processes and
between processes and the hardware: mutexes, semaphores, message queues,
pipes, and interrupt handling. I/O will be further included as needed.

#### Module 4

Next we will study how the OS handles the dynamic memory requirements of
processes and provides an easy-to-use, vast, and flat memory model to all
processes efficiently and without conflict: the Virtual Memory system.

#### Module 5

Longer-term (stable) memory allows processes and users to save and resume
their work: the next fundamental component is the filesystem. We will see how
the OS can support heterogenous file formats, even combining remote and local
filesystems, in a seamless, consisent format. We will also examine how a local
filesystem is layered on a raw disk paritition and locking at the file level.

#### Module 6

The filesystems will provide a segue to fill out our look at I/O systems. We
will see how the OS handles vast differences in bandwidth/latency between fast
(clocked) components and slow (mechanical) components as well as resolving
multiple simultaneous requests for the same device. We will examine and
simulate caching and scheduling algorithms and see how a reliable, fast
storage hierarchy is built.

#### Additional

As time allows, we will gain some broader perspective of computer systems.
Most likely we will look at networked OS coordination through standard
Internet utilities such as ftp and rsh, and some general, introductory
distributed issues such as time synchronization (xntpd). If possible we will
also look at the peculiar demands of very small (embedded) OSes and very large
(redundant disk/multi-processor systems.)

### Tools

You should be well-versed in E-mail and browsers as described below. You
should be able to operate the GNU tools and editors as a basis to learn more.
You should expect to become very familiar with Unix shell, gcc, jikes, jdb,
and java.

  * GNU C tools (gcc, gmake, gdb) -- compile, link, & debug Unix system programs 
  * GNU Emacs editor -- code development 
  * Jikes: the IBM open-source Java compiler -- compile Java programs 
  * java, jar, jdb -- run, archive, and debug Java programs 
  * Unix shell -- explore & learn Unix OSinterface, manage account 
  * E-mail -- to distribute timely information 
  * Web browser -- to do occasional research and on-line reading,   
access course website, submit programs, read and download course materials.

### Prerequisites

Intro: COMP-11 and Data Structures: COMP-15;  
Familiarity with using Emacs/C compiler on Unix  
Curiosity about Systems

###  Administrative Details and Course Schedule  
  
---  
  
#### _Note: information is subject to change (always accompanied by
announcements). A printed copy may become outdated especially with respect to
the schedule._  
  
**Lectures** |  Tuesdays  & Thursdays, 5:10-6:30 PM. Halligan Hall Room 108.  
Lectures start strictly on time. There will be a very short break in the
middle. While I do not mind if you are a few minutes late here or there,
leaving early is disruptive and strongly discouraged. If you come, please stay
for the duration or let me know ahead if you must leave early.

**You are responsible for all material presented in lecture.** |  **Homework**
|  Approximately eight written assignments; comprises 20% of grade. Mostly
written exercises including short answer, quantitative analysis, technical
explanation, and a few short programs that must compile and run.  |  **Exams**
|  Two 45-minute quizzes. One 80-minute midterm. One 2-3 hour final.

The quizzes and midterms are on the 3rd class of each month:  |  Feb. 12  |
5:10-5:55  | Check-up quiz  
---|---|---  
Mar. 12  | 5:10-6:30  | Mid-term  
Apr. 23  | 5:10-5:55  | Final-primer quiz  | May 7  | 5:00-7:00  | Final  
**Grading** |  Homework: 15%; Quizzes: 7.5% each; Midterm: 15%; Final: 30%;
Labs: 25%

Disregarding outliers, grading will be on a curve. Expect to turn in all work
and show general understanding of all major topics to receive a B. High
accuracy and completeness on written assignments  & tests, as well as
programming assignments showing robustness or innovative ideas will be
required to earn an A.

Class participation, effort, and attitude will not be formally tracked, but
will be noted and definitely taken into consideration in borderline cases. It
can only help!  
**Sections** |  Attendance is not enforced but is highly recommended. Sections
are loosely structured and students are responsible for bringing their
questions, particularly about approaching homeworks and labs. About 1/3 of the
time will be spent going over prepared problems.

Section is an important place to develop a working relationship with your TA
so that he can understand your strengths and weaknesses and better help you.  
**Office Hours** |  We will have a total of about eight office hours per week.
Prof. Bromberg will most likely hold his hours just before class 3:00-4:30 Tue
and Thu. The remainder are TBA. We will survey best times at the 1st class
meeting.  
**On-Line Help** |  In order: check the course website, e-mail  course staff:
staff128@eecs.tufts.edu**. We will be checking our e-mail constantly and can
usually reply within a day.

There is no such thing as a stupid question so please be forthcoming. There
_is_ such a thing as an un-researched question: we are not inclined to repeat
material from lecture, section, the slides  & assignment handouts, and
elsewhere on the course website. Quite often answers to questions will be
generalized and echoed to the entire class so your questions just might save
someone's day.  
**Required Text** |  _Applied Operating System Concepts_  
Abraham Silberschatz, Peter Galvin, Greg Gagne  
HardCover - 840 pages  
John Wiley  & Sons, Inc. (2000)  
ISBN: 0-471-36508-4  
  
**Academic Honesty** |  Plain and simple. Discuss as many concepts as you
would like with your peers and mentors to reach understanding; help each other
debug projects, especially compile-time errors.

**Write up your own solutions and prose. Don't study the solution of another
before you are done.**

Copying of code or prose is from others is not only self-defeating and easy to
detect (even in programming, everybody's style is different), **it invokes
undergraduate-wide policies on academic dishonesty.** Please see  these
policies for details.  
**Facilities** |  Halligan Hall Sun workstation labs. Details TBA.  
**Accounts** |  You should already have a Unix account and be able to login to
the Sun clusters. E-mail EECS staff if you need any help with your account.  
**Web Site** |  Please frequent  http://www.eecs.tufts.edu/g/ee128 for
updates.  
  
* * *

**Course Schedule**  
---  
**Date** | **Topics** | **Preparatory Reading** | **Assigned** | **Due** |
**Jan  17, 2002  
Course begins** |  Logistics - Course Structure, Content, Expectations - OS
purpose & defn - History Sketch - Current OSes  | This syllabus; AOS Ch. 1  |
Homework #1: Looking at OSes  | --  
**Jan  22** | Unix environment - shells, processes, utilities - OS
architecture - Java basics - C review  | AOS Ch. 3.1-3.2; Unix & Java reading
TBA | -- | --  
**Jan  24** | System-call API - #includes - make - man pages - Java packages -
Java architecture | AOS Ch. 3.3-3.10; Unix & Java reading TBA | -- | In-class
survey: your profile & interests  
**Jan  29** | Process Intro - Scheduling - Life-cycle - C Multiprogramming |
AOS Ch. 4.1-4.4; Additional C notes TBA |  | Homework 1 due  
**Jan  31** | Interprocess Communication - C Implementation |  |  | Lab #1
due: Charting Unix, Sipping Java  
**Feb  3** | Threads: User/kernel - multithreading models - Solaris |  |  |  
**Feb  7** | Threads: Java  |  |  | Homework 2 due  
**Feb  12** | Scheduling algorithms - fairness - starvation |  |  | **Quiz
#1:** 5:10-5:55  
**Feb  14** | Synchronization - critical sections - hardware support |  |  |  
**Feb  19** | Monitors - classical problems - Java synchronization |  |  |  
**Feb  21** | Deadlocks - definition - model - handling |  |  |  
**Feb  26** | Deadlocks - avoidance - detection - recovery |  |  |  
**Feb  28** | Memory management - swapping - allocation - paging  |  |  |  
**Mar  5** | Virtual memory - page table structure - demand paging -
replacement |  |  |  
**Mar  7** | Virtual memory - examples - cache maintenance - performance |  |
|  
**Mar  12** | Filesystems - user-view - abstract node layer - local vs. remote
|  |  | **Midterm:** 5:10-6:30  
**Mar  14** | Local filesystems - disk implementation - directory structure -
allocation |  |  |  
**Mar  26** | Local filesystems - free-management - performance - recovery |
|  |  
**Mar  28** | Remote filesystems - servers/daemons - locking/delays - AFS/NFS
|  |  |  
**Apr  2** | I/O system - intro - hardware - API  |  |  |  
**Apr  4** | I/O Kernel subsystem - I/O request handling - performance |  |  |  
**Apr  9** | Network structures - types - communication protocols |  |  |
**Quiz #2:** 5:10-5:55  
**Apr  11** | Networks - robustness - design - examples |  |  |  
**Apr  16** | Distributed communication - sockets - RMI - CORBA |  |  |  
**Apr  23** | Distributed coordination - event ordering - mutual exclusion |
|  |  
**Apr  25  
Last day** | Summary - Where to go next - Suggestions for further research |
|  | Lab #5 due: Java filesystem  
  
Page accesses:  _Last modified: Wed Jan 08 EDT 2001_

  * ### Main Page

  * ### Announcements and News

  * ### TA hours

  * ### Syllabus

  * ### Lecture Slides, Section, & Homeworks

  * ### Additional Hints & Reference

  * ### Q & A Archive: Assignment Questions

  * ### Submit Assignment

* * *

### EECS Department Administration

Tufts EECS Home  
---  
COMP 111 Course Catalog Entry  
  
* * *

Last Updated: Mon Apr 8 2002

* * *

