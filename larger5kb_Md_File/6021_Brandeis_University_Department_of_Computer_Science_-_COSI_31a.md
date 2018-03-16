![](simple-heading.gif)

#  **COSI 31a: Computer Structures and Organization**

# ** Fall, 1999

## **![](new.gif)Latest News**

12/12: The following are now available to help with your studying:

    * [Exam review problems](Examreview.txt)
    * [Exam review solutions](Examreviewsolns.txt)
    * [Final Exam solutions](Examsolns.html)

Good luck everybody!

##  **Description:**

This course is about the use, design, and implementation of operating systems.
Specifically, the goal of this course is for you to understand:

    * What is an operating system, what does it do, and why is it necessary?
    * The fundamental abstractions provided by operating systems.
    * The design issues and decisions that go into implementing these abstractions.

##  **Logistics:**

#### Professor:

     Prof. Mitch Cherniack ([mfc@cs.brandeis.edu](mailto:mfc@cs.brandeis.edu))     Office: Volen 137, x62738     Office Hours: Mon, 2-3:30 (or by appointment) 

#### TAs:

    Xiaoyu Wang ([wangxy@cs.brandeis.edu](mailto:wangxy@cs.brandeis.edu))     Office: Volen 111     Office Hours: Tue, 1:00-2:30

    Daniel Silberfarb ([pokerdan@cs.brandeis.edu](mailto:pokerdan@cs.brandeis.edu))     Office: Volen 104     Office Hours: Fri, 10:30-12

    Geoff Getz ([ggetz@cs.brandeis.edu](mailto:ggetz@cs.brandeis.edu))     Office: Volen 104     Office Hours: Thu, 2:00-3:00 (or by appointment)

#### Where and When:

    Meeting Place: 121 Gerstenzang     Meeting Time: 1:10-2:00 M, W, Th     Web Page: <http://www.cs.brandeis.edu/~cs31a/index.html>     Class Newsgroup: [news:brandeis.classes.cs31a ](news:brandeis.classes.cs31a)

##  **Course Requirements:**

**Prerequisites:**

**

The course prerequisites for COSI 31a are COSI 21a and COSI 21b. You should
have basic familiarity with Unix and either C, C++ or Java.

**

Assignments

**

There will be _seven_ problem sets and _two_ programming assignments. Both
problem sets and programming assignments will be provided in class, and
solutions to the problem sets will be posted on this page.

Hand in your homeworks before the beginning of class (i.e., by 1:10) on the
day the homework is due. **Please do each problem on a separate sheet of
paper**.

**

Readings

** The text for this course is

    * **Operating Systems: A Modern Perspective** , by Gary Nutt. (This is soon to be available at the bookstore. In the meantime, there are two copies on reserve in the Science Library.)
The course will largely follow the text, though occasionally, readings will be
assigned from elsewhere. Non-text readings will be available on reserve or
handed out in class. It is also strongly recommended that you buy or borrow a
text on Java, as that will be the language for programming assignments in this
course. For example, the classic Java reference is:

    * **The Java Programming Language** , by Ken Arnold and James Gosling (Addison-Wesley Publishers, 1996).
There are also numerous online references including:

    * [The Java Tutorial](http://java.sun.com/docs/books/tutorial/index.html)
    * [The Java Language Specification](http://java.sun.com/docs/books/jls/html/index.html)
    * [Java API Documentation](http://java.sun.com/products/jdk/1.1/docs/api/packages.html)
    * [Real's home(JAVA & JAVASCRIPT How-to)](http://www.geocities.com/SiliconValley/Vista/1337/realhome.html). A very helpful site with great examples.
    * [JDK tools from "Java in a nutshell"](jdktools/index.html)
**

In-Class Handouts

**

    * [Course Syllabus](index.html) (9/2) 
    * [Assembly Language Handout](AssemblyLanguageHandout.txt) (9/9) 
    * Java Handout (9/21). Available in the Office. 
    * [Programming Assignment 1: Shell](PA1.html) (9/23) 
    * [Midterm Review Problems](review.txt) and [Solutions](reviewsolns.txt) (10/13) 
    * [Programming Assignment 2: Bridges](PA2b.html) (10/21) 
    * [Microsoft NT's Page Replacement Policy](http://msdn.microsoft.com/library/techart/msdn_ntvmm.htm) (11/15, found by Sheeri Kritzer) 
    * ![](new.gif) [Exam Review Problems](Examreview.txt) and [Solutions](Examreviewsolns.txt) (12/12)  **

(Post midterm) Class Notes

**

    * [October 20](oct20.html) (Sheeri Kritzer) 
    * [October 21](notes1021.txt) (Steven Lubitz) 
    * [October 25](notes1025.html) (David Brooks) 
    * [October 27](notes1027.html) (Victoria Alesker) 
    * [October 28](notes1028.html) (Ross Schulman) 
    * [November 1](notes111.txt) (Jan Jirout) 
    * [November 3](notes113.html) (Radhakrishna Kamath) 
    * [November 4](notes1104.html) (Matt Kovner) 
    * [November 8](notes118.txt) (Adam Weinstein) 
    * [November 10](notes1110.html) (Fabricio Pettena) 
    * [November 11](notes1111.html) (Elin Barts) 
    * [November 15](notes1115.html) (David Lauer) 
    * [November 17](notes1117.html) (Eddie Galvez) 
    * [November 18](notes1118.html) (James Holley) 
    * [November 22](notes1122.html) (Marina Zlatkina) 
    * [November 24](notes1124.txt) (Catherine O'Meara) 
    * [November 29](notes1129.html) (Rahul Pande) 
    * [December 1](notes121.html) (Sarah Garb) 
    * [December 2](notes122.html) (Huiling Gong) 
    * December 6 - to come (David Haskell) 
    * December 7
      * [Course Divisions](course-divisions.txt)
      * [Summary of Abstractions](Abstractions.txt)
      * [List of Topics to Know](reviewtopics.txt) **

Lectures

** You are responsible for understanding **both** the material covered in the
readings and the lectures for this course. The purpose of the lectures is to:

    * help you to focus on the most relevant parts of the readings, 
    * help clarify questions about the readings, and 
    * supplement the readings with material otherwise not covered.  Lecture notes will often be borrowed from the slides available off of the textbook's web site at <http://www.cs.colorado.edu/~nutt/osamp.html>. You're encouraged to download these files for your notes, but note that the material presented in class will vary. 

**

On-line Support

** We will soon set up a [newsgroup](news:brandeis.classes.cs31a) for posting
and reading questions about topics relevant to this course (lectures,
readings, assignments etc.) Please post all of your questions to the
newsgroup, rather than sending e-mail to the instructor, except for questions
that only concern you (e.g., in order to set up an appointment to meet).

We will also use the newsgroup to post announcements regarding the course.
Make sure you check the postings regularly. If you are unfamiliar with how to
read news, speak to a TA.

## **Evaluation:**

**

Exams

**

There will be an in-class midterm (Oct. 18), and a final exam for this course.

**

Grading

**

Grades will be apportioned roughly as follows:

Midterm 15% Assignments 30% Programming Assignments 25% Final Exam 30% **

Late Policy

**

A late problem set will lose 20% for every day or part thereof that it is
late. Therefore, an assignment which is due on Thursday at 1:10 will be graded
as follows. Assume that the assignment is worth a grade of 100% before any
late penalty is applied. If that assignment is submitted between Thursday at
1:11 and Friday at 1:10, then it will receive a grade of 80%. If it is
submitted between Friday at 1:11 and Monday at 1:10, it will receive a grade
of 60%. If it is submitted between Monday at 1:11 and Tuesday at 1:10, it will
receive a grade of 40% etc. Note that no assignments will be accepted after
the solutions for that assignment have been posted.

Note also that no late submissions to PS 5 will be accepted so that we can
post the solutions well in advance of the final exam. A late programming
assignment will lose 20% for every week or part thereof it is late. **

Collaboration Policy

** Collaboration is neither permitted on the problem sets nor on the
programming assignments. You should see the TAs for help or an explanation.
You are responsible for protecting your homework directories so that others
cannot view them or copy them. Failure to do so constitutes a violation of
academic integrity. To protect a unix directory called "homework", "chmod og-
rwx homework".

##  **Students with Disabilities:**

If you are a student with a documented disability on record at Brandeis
University and wish to have a reasonable accommodation made for you in this
class, please see me immediately

##  **Due Dates:**

###  **Problem Sets:**

**PS 1** |  Out: 9/9 |  Due: 9/16 |  Problems: **1.6, 4.1, 4.6 (Hint: write
the Assembly Language equivalent first), 5.1**  
---|---|---|---  
**PS 2** |  Out: 9/16 |  Due: 9/23 |  Problems: **3.3, 5.3, 6.5 (See
hint[here](hint.html)), 6.7  
**PS 3** |  Out: 10/7 |  Due: 10/14 |  Problems: **7.7, 7.10, 8.3, 8.6, 8.9
(use semaphores)**  
**PS 4** |  Out: 11/4 |  Due: 11/11 |  The problem set is found
[here](ps4.html).  
**PS 5** |  Out: 11/11 |  Due: 11/18 |  The problem set is found
[here](ps5.html).  
**PS 6** |  Out: 11/18 |  Due: 11/24 |  The problem set is found
[here](ps6.html).  
**PS 7** |  Out: 11/29 |  Due: 12/6 |  The problem set is found
[here](ps7.html).  
  
###  **Programming Assts:**

**[PA 1](PA1.html)** |  Out: 9/23 |  Due: 10/7  
---|---|---  
**[PA 2](PA2b.html)** |  Out: 10/21 |  Due: 11/4  
  
### **Exams:**

**Midterm** |  10/18  
---|---  
**Final Exam** | _12/15, 1:30 PM  
  
## **Problem Set Solutions:**

    * [PS 1](ps1.jpeg)
    * [PS 2](ps2.txt)
    * [PS 3](ps3.html)
    * [PS 4](ps4.txt)
    * [PS 5](pa5.txt)
    * [PS 6](ps6solns.html)
    * [PS 7](ps7.sol)

##  **Schedule:**

As best as possible we will keep to the schedule below. Some topics may
require more time than is allotted, so the lecture schedule may get modified
as we get further into the course.

Please note that there will be no classes on the following days:

    * Mon, 9/6: Labor Day 
    * Mon, 9/20: Yom Kippur (Instead there will be class Tue, 9/21) 
    * Wed, 10/13: I'm Away (Instead there will be an optional final exam review class on Tue, 12/7) 
    * Thu, 11/25: Thanksgiving  The reading assignments cover the material that is discussed **that** week. To get the most out of the lectures, you should read this material before coming to class.

**

Week** |  **

Topic** |  **

Reading** |  **

Asst Out** |  **

Asst Due**  
---|---|---|---|---  
  
9/2 |

Introduction to Operating Systems

|

1, 2.1-2.2, 3 |

- | 

-  
  
9/8, 9/9 |

Basic Machine OrganizationAssembly Language

|

4, 5.1, [Handout](AssemblyLanguageHandout.txt) |

PS 1 (9/9) |

-  
  
9/13, 9/15, 9/16 |

Assembly Language (cont.)Processes and Threads |

2.3, 6 |

PS 2 (9/16) |

PS 1 (9/16)  
  
9/21, 9/22, 9/23 |

Processes and Threads (cont.)Java

|

[On-line tutorial](explore/index.html) _Any Java Book_ In-class Handouts |

PA 1 (9/23) |

PS 2 (9/23)  
  
9/27, 9/29, 9/30 |

Scheduling |

7 |

- | 

-  
  
10/4, 10/6, 10/7 |

Synchronization and Semaphores |

8 |

PS 3 (10/7) |

PA 1 (10/7)  
  
10/11, 10/14 |

Synchronization and SemaphoresHigh-Level Synchronization |

9 |

- | 

PS 3 (10/14)  
  
10/18, 10/20, 10/21 |

High-Level Synchronization |

- | 

PA 2 (10/21) |

Midterm (10/18)  
  
10/25, 10/27, 10/28 |

Deadlock |

10 |

- | 

-  
  
11/1, 11/3, 11/4 |

Memory Management |

11 |

PS 4 (11/4) |

PA 2 (11/4)  
  
11/8, 11/10, 11/11 |

Virtual Memory |

12 |

PS 5 (11/11) |

PS 4 (11/11)  
  
11/15, 11/17, 11/18 |

Files, Device Management |

13, 5.2-5.5 |

PS 6 (11/18) |

PS 5 (11/18)  
  
11/22, 11/24 |

Files, Device Management (cont.) |

- | 

- | 

PS 6 (11/24)  
  
11/29, 12/1, 12/2 |

Networks |

15 |

PS 7 (11/29) |

-  
  
12/6, 12/7 |

_TBA_ Final Exam Review (12/7) |

_TBA_ |

- | 

PS 7 (12/6)  
  
* * *

